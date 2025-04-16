import pygame



# Estrutura que controla o fluxo de clientes sendo atendidos
class Fila():
    def __init__(self,gc,x,y, filaMesa):
        self.clientes =[]
        self.screen = gc.screen
        self.x=x
        self.y=y
        self.gc=gc
        self.group = pygame.sprite.Group()
        self.padding =55
        self.capacidade=6
        self.filaMesa=filaMesa
        # :clientes:        Lista de clientes na fila
        # :screen:          Tela para renderizar imagem dos clientes
        # :x:               Posição x do início da fila 
        # :y:               Posição y do início da fila
        # :gc:              GameController para acessar prato e score
        # :group:           Grupo de sprites de clientes 
        # :padding:         Distância entre clientes 
        # :capacidade:      Tamanho máximo da fila
        # :filaMesa:        Estrutura que controla a ida as mesas

              
        
    def entra_cliente(self, cliente):
        self.clientes.append(cliente)
        self.group.add(cliente)
        self.update_client_positions()
    # Adiciona cliente a fila
    # Adiciona como sprite no grupo renderizador
    # Atualiza as posições x e y dos clientes da lista
        
    def sai_cliente(self, cliente):
        if cliente in self.clientes:
            self.group.remove(cliente)
            if not cliente.servido_certo:
                cliente.comido=True
                self.clientes.remove(cliente)
                del cliente
            else:
                self.filaMesa.alocar_cliente(cliente)
                self.clientes.remove(cliente)   
                 
        self.update_client_positions()
    # Remove cliente da lista e do grupo renderizador
    # Se não foi servido certo, comeu comida errada, 
    # é removido da lista e apagado. Se foi servido certo, 
    # manda para a fila de mesas e é removido da fila
    
    def update_client_positions(self):
        i = 0
        for item in self.clientes:
            item.rect.x = self.x + i * self.padding + 10
            item.rect.y = self.y
            item.x = item.rect.x  
            item.y = item.rect.y
            i += 1
    # Atualiza as posições x e y dos clientes da lista
    
            
    def draw(self):
        for cliente in self.clientes:
            # Desenha o cliente
            self.screen.blit(cliente.skin, pygame.Vector2(cliente.x,cliente.y))
            
            # Clone de urgencia do balao que fica vermelho
            balao_surface = cliente.balao_image.copy()
            
            # Tempo em ms para o fade do balao ficar suave
            tempo_percorrido= (pygame.time.get_ticks()-cliente.tempo_entrada)/1000
            
            # Balao começa a ficar vermelho nos segundos finais definidos por tempo_alerta
            if cliente.paciencia-tempo_percorrido< cliente.tempo_alerta:
                # Interpolação do balão
                intensidade = int(255 * ((tempo_percorrido+cliente.tempo_alerta-cliente.paciencia) / cliente.tempo_alerta))
                intensidade = max(0, min(255, intensidade))
                
                # Overlay que ficara vermelho
                overlay = pygame.Surface(balao_surface.get_size(), pygame.SRCALPHA)
                overlay.fill((255, 0, 0, intensidade))
                
                # Mascara aparecendo
                balao_surface.blit(overlay, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            # Balao base
            self.screen.blit(cliente.balao_image, pygame.Vector2(cliente.rect.topleft) + cliente.balao_offset)
            
            # Balao de urgencia
            self.screen.blit(balao_surface, pygame.Vector2(cliente.rect.topleft) + cliente.balao_offset)
            
            # Desenha o pedido por cima do balão 
            self.screen.blit(cliente.pedido_image, pygame.Vector2(cliente.rect.topleft) + cliente.pedido_offset)
            
    def update(self, events):
        self.group.update(events)
    # Atualiza o grupo de sprite por eventos (como click) e frames
    
    def cheia(self):
        if(len(self.clientes)==self.capacidade):
            return True
    # Retorna se a fila está cheia
    
    
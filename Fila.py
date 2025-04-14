import pygame


class Fila():
    def __init__(self,gc,x,y):
        self.clientes =[]
        self.screen = gc.screen
        self.x=x
        self.y=y
        self.gc=gc
        self.group = pygame.sprite.Group()
        self.padding =55
        
        
    def entra_cliente(self, cliente):
        self.clientes.append(cliente)
        self.group.add(cliente)
        self.update_client_positions()
        
    def sai_cliente(self, cliente):
        print("bye bye")
        if cliente in self.clientes:
            print("see ya")
            self.clientes.remove(cliente)
            del cliente
            
        self.update_client_positions()
    def update_client_positions(self):
        # Reposition remaining clientes
        i = 0
        for item in self.clientes:
            item.rect.x = self.x + i * self.padding + 10
            item.rect.y = self.y
            item.x = item.rect.x  # sincroniza para desenhar certinho
            item.y = item.rect.y
            i += 1
            
    def draw(self):
        for cliente in self.clientes:
            balao_surface = cliente.balao_image.copy()
            self.screen.blit(cliente.skin, pygame.Vector2(cliente.x,cliente.y))
            tempo_percorrido= pygame.time.get_ticks()/1000-(self.gc.level.time_init-cliente.tempo_entrada)
            if cliente.paciencia-tempo_percorrido< cliente.tempo_alerta:
                intensidade = int(255 * ((tempo_percorrido+cliente.tempo_alerta-cliente.paciencia) / cliente.tempo_alerta))
                intensidade = max(0, min(255, intensidade))
                overlay = pygame.Surface(balao_surface.get_size(), pygame.SRCALPHA)
                overlay.fill((255, 0, 0, intensidade),)
                balao_surface.blit(overlay, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            self.screen.blit(cliente.balao_image, pygame.Vector2(cliente.rect.topleft) + cliente.balao_offset)
            self.screen.blit(balao_surface, pygame.Vector2(cliente.rect.topleft) + cliente.balao_offset)
            # desenha o pedido por cima do balão (sempre por ultimo)
            self.screen.blit(cliente.pedido_image, pygame.Vector2(cliente.rect.topleft) + cliente.pedido_offset)
    def update(self, events):
        self.group.update(events)
    
    
    
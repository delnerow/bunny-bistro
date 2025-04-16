

pedidos={"Caponata":"assets\\images\\pratos\\caponata.png", "Hamburguer":"assets\\images\\pratos\\hamburguer.png","Quiche":"assets\\images\\pratos\\quiche.png"}

import pygame

# Objeto que contém duas cadeiras para um cliente sentar
class Mesa(pygame.sprite.Sprite):
    def __init__(self,x,y, filaMesa):
        super().__init__()
        self.image = pygame.image.load("assets\\images\\cozinha\\mesa.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 2)
        self.rect = self.image.get_rect(center=(x, y))
        self.x=x
        self.y=y
        self.filaMesa=filaMesa
        self.lugares=2
        self.cadeiras=[(x-110,y-70),(x+30,y-70)]
        self.cadeira1 = Cadeira(self.cadeiras[0],self.filaMesa,True)
        self.cadeira2 = Cadeira(self.cadeiras[1],self.filaMesa,False)
        
        
        self.filaMesa.disponiveis.append(self.cadeira1)
        self.filaMesa.disponiveis.append(self.cadeira2)
        # :image: imagem da mesa, carregada e escalada
        # :rect: retângulo da posição da mesa
        # :x: coordenada X da mesa
        # :y: coordenada Y da mesa
        # :filaMesa: fila de cadeiras disponíveis
        # :lugares: quantidade de assentos que a mesa possui
        # :cadeiras: lista com as posições das cadeiras ao redor da mesa
        # :cadeira1: primeira cadeira associada a essa mesa
        # :cadeira2: segunda cadeira associada a essa mesa
            
            
    
    def update(self,events):
        self.cadeira1.update(events)
        self.cadeira2.update(events)
    # Atualiza o estado das duas cadeiras associadas à mesa
    
    def print(self,screen):
        self.cadeira1.print(screen)
        self.cadeira2.print(screen)
    # Desenha os clientes e pedidos das cadeiras na tela
                
class Cadeira():
    def __init__(self, pos,filaMesa,esquerda):
        self.esquerda=esquerda
        self.pos = pos
        self.ocupante=[]
        self.refeicao = None
        self.refeicao_offset = pygame.Vector2(50, -30)
        self.tempo_comer=10
        self.filaMesa=filaMesa
        # :esquerda: se a cadeira fica à esquerda da mesa (booleano)
        # :pos: posição da cadeira (coordenadas X,Y)
        # :ocupante: lista de clientes sentados na cadeira (normalmente 0 ou 1)
        # :refeicao: tipo do pedido que o cliente dessa cadeira está comendo
        # :refeicao_offset: deslocamento visual para exibir o pedido acima do cliente
        # :tempo_comer: tempo fixo para o cliente terminar de comer
        # :filaMesa: referência para adicionar a cadeira de volta quando ficar livre
        
    def senta(self,cliente):
        if(self.esquerda):
            cliente.virar=True
        cliente.x=self.pos[0]
        cliente.y=self.pos[1]
        cliente.inicio_comer=pygame.time.get_ticks()
        self.ocupante.append(cliente)
        self.refeicao=cliente.pedido
    # Posiciona o cliente na cadeira e marca o horário de início da refeição
        
    def levanta(self):
        print(self.ocupante[0].especie+" levantouuu")
        self.ocupante[0].comido=True
        self.ocupante.pop()
        self.filaMesa.disponiveis.append(self)
        self.refeicao=None
    # Cliente termina de comer e libera a cadeira para uso
    
    def vazia(self):
        return len(self.ocupante)==0
    # Retorna True se a cadeira não tem ninguém sentado
    
    def update(self,events):
        if(not self.vazia()):
            tempo_percorrido = (pygame.time.get_ticks()- self.ocupante[0].inicio_comer)/1000
            self.ocupante[0].update(events)
            if tempo_percorrido>=self.tempo_comer:
                self.levanta()
    # Atualiza o cliente na cadeira, e verifica se ele já terminou de comer
            
    def print(self,screen):
        if(not self.vazia()):
            cliente = self.ocupante[0]
            pedido_image = pygame.image.load(pedidos[self.refeicao]).convert_alpha() 
            pedido_image = pygame.transform.scale_by(pedido_image, 1.5)
            dx= -25
            if(self.esquerda):
                dx= 60
            screen.blit(pedido_image, pygame.Vector2(cliente.x,cliente.y)+pygame.Vector2(dx,+20))
            screen.blit(cliente.skin, pygame.Vector2(cliente.x,cliente.y))
    # Desenha o cliente e o ícone do pedido acima dele


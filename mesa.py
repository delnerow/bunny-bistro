


import pygame


class Mesa(pygame.sprite.Sprite):
    def __init__(self,x,y, filaMesa):
        super().__init__()
        self.image = pygame.image.load("images\mesa.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 2)
        self.rect = self.image.get_rect(center=(x, y))
        self.x=x
        self.y=y
        self.filaMesa=filaMesa
        self.lugares=2
        self.cadeiras=[(x-110,y-70),(x+30,y-70)]
        self.cadeira1 = Cadeira(self.cadeiras[0],self.filaMesa,True)
        self.cadeira2 = Cadeira(self.cadeiras[1],self.filaMesa,False)
        
        self.talher=[(x-40,y),(x+40,y)]
        self.tempo_comer=100
        
        self.filaMesa.disponiveis.append(self.cadeira1)
        self.filaMesa.disponiveis.append(self.cadeira2)
        
            
            
    
    def update(self,events):
        self.cadeira1.update(events)
        self.cadeira2.update(events)
    def print(self,screen):
        self.cadeira1.print(screen)
        self.cadeira2.print(screen)

                
class Cadeira():
    def __init__(self, pos,filaMesa,esquerda):
        self.esquerda=esquerda
        self.pos = pos
        self.ocupante=[]
        self.tempo_comer=100
        self.filaMesa=filaMesa
    def senta(self,cliente):
        if(self.esquerda):
            cliente.virar=True
        cliente.x=self.pos[0]
        cliente.y=self.pos[1]
        cliente.inicio_comer=pygame.time.get_ticks()
        self.ocupante.append(cliente)
    def levanta(self):
        print(self.ocupante[0].especie+" levantouuu")
        self.ocupante[0].comido=True
        self.ocupante.pop()
        self.filaMesa.disponiveis.append(self)
    def vazia(self):
        return len(self.ocupante)==0
    def update(self,events):
        
        if(not self.vazia()):
            tempo_percorrido = (pygame.time.get_ticks()- self.ocupante[0].inicio_comer)/1000
            self.ocupante[0].update(events)
            if tempo_percorrido>=self.tempo_comer:
                self.levanta()
            
    def print(self,screen):
        if(not self.vazia()):
            cliente = self.ocupante[0]
            screen.blit(cliente.skin, pygame.Vector2(cliente.x,cliente.y))

        
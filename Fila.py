import pygame


class Fila():
    def __init__(self,gc,x,y):
        self.clientes =[]
        self.screen = gc.screen
        self.x=x
        self.y=y
        self.group = pygame.sprite.Group()
        self.padding =50
    def entra_cliente(self, cliente):
        self.clientes.append(cliente)
        self.group.add(cliente.sprite)
        i=0
        for item in self.clientes:
            item.sprite.rect.x= self.x +i*self.padding+10
            item.sprite.rect.y= self.y
            i=i+1
        
    def sai_cliente(self, cliente):
        if cliente in self.clientes:
            self.clientes.remove(cliente)
        i=0
        for item in self.clientes:
            item.sprite.rect.x= self.x +i*self.padding+10
            item.sprite.rect.y= self.y
            i=i+1
            
    def display(self):
        self.group.draw(self.screen)
    
    def update(self, events):
        self.group.update(events)
    
    
    
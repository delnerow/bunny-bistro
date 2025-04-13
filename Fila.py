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
            self.screen.blit(cliente.skin, pygame.Vector2(cliente.x,cliente.y))

    
    def update(self, events):
        self.group.update(events)
    
    
    
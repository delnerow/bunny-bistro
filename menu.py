import pygame

class Menu:
    def __init__(self, gc, items,x,y):
        self.screen = gc.screen
        self.x=x
        self.y=y
        self.items = items  #lista de itens do menu
        self.image = pygame.image.load("images/menu.png").convert_alpha()
        self.group = pygame.sprite.Group()
        padding =50
        i =0
        for item in self.items:
            item.sprite.rect.x= self.x +i*padding+10
            item.sprite.rect.y= self.y
            self.group.add(item.sprite)
            i=i+1
    def get_rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        self.group.draw(self.screen)
    
    def update(self, events):
        self.group.update(events)
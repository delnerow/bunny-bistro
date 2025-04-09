import pygame

class Menu:
    def __init__(self, gc, items):
        self.screen = gc.screen
        self.items = items  #lista de itens do menu
        self.image = pygame.image.load("images/menu.png").convert_alpha()
        self.group = pygame.sprite.Group()

        for item in self.items:
            self.group.add(item.sprite)


    def display(self, x, y):
        self.screen.blit(self.image, (x, y))
        self.group.draw(self.screen)
    
    def update(self, events):
        self.group.update(events)
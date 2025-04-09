import pygame


class PratoDisplay():
    def __init__(self, screen):
        self.screen = screen
        self.items = []  #lista de itens do menu
        self.image = pygame.image.load("images/menu.png").convert_alpha()
        self.group = pygame.sprite.Group()
        self.SLOT_SIZE = 64
        self.PADDING = 10
        self.START_X = 20
        self.START_Y = 50


    def update_ingrediente(self, ingredientes):
        self.items=ingredientes
        
    def display(self, x, y):
        self.screen.blit(self.image, (x, y))
        self.group.draw(self.screen)
        x = self.START_X
        for item in self.items:
            self.screen.blit(item.surface, (x, self.START_Y))
            x += self.SLOT_SIZE + self.PADDING
    
    def update(self, events):
        self.group.update(events)
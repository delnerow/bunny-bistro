import pygame

class Menu:
    def __init__(self, screen, items):
        self.screen = screen
        self.items = items  #lista de itens do menu
        self.image = pygame.image.load("images/menu.png").convert_alpha()
    
    def display(self, x, y):
        self.screen.blit(self.image, (x, y))
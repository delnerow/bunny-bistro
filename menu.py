import pygame

class Menu:
    def __init__(self, screen, items):
        self.screen = screen
        self.items = items
        self.image = pygame.image.load("images/menu.png").convert_alpha()
    
    def display(self):
        self.screen.blit(self.image, (0, 0))
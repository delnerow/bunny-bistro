

import pygame


class ColaUI():
    def __init__(self,x,y):
        self.image = pygame.image.load("images/colas.png").convert_alpha()  # carrega a imagem do balão
        self.image = pygame.transform.scale_by(self.image, 0.35)
        self.x=x
        self.y=y
    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))
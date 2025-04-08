import pygame
from ingrediente import Cebola, Tomate, Leite
from ClickSprite import ClickableSprite
from menu import Menu

class Armazem:
    def __init__(self, image, screen):
        self.sprite = ClickableSprite(image, 0, 0, self.abrir_menu)
        self.menu_image = pygame.image.load("images/menu.png").convert_alpha()
        self.menu_aberto = False
        self.menu = Menu(screen, [])
    def abrir_menu(self):
        print("erroerroo")


class Geladeira(Armazem):
    def __init__(self, gc):
        self.ingredientes = []
        self.image = pygame.image.load("images/geladeira.png").convert_alpha()
        super().__init__(self.image, gc)
    
    def abrir_menu(self):
        if(self.menu_aberto):
            self.menu_aberto = False
            return
        self.menu_aberto = True

    def menu_show(self):
        if self.menu_aberto:
            self.menu.display()

    def print(self):
        #o print da geladeira é feito diretamente no level.py
        self.menu_show()

import pygame
from ingrediente import Cebola, Tomate, Leite
from ClickSprite import ClickableSprite
from menu import Menu

class Armazem:
    def __init__(self, image, gc, x, y, ingredientes):
        self.sprite = ClickableSprite(image, x, y, self.abrir_menu)
        self.menu_image = pygame.image.load("images/menu.png").convert_alpha()
        self.menu_aberto = False
        self.menu = Menu(gc, ingredientes)

    def print(self):
        #o print da geladeira é feito diretamente no level.py
        self.menu_show()

    def menu_show(self):
        if self.menu_aberto:
            self.menu.display(0,0)

    def abrir_menu(self):
        if(self.menu_aberto):
            self.menu_aberto = False
            return
        self.menu_aberto = True
    
    def update(self, events):
        if self.menu_aberto:
            self.menu.update(events)


class Geladeira(Armazem):
    def __init__(self, gc, x, y):
        self.x_menu = 10
        self.y_menu = 50
        self.ingredientes = []
        self.image = pygame.image.load("images/geladeira.png").convert_alpha()
        
        self.ingredientes.append(Tomate(gc, self.x_menu + 100, self.y_menu))
        super().__init__(self.image, gc, x, y, self.ingredientes)
    
    def menu_show(self):
        if self.menu_aberto:
            self.menu.display(self.x_menu, self.y_menu)

class Despensa(Armazem):
    def __init__(self, gc, x, y):
        self.ingredientes = []
        self.image = pygame.image.load("images/despensa.png").convert_alpha()
        super().__init__(self.image, gc, x, y, self.ingredientes)

    def menu_show(self):
        if self.menu_aberto:
            self.menu.display(0,0)
import pygame
from ingrediente import Cebola, Tomate, Leite, Brocolis, Grao, Farinha
from ClickSprite import ClickableSprite
from menu import Menu

class Armazem:
    def __init__(self, image, gc, x, y, ingredientes):
        self.sprite = ClickableSprite(image, x, y, self.abrir_menu)
        self.menu_image = pygame.image.load("images/menu.png").convert_alpha()
        self.menu_aberto = False
        self.gc=gc
        self.x=x
        self.y=y
        self.menu = Menu(gc, ingredientes)
        self.position = 0

    def print(self):
        #o print da geladeira é feito diretamente no level.py
        self.menu_show()

    def menu_show(self):
        if self.menu_aberto:
            self.menu.display(0,0)

    def abrir_menu(self):
        self.gc.player.move(self.position)
        if(self.menu_aberto):
            self.menu_aberto = False
            return
        self.menu_aberto = True
    

            


class Geladeira(Armazem):
    def __init__(self, gc, x, y):
        self.x_menu = x+20
        self.y_menu = y-50
        self.ingredientes = []
        self.image = pygame.image.load("images/geladeira.png").convert_alpha()
        self.image= pygame.transform.scale(self.image, (64, 64*2))
        self.ingredientes.append(Tomate(gc, self.x_menu + 32, self.y_menu))
        self.ingredientes.append(Cebola(gc, self.x_menu + 32*2, self.y_menu))
        self.ingredientes.append(Leite(gc, self.x_menu + 32*3, self.y_menu))
        self.ingredientes.append(Brocolis(gc, self.x_menu + 32*4, self.y_menu))
        
        super().__init__(self.image, gc, x, y, self.ingredientes)
        self.position = 0
    
    def menu_show(self):
        if self.menu_aberto:
            self.menu.display(self.x_menu, self.y_menu)
   
    def update(self, events):
        if self.menu_aberto:
            self.menu.update(events)
        if self.gc.player.position != 0:
            self.menu_aberto = False 


class Despensa(Armazem):
    def __init__(self, gc, x, y):
        self.x_menu = x+20
        self.y_menu = y-50-32
        self.ingredientes = []
        self.image = pygame.image.load("images/despensa.png").convert_alpha()
        self.image= pygame.transform.scale(self.image, (64, 64))
        self.ingredientes.append(Farinha(gc, self.x_menu + 32, self.y_menu))
        self.ingredientes.append(Grao(gc, self.x_menu + 32*2, self.y_menu))
        
        super().__init__(self.image, gc, x, y, self.ingredientes)
        self.position = 1
    
    def menu_show(self):
        if self.menu_aberto:
            self.menu.display(self.x_menu, self.y_menu)

    def update(self, events):
        if self.menu_aberto:
            self.menu.update(events)
        if self.gc.player.position != 1:
            self.menu_aberto = False
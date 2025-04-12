import pygame
from HoverSprite import HoverSprite
from ingrediente import Cebola, Farinha, Grao, Tomate, Leite
from ClickSprite import ClickableSprite
from menu import Menu

class Armazem(HoverSprite):
    def __init__(self, image, gc, x, y, x_menu,y_menu,items):
        super().__init__(image, x, y,self.abre_ou_fecha,self.abre_ou_fecha)
        self.gc=gc
        self.x=x
        self.y=y
        #coordenadas do Armazem
        
        
        self.x_menu=x_menu
        self.y_menu=y_menu
        # coordenadas do menu gerado
        
        
        self.menu_aberto = False 
        self.menu_image = pygame.image.load("images/menu.png").convert_alpha()
        self.items = items
        # items que o menu deve mostrar
        
        
        self.menu = Menu(gc, self.items, self.x_menu,self.y_menu)
        #criado o menu
       

    def print(self):
        #o print da geladeira é feito diretamente no level.py
        if self.menu_aberto:
            self.menu.display()


    def update(self, events):
        super().update(events)  # <-- This brings back hover detection!
        if self.menu_aberto:
            self.menu.update(events)
    
    def abre_ou_fecha(self):
        print("abre ou fecha")
        self.gc.player.move(self.x,self.y+10,1)
        if(self.menu_aberto):
            self.menu_aberto = False
            return
        self.menu_aberto = True
    

    def is_mouse_over(self, mouse_pos):
        # Override to include both sprite and its menu in hover area
        return self.rect.collidepoint(mouse_pos) or (self.menu_aberto and self.menu.get_rect().collidepoint(mouse_pos))

            


class Geladeira(Armazem):
    def __init__(self, gc, x, y):
        self.x_menu = x+10
        self.y_menu = y-50
        self.image = pygame.image.load("images/geladeira.png").convert_alpha()
        self.image= pygame.transform.scale(self.image, (64, 128))
        self.items=[Tomate(gc, 0, 0),Cebola(gc,0, 0),Leite(gc, 0 , 0)]
        
        super().__init__(self.image, gc, x, y,self.x_menu,self.y_menu,self.items)
    

class Despensa(Armazem):
    def __init__(self, gc, x, y):
        self.x_menu = x+20
        self.y_menu = y-50
        image = pygame.image.load("images/despensa.png").convert_alpha()
        self.items=[Grao(gc, 0, 0),Farinha(gc, 0, 0)]

        super().__init__(image, gc, x, y,self.x_menu,self.y_menu,self.items)
    
import pygame
from src.sprites.HoverSprite import HoverSprite
from src.entities.ingrediente import Brocolis, Cebola, Farinha, Grao, Tomate, Leite
from src.ui.menu import Menu


# Objeto que armazena ingredientes dentro de si e mostra um menu do seu interior
class Armazem(HoverSprite):
    def __init__(self, image, gc, x, y, x_menu,y_menu,items,position):
        self.gc = gc
        self.x = x
        self.y = y
        self.position = position
        self.sound = pygame.mixer.Sound("assets\\sounds\\menu.mp3")
        super().__init__(image, self.x, self.y,self.abre_ou_fecha,self.abre_ou_fecha)
        # :gc:              GameController para acessar prato e score 
        # :x:               Posição x do armazem 
        # :y:               Posição y do armazem
        # :sound:           Som do armazem abrindo
        
        
        self.x_menu = x_menu
        self.y_menu = y_menu
        self.menu_aberto = False 
        self.menu_image = pygame.image.load("assets\\images\\cozinha\\menu.png").convert_alpha()
        self.items = items
        self.menu = Menu(gc, self.items, self.x_menu,self.y_menu)
        
        # :x:               Posição x do menu gerado
        # :y:               Posição y do menu gerado
        # :menu_aberto:     Se o menu está visível
        # :items:           Itens contidos no menu
        # :menu:            Objeto Menu contido no armazem
       

    def print(self):
        if self.menu_aberto:
            self.menu.display()
    # Desenha o menu caso esteja visível

    def update(self, events):
        super().update(events) 
        if self.menu_aberto:
            self.menu.update(events)
    # Atualiza eventos para o Menu, se ele estiver visível 
    # com base no HoverSprite
    
    def abre_ou_fecha(self):
        self.gc.player.is_on_armazem = not self.gc.player.is_on_armazem
        self.sound.play()
        self.gc.player.move(self.position)
        if(self.menu_aberto):
            self.menu_aberto = False
            return
        self.menu_aberto = True
    # Lógica para sprite do player virar em direção ao armazem
    # Som do menu abrindo/fechando e player se movendo
    # Se estava invisível, esta visível e vice-versa

    def is_mouse_over(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos) or (self.menu_aberto and self.menu.get_rect().collidepoint(mouse_pos))
    # Complemento do método HoverSprite, pois a área do menu também é considerada
            
class Geladeira(Armazem):
    def __init__(self, gc, x, y):
        self.x_menu = x+10
        self.y_menu = y-50
        self.position=0
        self.image = pygame.image.load("assets\\images\\cozinha\\geladeiras\\geladeira_nivel1.png").convert_alpha()
        self.image= pygame.transform.scale(self.image, (64, 64*2))
        self.items=[Tomate(gc, 0, 0),Cebola(gc,0, 0),Leite(gc, 0 , 0), Brocolis(gc, 0, 0)]
        super().__init__(self.image, gc, x, y,self.x_menu,self.y_menu,self.items, self.position)

class Despensa(Armazem):
    def __init__(self, gc, x, y):
        self.x_menu = x+20
        self.y_menu = y-50
        self.position =1
        self.image = pygame.image.load("assets\\images\\cozinha\\despensa.png").convert_alpha()
        self.image= pygame.transform.scale(self.image, (35, 35))
        self.items=[Grao(gc, 0, 0),Farinha(gc, 0, 0)]
        super().__init__(self.image, gc, x, y,self.x_menu,self.y_menu,self.items,self.position)
    
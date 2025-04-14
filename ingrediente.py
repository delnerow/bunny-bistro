
from copy import deepcopy
import pygame
from ClickSprite import ClickableSprite


class Ingrediente:
    def __init__(self, nome, indiceReceita,gc1, image,x,y):
        self.nome=nome
        self.indiceReceita = indiceReceita
        self.gc = gc1
        self.x=x
        self.y=y
        self.estadoReceita=[]
        self.sprite = ClickableSprite(image,self.x,self.y,self.alertarEscolha)
        self.sound = pygame.mixer.Sound("sounds\\vup.mp3")
    #
    # Um nome para identificar o ingrediente
    # o índice no código carteado de receita
    # bools indicando o estado culinário do ingrediente
    #
    # DISCLAIMER: talvez um ingrediente sprite n seja o mesmo que um ingrediente no prato
    #
    def cortar(self):
        self.__cortado= True
        if self.estadoReceita.count(1) == 0:
            self.estadoReceita.append(1)
    #
    # corta o ingrediente
    #
    
    def bater(self):
        self.__batido= True
        if self.estadoReceita.count(2) == 0:
            self.estadoReceita.append(2)
    #
    # bate o ingrediente
    #
    def assar(self):
        self.__assado= True
        if self.estadoReceita.count(3) == 0:
            self.estadoReceita.append(3)
    #
    # assa o ingrediente
    #
    def restaurar(self):
        self.estadoReceita = []
    #
    # restaura o ingrediente
    #
    
    def alertarEscolha(self):
        print("beep beep")
        #self.gc.level.player.prato.add_ingrediente(self.__clonar__())
        if(self.gc.player.prato != None):
            self.sound.play()
            self.gc.player.prato.add_ingrediente(self)
        
    #
    # um ingrediente clicado informa o GameController dessa escolha
    # altera um parâmetro do gameController (ou será melhor uma função só para isso?)
    
    def __clonar__(self, memo):
        # just create a new instance 
        raise NotImplementedError("Subclasses must implement this method")

    
    def estadoNumerico(self):
        
        return tuple(self.estadoReceita)
    #
    # definindo qual o estado culinário do ingrediente
    # transformando lista de algarismos num número
    #
class Tomate(Ingrediente):
    def __init__(self,gc,x,y):
        self.image=pygame.image.load('images\\food\Vegetables\Tomato.png').convert_alpha();
        self.image = pygame.transform.scale_by(self.image, 3)
        super().__init__("Tomate", 0,gc,self.image,x,y)  
    #
    # carrega imagem do sprite
    # define nome e índice na lei da receita
    #
    
    def __clonar__(self): 
        return Tomate(self.gc,0,0) 
    #
    # cria nova instância de Tomate
    #

class Cebola(Ingrediente):
    def __init__(self,gc,x,y):
        self.image=pygame.image.load('images\\food\Vegetables\Onion.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 3)
        super().__init__("Cebola", 1,gc,self.image,x,y)  
    #
    # carrega imagem do sprite
    # define nome e índice na lei da receita
    #
     
    def __clonar__(self):
        return Cebola(self.gc,0,0)  
    #
    # cria nova instância de Ceebola
    #

class Grao(Ingrediente):
    def __init__(self,gc, x, y):
        self.image=pygame.image.load('images\\food\Vegetables\potato.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 3)
        super().__init__("Grão de Bico", 2, gc, self.image, x, y) 
        
class Farinha(Ingrediente):
    def __init__(self,gc, x, y):
        self.image=pygame.image.load('images\\food\Sweets\Sugar.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 3)
        super().__init__("Farinha", 3, gc, self.image, x, y) 
        
class Leite(Ingrediente):
    def __init__(self,gc, x, y):
        self.image=pygame.image.load('images\\food\EggsandDairy\Milk1.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 3)
        super().__init__("Leite Vegetal", 4,gc,self.image,x,y)  
        
class Brocolis(Ingrediente):
    def __init__(self,gc, x, y):
        self.image=pygame.image.load('images\\food\Vegetables\Broccoli.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 3)
        super().__init__("Brócolis", 5, gc, self.image, x, y) 
        
        
       
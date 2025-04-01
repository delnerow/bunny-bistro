
from copy import deepcopy
import pygame
from ClickSprite import ClickableSprite


class Ingrediente:
    def __init__(self, nome, indiceReceita,gc, image,x,y):
        self.nome=nome
        self.indiceReceita = indiceReceita
        self.estadoReceita=[]
        self.__cortado=False
        self.__batido=False
        self.__assado=False
        self.gc=gc
        self.sprite = ClickableSprite(image,x,y,self.alertarEscolha)
    #
    # Um nome para identificar o ingrediente
    # o índice no código carteado de receita
    # bools indicando o estado culinário do ingrediente
    #
    def cortar(self):
        self.__cortado= True
        self.estadoReceita.append(1)
    #
    # corta o ingrediente
    #
    
    def bater(self):
        self.__batido= True
        self.estadoReceita.append(2)
    #
    # bate o ingrediente
    #
    def assar(self):
        self.__assado= True
        self.estadoReceita.append(3)
    #
    # assa o ingrediente
    #
    
    def alertarEscolha(self):
        print("beep beep")
        self.gc.holderPrato.add_ingrediente(self.__clonar__())
        self.gc.printarPrato()
        
    #
    # um ingrediente clicado informa o GameController dessa escolha
    #
    
    def __clonar__(self, memo):
        # just create a new instance 
        raise NotImplementedError("Subclasses must implement this method")

    
    def estadoNumerico(self):
        estado=0
        for i in range(len(self.estadoReceita)):
            estado = estado +pow(10,len(self.estadoReceita)-i-1)*self.estadoReceita[i]
        return estado
    #
    # definindo qual o estado culinário do ingrediente
    # 
    #
class Tomate(Ingrediente):
    def __init__(self,gc,x,y):
        self.image=pygame.image.load('images/tomate.png').convert_alpha();
        super().__init__("Tomate", 0,gc,self.image,x,y)  
    def __clonar__(self):
        # just create a new instance 
        return Tomate(self.gc,0,0) 
 
class Cebola(Ingrediente):
    def __init__(self,gc,x,y):
        self.image=pygame.image.load('images/cebola.png').convert_alpha();
        super().__init__("Cebola", 1,gc,self.image,x,y)   
    def __clonar__(self):
        # just create a new instance 
        return Cebola(self.gc,0,0)  

class Grao(Ingrediente):
    def __init__(self):
        super().__init__("Grão de Bico", 2) 
        
class Farinha(Ingrediente):
    def __init__(self):
        super().__init__("Farinha", 3) 
        
class Leite(Ingrediente):
    def __init__(self):
        super().__init__("Leite Vegetal", 4)    
        
class Brocolis(Ingrediente):
    def __init__(self):
        super().__init__("Brócolis", 5) 
        
        
       

import pygame
from src.sprites.ClickSprite import ClickableSprite

# Ingredientes, que combinados e preparados num certa ordem geram um prato de comida
class Ingrediente(ClickableSprite):
    def __init__(self, indice_Receita,gc1, image,x,y):
        self.indice_Receita = indice_Receita
        self.estado_Receita=[]
        self.x=x
        self.y=y
        self.gc = gc1
        self.sound = pygame.mixer.Sound("assets\\sounds\\vup.mp3")
        self.sound2 = pygame.mixer.Sound("assets\\sounds\\menu.mp3")
        self.sound2.set_volume(0.3)
        super().__init__(image,self.x,self.y,self.alertar_Escolha)  
        # :indice_Receita:  Cada ingrediente tem um índice no código de receita
        # :estado_Receita:  Lista com a ordem dos preparos
        # :x:               Posição x da imagem do ingrediente 
        # :y:               Posição y da imagem do ingrediente
        # :gc:              GameController para acessar prato e score 
        # :sound:           Som de ingrediente inserio no prato 
        # :sound2:          Som de erro, quando o prato está cheio/sem prato
        
    def cortar(self):
        if self.estado_Receita.count(1) == 0:
            self.estado_Receita.append(1)
    # Preparo de cortar
    
    def bater(self):
        if self.estado_Receita.count(2) == 0:
            self.estado_Receita.append(2)
    # Preparo de bater
    
    def assar(self):
        if self.estado_Receita.count(3) == 0:
            self.estado_Receita.append(3)
    # Preparo de assar
    
    def alertar_Escolha(self):
        if(self.gc.player.prato != None):
            self.gc.player.prato.add_ingrediente(self.__clonar__())
            if(len(self.gc.player.prato.ingredientes)<=5):
                self.sound.play()
            else:
                self.sound2.play()
    # Se há um prato clonar o ingrediente clicado para o prato
    # Se foi possível adicionar, tocar som de sucesso 
    # caso contrário som de erro
    
    def __clonar__(self):
        raise NotImplementedError("Subclasse sobrescreve esse método")
    # Cria uma nova instancia do objeto, a depender da subclasse
    
    def estado_Numerico(self):
        return tuple(self.estado_Receita)
    # Definindo qual o estado e ordem de preparo do ingrediente

class Tomate(Ingrediente):
    def __init__(self,gc,x,y):
        self.image=pygame.image.load('assets\\images\\pratos\\ingredientes\\tomate.png').convert_alpha();
        self.image = pygame.transform.scale_by(self.image, 3)
        super().__init__(0,gc,self.image,x,y)  
    # Carrega imagem do sprite e dimensiona
    # Define índice do ingrediente na lei da receita
    
    def __clonar__(self): 
        return Tomate(self.gc,0,0) 
    # Cria nova instância de Tomate

class Cebola(Ingrediente):
    def __init__(self,gc,x,y):
        self.image=pygame.image.load('assets\\images\\pratos\\ingredientes\\cebola.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 3)
        super().__init__(1,gc,self.image,x,y)  
    # Carrega imagem do sprite e dimensiona
    # Define índice do ingrediente na lei da receita
     
    def __clonar__(self):
        return Cebola(self.gc,0,0)  
    # Cria nova instância de Cebola

class Grao(Ingrediente):
    def __init__(self,gc, x, y):
        self.image=pygame.image.load('assets\\images\\pratos\\ingredientes\\batata.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 3)
        super().__init__(2, gc, self.image, x, y) 
    # Carrega imagem do sprite e dimensiona
    # Define índice do ingrediente na lei da receita
    
    def __clonar__(self):
        return Grao(self.gc,0,0) 
    # Cria nova instância de Grão de Bico
        
class Farinha(Ingrediente):
    def __init__(self,gc, x, y):
        self.image=pygame.image.load('assets\\images\\pratos\\ingredientes\\acucar.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 3)
        super().__init__(3, gc, self.image, x, y) 
    # Carrega imagem do sprite e dimensiona
    # Define índice do ingrediente na lei da receita
    
    def __clonar__(self):
        return Farinha(self.gc,0,0) 
    # Cria nova instância de Farinha
        
class Leite(Ingrediente):
    def __init__(self,gc, x, y):
        self.image=pygame.image.load('assets\\images\\pratos\\ingredientes\\leite.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 3)
        super().__init__(4,gc,self.image,x,y)  
    # Carrega imagem do sprite e dimensiona
    # Define índice do ingrediente na lei da receita
    
    def __clonar__(self):
        return Leite(self.gc,0,0) 
    # Cria nova instância de leite Vegetal
        
class Brocolis(Ingrediente):
    def __init__(self,gc, x, y):
        self.image=pygame.image.load('assets\\images\\pratos\\ingredientes\\brocolis.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 3)
        super().__init__( 5, gc, self.image, x, y) 
    # Carrega imagem do sprite e dimensiona
    # Define índice do ingrediente na lei da receita
    
    def __clonar__(self):
        return Brocolis(self.gc,0,0) 
    # Cria nova instância de Brocolis
        
        
       
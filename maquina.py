from prato import Prato
from ClickSprite import ClickableSprite
import pygame
class Maquina:
    def __init__(self,gc,image,x,y):
        self.prato_atual= Prato()
        self.__ocupada=False
        self.gc=gc
        self.x=x
        self.y=y
        self.sprite = ClickableSprite(image,x,y,self.ocupar)
        self.position = 0
        
    #
    # inicializa uma máqina (superclasse)
    # e desocupada
    # 
    
    def ocupar(self):
        bandeja = self.gc.player.prato
        self.gc.player.move(self.position)
        print("ocupar")
        if(bandeja != None and not self.__ocupada):
            if not bandeja.esta_vazio():
                self.prato_atual.ingredientes= bandeja.ingredientes
                bandeja.limpar_comida()
                self.__ocupada= True
                self.__operar()
            else:
                print("Erro: nada na bandeja")
        else:
            print("Erro: máquina ocupada")
        
    #
    # esvazia ingredientes da bandeja
    # ocupa a máquina
    # começa a operar
    #
    
    def __operar(self):
        if(not self.prato_atual.esta_vazio()):
            #lançar minigame
            success = True
            if success:
                self.cozinhar()
            else:
                print("Erro: falhou no minigame")   
                
    # Iniciaria minigame para ver se irá realmente cozinhar
    # e começa a cozinhar
    #
    
    def cozinhar(self):
        
        raise NotImplementedError("Subclasses must implement this method")
    # 
    # Cada subclasse tem o seu próprio
    # dependendo da maquina da cozinha
    #
    
    def free(self):
        bandeja=self.gc.player.prato
        if bandeja != None and bandeja.ingredientes==[] and not self.prato_atual.esta_vazio():
            bandeja.ingredientes=self.prato_atual.ingredientes
            self.prato_atual.limpar_comida()
            self.__ocupada=False
            self.gc.printarPrato()
        else:
            print("Erro: bandeja cheia/maquina já vazia")
    #
    # retorna ingredientes à bandeja
    # e se desocupa
    #
class Tabua(Maquina):
    def __init__(self,gc,x,y):
        self.image=pygame.image.load('images/tabua.png').convert_alpha();
        self.image= pygame.transform.scale(self.image, (64, 32))
        super().__init__(gc,self.image,x,y)
        self.position = 4
        self.sound = pygame.mixer.Sound('sounds/cortar.mp3')
    
    def cozinhar(self):
        self.sound.play()
        print("cozinhar")
        for i in range(len(self.prato_atual.ingredientes)):
            self.prato_atual.ingredientes[i].cortar()
        self.free()
    #
    # tabua de corte
    # ela corta
    #
               
class Batedeira(Maquina):
    def __init__(self,gc,x,y):
        self.image=pygame.image.load('images/batedeira.png').convert_alpha();
        self.image= pygame.transform.scale(self.image, (64, 64))
        super().__init__(gc,self.image,x,y)
        self.position = 3
        self.sound = pygame.mixer.Sound('sounds/bater.mp3')
    def cozinhar(self):
        self.sound.play()
        for i in range(len(self.prato_atual.ingredientes)):
            self.prato_atual.ingredientes[i].bater()
        self.free()
    #
    # batedeira
    # ela bate
    #
class Forno(Maquina):
    def __init__(self,gc,x,y):
        self.image=pygame.image.load('images/forno.png').convert_alpha()
        self.image= pygame.transform.scale(self.image, (64, 64))
        super().__init__(gc,self.image,x,y)
        self.position = 2
        self.sound = pygame.mixer.Sound('sounds/forno.mp3')
    def cozinhar(self):
        self.sound.play()
        for i in range(len(self.prato_atual.ingredientes)):
            self.prato_atual.ingredientes[i].assar()
        self.free()
    #
    # forno
    # ele assa
    #
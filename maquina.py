from prato import Prato
from ClickSprite import ClickableSprite
import pygame

# Classe base para todas as máquinas de cozinha
class Maquina(ClickableSprite):
    def __init__(self,gc,image,x,y):
        self.prato_atual= Prato()
        self.__ocupada=False
        self.gc=gc
        self.x=x
        self.y=y
        self.position = 0
        super().__init__(image,x,y,self.ocupar)
        # :prato_atual:     Prato que está sendo preparado na máquina
        # :ocupada:         Flag de controle para saber se a máquina está em uso
        # :gc:              GameController, para acessar o contexto geral do jogo 
        # :x:               Posição X da máquina no jogoe
        # :y:               Posição Y da máquina no jogo 
        # :position:        ID de posição no layout do jogo
    
    def ocupar(self):
        bandeja = self.gc.player.prato
        self.gc.player.move(self.position)
        self.gc.player.machine_using()
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
    # Se o prato do jogador não estiver vazio e a máquina estiver livre,
    # transfere ingredientes da bandeja para a máquina e inicia o processamento.
    
    def __operar(self):
        if(not self.prato_atual.esta_vazio()):
            success = True
            if success:
                self.cozinhar()
            else:
                print("Erro: falhou no minigame")   
                
    # Se os ingredientes estiverem prontos, chama o método cozinhar.
    # Substituível por minigame real no futuro.
    
    def cozinhar(self):
        
        raise NotImplementedError("Subclasse sobresscreve esse método")
    # Método abstrato para definir o que a máquina fará com os ingredientes.
    # Cada subclasse (ex: Forno, Tabua) deve implementar sua versão específica.
    
    def desocupar(self):
        bandeja=self.gc.player.prato
        if bandeja != None and bandeja.ingredientes==[] and not self.prato_atual.esta_vazio():
            bandeja.ingredientes=self.prato_atual.ingredientes
            self.prato_atual.limpar_comida()
            self.__ocupada=False
            #self.gc.printarPrato()
        else:
            print("Erro: bandeja cheia/maquina já vazia")
        # Transfere os ingredientes processados da máquina de volta para a bandeja
        # e libera a máquina.
 
class Tabua(Maquina):
    def __init__(self,gc,x,y):
        self.image=pygame.image.load('images\\cozinha\\tabua.png').convert_alpha();
        self.image= pygame.transform.scale(self.image, (50, 50))
        super().__init__(gc,self.image,x,y)
        self.position = 4
        self.sound = pygame.mixer.Sound('sounds\\cortar.mp3')
    
    def cozinhar(self):
        self.sound.play()
        for i in range(len(self.prato_atual.ingredientes)):
            self.prato_atual.ingredientes[i].cortar()
        self.desocupar()
    # Ao processar, todos os ingredientes serão cortados.
               
class Batedeira(Maquina):
    def __init__(self,gc,x,y):
        self.image=pygame.image.load('images\\cozinha\\batedeira.png').convert_alpha();
        self.image= pygame.transform.scale(self.image, (40, 40))
        super().__init__(gc,self.image,x,y)
        self.position = 3
        self.sound = pygame.mixer.Sound('sounds\\bater.mp3')
        
    def cozinhar(self):
        self.sound.play()
        for i in range(len(self.prato_atual.ingredientes)):
            self.prato_atual.ingredientes[i].bater()
        self.desocupar()
    # Ao processar, todos os ingredientes serão batidos.
    
class Forno(Maquina):
    def __init__(self,gc,x,y):
        self.image=pygame.image.load('images\\cozinha\\fogoes\\fogao_nivel1.png').convert_alpha()
        self.image= pygame.transform.scale(self.image, (64, 64))
        super().__init__(gc,self.image,x,y)
        self.position = 2
        self.sound = pygame.mixer.Sound('sounds\\forno.mp3')
    def cozinhar(self):
        self.sound.play()
        for i in range(len(self.prato_atual.ingredientes)):
            self.prato_atual.ingredientes[i].assar()
        self.desocupar()
    # Ao processar, todos os ingredientes serão assados.
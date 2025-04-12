especies=("humano","cao","gato")
import pygame
from ClickSprite import ClickableSprite
from prato import Prato


def get_image(sheet, width, height, scale, colour, position):
	#retira uma fração de uma imagem maior para utilizar
	#como sprite, usado para elementos pequenos na tela
	
	image = pygame.Surface((width, height)).convert_alpha()
	image.blit(sheet, (0, 0), (width*position[0], height*position[1],width*(position[0]+1), height*(position[1]+1)))
	image = pygame.transform.scale(image, (width*scale, height*scale))
	image.set_colorkey(colour)
	return image

class Cliente(ClickableSprite):
    def __init__(self,gc,x,y,paciencia, pedido, especie):
        self.paciencia = paciencia
        self.pedido = pedido
        self.especie = especie
        self.x=x
        self.y=y
        self.gc=gc
        self.image = pygame.image.load("images\cliente.png").convert_alpha()
        self.skinVector = [get_image(self.image, 14, 32, 3, (0,0,0), (i, 0)) for i in range(2)]
        self.skin = self.skinVector[0]

        #frame do coelho: alterna entre imagens na mesma 
        # direção pra ele ter movimento mesmo parado :D 
        self.frame = 0
        
        self.__score=0
        super().__init__(self.image, x, y,self.comer)
    #
    # inicializa um cliente com tempo de paciencia
    # pedido desejado, especie do cliente
    # score do pedido
    # e sabendo qual o gameController
    
    def comer(self):
        print("nham nham")
        prato = self.gc.player.prato
        if(prato):
            if(self.pedido == prato.validar_receita()):
                self.__score=100
                print("que gostoso")
            else:
                self.__score=0
                print("que bosta")
            prato.ingredientes = []
            self.gc.level.score= self.gc.level.score+self.satisfacao()
    #
    # interacao do cliente com oq tem no prato
    # se for oq pediu, brasil
    #  os ingredientes são consumidos no processo
    #
    
    def satisfacao(self):
        return self.__score
    
    #
    # retornar qualidade do prato
    #
    def update(self, events):
        #atualiza a posição do coelho na tela
        #a cada 10 frames, muda a imagem do coelho
        #para dar a impressão de movimento
        super().update(events)
        self.frame += 1             
        if self.frame == 40:
            self.skin = self.skinVector[1]
        elif self.frame == 80:
            self.skin = self.skinVector[0]
            self.frame = 0
        #self.image = self.skin 
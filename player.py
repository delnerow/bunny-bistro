#código do jogador como movimento, interação com o ambiente e ações
#além das imagens
import pygame
from pygame.math import Vector2
from prato import *

def get_image(sheet, width, height, scale, colour, position):
	#retira uma fração de uma imagem maior para utilizar
	#como sprite, usado para elementos pequenos na tela
	
	image = pygame.Surface((width, height)).convert_alpha()
	image.blit(sheet, (0, 0), (width*position[0], height*position[1],width*(position[0]+1), height*(position[1]+1)))
	image = pygame.transform.scale(image, (width*scale, height*scale))
	image.set_colorkey(colour)
	return image


class Player:
    def __init__(self):
        self.screenposition = Vector2(200,200) #posição na tela, para print

        #posição do coelho na cozinha (em que máquina ele está)
        self.position = 0 
        
        self.sheet = pygame.image.load("images\coelinho.png").convert_alpha()

        #cria o vetor de sprites do coelho (a gente não deve usar todas...)
        self.skinVector = [get_image(self.sheet, 48,48, 3, (0,0,0), (int(x / 4), x % 4)) for x in range(16)]
        self.skin = self.skinVector[0]

        #frame do coelho: alterna entre imagens na mesma 
        # direção pra ele ter movimento mesmo parado :D 
        self.frame = 0

        #inicia o prato do coelho como vazio
        self.prato = Prato

    def update(self):
        #atualiza a posição do coelho na tela
        #a cada 10 frames, muda a imagem do coelho
        #para dar a impressão de movimento
        self.frame += 1
        if self.frame == 40:
            self.skin = self.skinVector[4]
        elif self.frame == 80:
            self.skin = self.skinVector[0]
            self.frame = 0

    def move(self, newPosition):
        #muda a posição do coelho na tela com base na posição
        #da máquina em que ele está (depende da arte)

        #geladeira
        if newPosition == 0:
            self.screenposition = Vector2(200, 200)
            self.skin = self.skinVector[0]

        #fogão
        elif newPosition == 1:
            self.screenposition = Vector2(200, 300)
            self.skin = self.skinVector[1]

        #tábua
        elif newPosition == 2:
            self.screenposition = Vector2(200, 400)
            self.skin = self.skinVector[2]

        #bancada
        elif newPosition == 3:
            self.screenposition = Vector2(200, 500)
            self.skin = self.skinVector[3]
    
        def printOi():
            print("oi")
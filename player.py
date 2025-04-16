
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

# Jogador com movimento, interação com o ambiente e ações além das imagens
class Player:
    def __init__(self):
        # Posição na tela, para print
        self.screenposition = Vector2(64*3,64*3) 

        # Posição do coelho na cozinha (em que máquina ele está)
        self.position = 0 
        self.is_on_armazem = False
        self.using_machine_timer = 0
        
        self.sheet = pygame.image.load("images\\coelinho.png").convert_alpha()

        # Cria o vetor de sprites do coelho (a gente não deve usar todas...)
        self.skinVector = [get_image(self.sheet, 48,48, 3, (0,0,0), (int(x / 4), x % 4)) for x in range(16)]
        self.skin = self.skinVector[0]

        # Frame do coelho: alterna entre imagens na mesma 
        # Direção pra ele ter movimento mesmo parado :D 
        self.frame = 0
        # coelho está com a arma
        self.mira = False 

        # Inicia o prato do coelho como NONE!!!
        self.prato = None

        # Lista de posições fixas na cozinha para cada estação
        self.movVec = []
        
        #declara as posições do player na cozinha
        pos_geladeira = Vector2(64*2.5, 64*1.5) #0
        pos_armario = Vector2(64*8.5, 64*1.5)   #1
        pos_fogao = Vector2(64*7.5, 64*1.5)     #2
        pos_batedeira = Vector2(64*5.65,64*1.5) #3
        pos_tabua = Vector2(64*13.50, 64*1.5)         #4
        pos_prato = Vector2(64*4, 64*3)         #5
        pos_lixo = Vector2(32*0.3, 64*2.7)        #6
        
        self.movVec.extend([pos_geladeira, pos_armario, pos_fogao, pos_batedeira, pos_tabua, pos_prato, pos_lixo])

        self.prepGunSound = pygame.mixer.Sound("sounds\\gunPrepare.mp3")
        self.shootSound = pygame.mixer.Sound("sounds\\gunShoot.mp3")

    def update(self):
        #atualiza a posição do coelho na tela
        #a cada 10 frames, muda a imagem do coelho
        #para dar a impressão de movimento
        self.frame += 1

        #verifica se olha pra cima
        if self.is_on_armazem:
            self.skin = self.skinVector[1+4*(self.frame//40)]
            if self.frame > 78:
                self.frame = 0

        #verifica se está usando máquina
        elif self.using_machine_timer > 0:
            k=1
            if self.position==4:
                k=0
            
            self.skin = self.skinVector[k+4*(self.frame//40)]
            self.using_machine_timer -= 1
            if self.frame > 78:
                self.frame = 0

        #verifica se está no lixo
        elif self.position == 6:
            self.skin = self.skinVector[2+4*(self.frame//40)]
            if self.frame > 78:
                self.frame = 0

        #posição padrão do coelho
        else:
            self.skin = self.skinVector[8*self.mira+4*(self.frame//40)]
            if self.frame > 78:
                self.frame = 0

    def move(self, position):
        #muda a posição do coelho na tela com base na posição
        #da máquina em que ele está (depende da arte)
        # acho q da pra generalizar
        self.screenposition = self.movVec[position]
        self.position = position

    def machine_using(self):
        self.using_machine_timer = 30
    # Coelho olha por pouco tempo na maquina quando usa
    
    def mirar(self):
        self.mira = not self.mira
    # Alterna o estado de mira do coelho

    def engatilhar(self):
        self.prepGunSound.play()
    # Prepara a arma para atirar
    
    def shoot(self):
        self.shootSound.play()

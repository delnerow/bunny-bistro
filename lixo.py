from prato import Prato
from ClickSprite import ClickableSprite
import pygame


# Objeto destruidor de pratos que sairam errado
class Lixo(ClickableSprite):
    def __init__(self,gc,x,y):
        self.gc = gc
        self.image=pygame.image.load('images\\cozinha\\lixo.png').convert_alpha()
        self.image= pygame.transform.scale(self.image, (40, 40))
        self.sound = pygame.mixer.Sound('sounds\\lixo.mp3')
        super().__init__(self.image,x,y,self.descartar)  
        # :indice_Receita:  Cada ingrediente tem um índice no código de receita
        # :estado_Receita:  Lista com a ordem dos preparos
        # :x:               Posição x da imagem do ingrediente 
        # :y:               Posição y da imagem do ingrediente
        # :gc:              GameController para acessar prato e score 
        # :sound:           Som de ingrediente inserio no prato 
        # :sound2:          Som de erro, quando o prato está cheio/sem prato
    
    def descartar(self):
        self.gc.player.move(6)
        bandeja = self.gc.player.prato
        if (bandeja == None):
            return
        if not bandeja.esta_vazio():
            bandeja.limpar_comida()
            self.sound.play()
        else:
            print("Erro: nada na bandeja")
        # Faz o player mover até a maquina, 
        # se existir um prato limpa a comida e toca som
    
    
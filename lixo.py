from prato import Prato
from ClickSprite import ClickableSprite
import pygame

class Lixo:
    def __init__(self,gc,x,y):
        self.gc = gc
        self.image=pygame.image.load('images/lixo.png').convert_alpha()
        self.image= pygame.transform.scale(self.image, (150, 150))
        self.sprite = ClickableSprite(self.image, x, y, self.descartar)
    
    def descartar(self):
        bandeja = self.gc.player.prato
        print("descartar")
        if not bandeja.esta_vazio():
            bandeja.restaurar_prato()
            bandeja.limpar_comida()
            self.gc.printarPrato()
        else:
            print("Erro: nada na bandeja")
    #
    # lixo
    # ele lixea
    #

import pygame
from ClickSprite import ClickableSprite
from prato import Prato


class Bancada():
    def __init__(self,gc,x,y):
        self.gc=gc
        self.x=x
        self.y=y
        self.image = self.image=pygame.image.load('images/despensa.png').convert_alpha();
        #self.image= pygame.transform.scale(self.image, (64, 64))
        self.sprite = ClickableSprite(self.image,x,y,self.dar_novo_prato)
    def dar_novo_prato(self):
        self.gc.player.move(self.x,self.y+10,1)
        if(self.gc.player.prato is None):
            self.gc.player.prato = Prato()
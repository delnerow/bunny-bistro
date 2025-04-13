
import pygame
from ClickSprite import ClickableSprite
from prato import Prato


class Bancada():
    def __init__(self,gc,x,y):
        self.gc=gc
        self.x=x
        self.y=y
        self.image = self.image=pygame.image.load('images/pratos.png').convert_alpha();
        self.image = pygame.transform.scale_by(self.image, 1.5)
        #self.image= pygame.transform.scale(self.image, (64, 64))
        self.sprite = ClickableSprite(self.image,x,y,self.dar_novo_prato)
        self.position = 5
    def dar_novo_prato(self):
        self.gc.player.move(self.position)
        if(self.gc.player.prato is None):
            self.gc.player.prato = Prato()
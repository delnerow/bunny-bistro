
import pygame
from ClickSprite import ClickableSprite
from prato import Prato

# Objeto que gera pratos as mãos vazias do player
class Bancada(ClickableSprite):
    def __init__(self,gc,x,y):
        self.gc=gc
        self.image = self.image=pygame.image.load('images/pratos.png').convert_alpha();
        self.image = pygame.transform.scale_by(self.image, 1.5)
        super().__init__(self.image,x,y,self.dar_novo_prato)
        self.position = 5
        # :gc:              GameController para acessar prato e score 
        # :x:               Posição x da bancada 
        # :y:               Posição y da bancada
        # :imagem:          Carrega e dimensiona imagem
        # :sound:           Som do armazem abrindo
        
    def dar_novo_prato(self):
        self.gc.player.move(self.position)
        if(self.gc.player.prato is None):
            self.gc.player.prato = Prato()
    # Player se move até bancada
    # Se não existir prato, cria prato
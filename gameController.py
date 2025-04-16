from prato import Prato
from level import Level
from player import Player
import pygame

class GameController:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        icon = pygame.image.load("images/icon.bmp")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Bunny-Bistro")
        self.screen = pygame.display.set_mode((16*64, 9*64))

        self.time=0
        self.player = Player()
        self.level = Level(self, self.screen, self.player)

    #
    def printarPrato(self):
        print("=====Prato atual=====")
        for c in self.player.prato.ingredientes:
            print(c.nome+""+str(c.estadoNumerico())+"", end='')
            print("")
        print(" = ", self.player.prato.validar_receita())
    #
    # atualiza o prato nas mãos do Chef
    #

    def run(self):
        self.level.run()

    def printOI(self):
        print("oi\n")
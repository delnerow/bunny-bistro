from prato import Prato
from level import Level
from player import Player
import pygame
from telaInicial import TelaInicial
class GameController:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        icon = pygame.image.load("images\\icon.bmp")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Bunny-Bistro")
        self.screen = pygame.display.set_mode((16*64, 9*64))

        self.time=0
        self.player = Player()
        self.level = Level(self)
        self.start=TelaInicial(self)

        self.state = "menu"  # <- Começa pelo menu
        self.clock = pygame.time.Clock()

        

    def run(self):
        escolha = self.start.run()
        if escolha == "jogar":
            self.level.run()

    def printOI(self):
        print("oi\n")
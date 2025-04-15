from prato import Prato
from level import Level
from player import Player
import pygame


# Estrutura intermediária de varios eventos e objetos globais, além das fases
class GameController:
    def __init__(self):
        # Inicio do jogo e mixer de som
        pygame.init()
        pygame.mixer.init()
        
        # Setup do icone/thumbnail do jogo
        icon = pygame.image.load("images\icon.bmp")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Bunny-Bistro")
        
        # Tamanho/resolucao da tela
        self.screen = pygame.display.set_mode((16*64, 9*64))

        # Inicialização do tempo, jogador e Level
        self.time=0
        self.player = Player()
        self.level = Level(self)

    # Roda o nível atual
    def run(self):
        self.level.run()


import pygame, sys
from player import Player
from ui import UI
import maquina
from armazem import Geladeira, Despensa

class Level:
    def __init__(self, gc):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("tituloo")
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("images\cozinha_demo.png").convert_alpha()

        #controle de jogo
        self.gc = gc
        self.ui = UI() 

        #o nosso player
        self.player = Player()

        #as máquinas da cozinha
        self.tabua = maquina.Tabua(gc, 64*3.5,64*5)
        self.batedeira = maquina.Batedeira(gc, 200, 80)
        self.forno = maquina.Forno(gc, 476, 155)

        self.maquinasGroup = pygame.sprite.Group()
        self.maquinasGroup.add(self.tabua.sprite)
        self.maquinasGroup.add(self.batedeira.sprite)
        self.maquinasGroup.add(self.forno.sprite)

        #despensa
        self.geladeira = Geladeira(self.screen, 1, 1)
        self.despensa = Despensa(self.screen, 10, 100)

        self.armazemGroup = pygame.sprite.Group()
        self.armazemGroup.add(self.geladeira.sprite)
        self.armazemGroup.add(self.despensa.sprite)

    def run(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            #atualização
            self.update(events)

            #impressão na tela
            self.print()

    def update(self, events):
        # Atualiza a lógica do jogo aqui
        self.player.update()
        self.maquinasGroup.update(events)
        self.armazemGroup.update(events)

    def print(self):
        # Desenha o fundo
        self.screen.blit(self.background, (0, 0))

        #imprime as máquinas na tela
        self.maquinasGroup.draw(self.screen)
        self.armazemGroup.draw(self.screen)

        #imprime o coelho na tela
        self.screen.blit(self.player.skin, self.player.screenposition)

        #imprime a interface
        self.geladeira.print()
        self.despensa.print()

        # Atualiza a tela
        pygame.display.flip()
        self.clock.tick(60)
import pygame, sys
from bancada import Bancada
from player import Player
from pratoDIsplay import PratoDisplay
from ui import UI
import maquina
from armazem import Geladeira, Despensa
from lixo import Lixo

class Level:
    def __init__(self, gc, screen, player):
        pygame.display.set_caption("tituloo")
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("images\cozinha_demo.png").convert_alpha()
        self.background = pygame.transform.scale2x(self.background)
        self.screen = screen

        #controle de jogo
        self.gc = gc
        self.ui = UI() 
        
        self.pratoDisplay = PratoDisplay(self.screen)

        #o nosso player
        self.player = player

        #as máquinas da cozinha
        self.tabua = maquina.Tabua(gc, 64*3.5,64*5)
        self.batedeira = maquina.Batedeira(gc, 620, 80)
        self.forno = maquina.Forno(gc, 476, 155)
        
        # bancada de pratos
        self.bancada = Bancada(gc,64*5,64*5)

        self.maquinasGroup = pygame.sprite.Group()
        self.maquinasGroup.add(self.tabua.sprite)
        self.maquinasGroup.add(self.batedeira.sprite)
        self.maquinasGroup.add(self.forno.sprite)
        self.maquinasGroup.add(self.bancada.sprite)

        #despensa
        self.geladeira = Geladeira(self.gc, 125, 70)
        self.despensa = Despensa(self.gc, 10, 100)

        self.armazemGroup = pygame.sprite.Group()
        self.armazemGroup.add(self.geladeira.sprite)
        self.armazemGroup.add(self.despensa.sprite)

        #lixo
        self.lixo = Lixo(gc, 10, 500)
        self.lixoGroup = pygame.sprite.Group()
        self.lixoGroup.add(self.lixo.sprite)

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
        self.lixoGroup.update(events)
        self.pratoDisplay.update_ingrediente(self.player.prato)
        self.geladeira.update(events)
        self.despensa.update(events)

    def print(self):
        # Desenha o fundo
        self.screen.blit(self.background, (0, 0))

        #imprime as máquinas na tela
        self.maquinasGroup.draw(self.screen)
        self.armazemGroup.draw(self.screen)
        self.lixoGroup.draw(self.screen)

        #imprime o coelho na tela
        self.screen.blit(self.player.skin, self.player.screenposition)

        #imprime a interface
        self.geladeira.print()
        self.despensa.print()
        self.pratoDisplay.display(700,430)

        # Atualiza a tela
        pygame.display.flip()
        self.clock.tick(60)
    
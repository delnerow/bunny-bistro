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

        # Timer do jogo (em segundos)
        self.time_remaining = 300  # Exemplo: 5 minutos
        self.last_time = pygame.time.get_ticks()
        self.timer_font = pygame.font.Font("images\DigitalDismay.otf", 36) 
        
        self.pratoDisplay = PratoDisplay(self.screen)

        #o nosso player
        self.player = player

        #as máquinas da cozinha
        self.tabua = maquina.Tabua(gc, 64*3.5,64*4.5)
        self.batedeira = maquina.Batedeira(gc, 620, 80)
        self.forno = maquina.Forno(gc, 64*8, 64*1.5)
        
        # bancada de pratos
        self.bancada = Bancada(gc,64*5,64*4.5)

        self.maquinasGroup = pygame.sprite.Group()
        self.maquinasGroup.add(self.tabua.sprite)
        self.maquinasGroup.add(self.batedeira.sprite)
        self.maquinasGroup.add(self.forno.sprite)
        self.maquinasGroup.add(self.bancada.sprite)

        #despensa
        self.geladeira = Geladeira(self.gc, 64*2, 64)
        self.despensa = Despensa(self.gc, 64*4, 64*1.5)

        self.armazemGroup = pygame.sprite.Group()
        self.armazemGroup.add(self.geladeira)
        self.armazemGroup.add(self.despensa)

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
        #self.armazemGroup.update(events)
        self.lixoGroup.update(events)
        self.pratoDisplay.update_ingrediente(self.player.prato)
        self.geladeira.update(events)
        self.despensa.update(events)

        #atualiza o timer
        current_time = pygame.time.get_ticks()
        if current_time - self.last_time >= 1000:  # 1000 ms = 1 segundo
            self.time_remaining -= 1
            self.last_time = current_time

        # Verifica se o tempo acabou
        if self.time_remaining <= 0:
            print("Fim do jogo! O tempo acabou!")
            pygame.quit()
            sys.exit()

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

        # Exibe o timer na tela
        timer_text = self.timer_font.render(f"Tempo: {self.time_remaining}", True, (255, 255, 255))  # Texto branco
        self.screen.blit(timer_text, (10, 10))  # Posição no canto superior esquerdo

        # Atualiza a tela
        pygame.display.flip()
        self.clock.tick(60)
    
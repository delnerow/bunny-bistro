import pygame, sys
from Fila import Fila
from bancada import Bancada
from cliente import Cliente
from player import Player
from pratoDIsplay import PratoDisplay
from ui import UI
import maquina
from armazem import Geladeira, Despensa
from lixo import Lixo

class Level:
    def __init__(self, gc, screen, player):
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("images\cozinha_demo.png").convert_alpha()
        self.background = pygame.transform.scale2x(self.background)
        self.screen = screen

        #controle de jogo
        self.gc = gc
        self.ui = UI() 
        self.score = 0

        # Timer do jogo (em segundos)
        self.time_init = 100
        self.time_remaining = self.time_init
        self.last_time = pygame.time.get_ticks()
        self.font = pygame.font.Font("images\DigitalDismay.otf", 36) 
        
        self.pratoDisplay = PratoDisplay(self.screen)

        #o nosso player
        self.player = player
        self.fila = Fila(gc,64*7,64*4.5 )
        
        # clientes
        self.cliente = Cliente(gc,64*7,64*4.5, 100, "Caponata","cao",self.fila)
        self.cliente2 = Cliente(gc,64*10,64*4.5, 100, "Hamburguer","cao",self.fila)
        self.cliente3 = Cliente(gc,64*10,64*4.5, 100, "Quiche","cao",self.fila)

        self.fila.entra_cliente(self.cliente)
        self.fila.entra_cliente(self.cliente2)
        self.fila.entra_cliente(self.cliente3)

        #as máquinas da cozinha
        self.tabua = maquina.Tabua(gc, 64*3.5,64*4.5)
        self.batedeira = maquina.Batedeira(gc, 348, 80)
        self.forno = maquina.Forno(gc, 64*8, 64*1.5)
        
        # bancada de pratos
        self.bancada = Bancada(gc,64*5,64*4.2)

        self.maquinasGroup = pygame.sprite.Group()
        self.bancadaGroup= pygame.sprite.Group()
        self.maquinasGroup.add(self.tabua.sprite)
        self.maquinasGroup.add(self.batedeira.sprite)
        self.maquinasGroup.add(self.forno.sprite)
        self.bancadaGroup.add(self.bancada.sprite)


        #despensa
        self.geladeira = Geladeira(self.gc, 64*2, 64)
        self.despensa = Despensa(self.gc, 64*9, 64*1.5)

        self.armazemGroup = pygame.sprite.Group()
        self.armazemGroup.add(self.geladeira)
        self.armazemGroup.add(self.despensa)

        #lixo
        self.lixo = Lixo(gc, 10, 500)
        self.lixoGroup = pygame.sprite.Group()
        self.lixoGroup.add(self.lixo.sprite)

        #musica
        self.volume = 0.2
        self.music = pygame.mixer.Sound('sounds/music.mp3')

        pygame.mixer.music.set_volume(self.volume)   
        pygame.mixer.music.load('sounds/music.mp3')

        self.musicNow = 0

    def run(self):
        # Inicia a música de fundo
        pygame.mixer.music.play(-1)  # -1 para tocar em loop
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
        self.fila.update(events)
        self.maquinasGroup.update(events)
        self.bancadaGroup.update(events)
        #self.armazemGroup.update(events)
        self.lixoGroup.update(events)
        self.pratoDisplay.update_ingrediente(self.player.prato)
        self.geladeira.update(events)
        self.despensa.update(events)
        self.update_music()
        self.update_timer()

    def print(self):
        # Desenha o fundo
        self.screen.blit(self.background, (0, 0))

        # Exibe o timer na tela
        timer_text = self.font.render(f"Tempo: {self.time_remaining}", True, (255, 255, 255))  # Texto branco
        self.screen.blit(timer_text, (10, 10))  # Posição no canto superior esquerdo

        # Exibe a pontuação na tela
        score_text = self.font.render(f"Pontuacao: {self.score}", True, (255, 255, 255))  # Texto branco
        self.screen.blit(score_text, (10, 50))  # Posição no canto superior esquerdo, abaixo do timer
        
        #imprime as máquinas na tela
        self.maquinasGroup.draw(self.screen)
        self.armazemGroup.draw(self.screen)
        self.lixoGroup.draw(self.screen)

        #imprime o coelho na tela
        self.screen.blit(self.player.skin, self.player.screenposition)
        self.fila.draw()
        #imprime a interface
        self.geladeira.print()
        self.despensa.print()
        self.pratoDisplay.display(700,430)
        self.bancadaGroup.draw(self.screen)
        # Atualiza a tela
        pygame.display.flip()
        self.clock.tick(60)
    
    def update_music(self):
        if self.time_remaining <= self.time_init/2 and self.musicNow == 0:
            self.musicNow = 1
            pygame.mixer.music.fadeout(100)  # Fadeout da música atual (1 segundo)
            pygame.mixer.music.load('sounds/music_fast.mp3')  # Carrega a nova música
            pygame.mixer.music.play(-1, fade_ms=100)  # Toca a nova música com fadein (1 segundo)


        if self.time_remaining <= self.time_init/4 and self.musicNow == 1:
            self.musicNow = 2
            pygame.mixer.music.fadeout(100)  # Fadeout da música atual (1 segundo)
            pygame.mixer.music.load('sounds/music_muitofast.mp3')  # Carrega a nova música
            pygame.mixer.music.play(-1, fade_ms=100)  # Toca a nova música com fadein (1 segundo)
    
    def update_timer(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_time >= 1000:  # 1000 ms = 1 segundo
            self.time_remaining -= 1
            self.last_time = current_time

        # Verifica se o tempo acabou
        if self.time_remaining <= 0:
            #faz algo quando o tempo acaba!!
            pass

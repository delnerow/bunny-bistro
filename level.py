import pygame, sys
from ClienteSpawner import ClienteSpawner
from fila import Fila
from filaMesa import FilaMesa
from mesa import Mesa
from bancada import Bancada
from cliente import Cliente
from colaReceitas import ColaUI
from player import Player
from pratoDIsplay import PratoDisplay
from ui import UI
import maquina
from armazem import Geladeira, Despensa
from lixo import Lixo
from window import Window

class Level:
    def __init__(self, gc, screen, player):
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("images\cozinha1.png").convert_alpha()
        self.background = pygame.transform.scale2x(self.background)
        self.screen = screen

        #controle de jogo
        self.gc = gc
        self.ui = UI() 
        self.score = 400
        self.max_score = 1000

        # Configuração da barra de pontuação
        self.score_bar_width = 300  # Largura máxima da barra
        self.score_bar_height = 30  # Altura da barra
        self.score_bar_x = 10       # Posição X da barra
        self.score_bar_y = 16       # Posição Y da barra
        self.score_bar_color = (0, 75, 35)  # Cor da barra (verde)
        self.max_score = 1000  # Pontuação máxima para encher a barra
        self.gradient_colors = [
        (0, 75, 35),    # Vermelho
        (0, 100, 0),  # Laranja
        (0, 114, 0),  # Amarelo
        (56, 176, 0),    # Verde
        (112, 224, 0),    # Azul
        (158, 240, 26)   # Roxo
        ]    

        self.cola = ColaUI(750,280)
        self.janela = Window(730,5)
        # Timer do jogo (em segundos)
        self.time_init = 100
        self.time_remaining = self.time_init
        self.last_time = pygame.time.get_ticks()
        self.font = pygame.font.Font("images\DigitalDismay.otf", 36) 
        self.font_point = pygame.font.Font(None, 22) 
        
        self.pratoDisplay = PratoDisplay(self.screen)

        # mesas
        

        #o nosso player
        self.player = player
        self.filaMesa=FilaMesa()
        self.mesa1= Mesa(360,490, self.filaMesa)
        self.mesa2= Mesa(100,490, self.filaMesa)
        self.fila = Fila(gc,64*7,64*4.5, self.filaMesa )
        
        # clientes
        self.cliente = Cliente(gc,64*7,64*4.5, 20, "Caponata","bode",self.fila)
        self.clienteControl = ClienteSpawner(self.gc,self.fila,0.2)
        self.fila.entra_cliente(self.cliente)

        #as máquinas da cozinha
        self.tabua = maquina.Tabua(gc, 64*3.5,64*4.4)
        self.batedeira = maquina.Batedeira(gc, 348, 80)
        self.forno = maquina.Forno(gc, 64*8, 64*1.5)
        
        
        
        
        self.mesasGroup = pygame.sprite.Group()
        self.maquinasGroup = pygame.sprite.Group()
        self.bancadaGroup= pygame.sprite.Group()
        self.maquinasGroup.add(self.tabua.sprite)
        self.maquinasGroup.add(self.batedeira.sprite)
        self.maquinasGroup.add(self.forno.sprite)
        self.mesasGroup.add(self.mesa1)
        self.mesasGroup.add(self.mesa2)
        
        # bancada de pratos
        self.bancada = Bancada(gc,64*6,64*4.2)
        self.bancadaGroup.add(self.bancada.sprite)
        
        #despensa
        self.geladeira = Geladeira(self.gc, 64*3, 64)
        self.despensa = Despensa(self.gc, 64*9, 64*1.5)

        self.armazemGroup = pygame.sprite.Group()
        self.armazemGroup.add(self.geladeira)
        self.armazemGroup.add(self.despensa)

        #lixo
        self.lixo = Lixo(gc, 10, 36*7)
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
        self.mesasGroup.update(events)
        self.janela.update()
        self.player.update()
        self.fila.update(events)
        self.maquinasGroup.update(events)
        self.bancadaGroup.update(events)
        #self.armazemGroup.update(events)
        self.lixoGroup.update(events)
        self.pratoDisplay.update_ingrediente(self.player.prato)
        self.geladeira.update(events)
        self.despensa.update(events)
        self.clienteControl.update()
        self.update_music()
        self.update_timer()
        
        

    def print(self):
        # Desenha o fundo
        self.screen.blit(self.background, (0, 0))
        self.janela.print(self.screen)
        
        self.mesasGroup.draw(self.screen)
        for mesa in self.mesasGroup:
            mesa.print(self.screen)
        # Exibe o timer na tela
        timer_text = self.font.render(f"{self.time_remaining}", True, (255, 255, 255))  # Texto branco
        self.screen.blit(timer_text, (64*7.5+16, 14))  # Posição no mostrador

        # Exibe a pontuação na tela
        self.print_pointbar()
        score_text = self.font_point.render(f"EcoPoints: {self.score}", True, (255, 255, 255))  # Texto branco
        self.screen.blit(score_text, (18, 22))  # Posição no canto superior esquerdo, abaixo do timer
        
        #imprime as máquinas na tela
        self.maquinasGroup.draw(self.screen)
        
        self.armazemGroup.draw(self.screen)
        self.lixoGroup.draw(self.screen)
        
        
        

        #imprime o coelho na tela
        self.screen.blit(self.player.skin, self.player.screenposition)
        self.fila.draw()

        #imprime a interface
        self.janela.print(self.screen)
        self.geladeira.print()
        self.despensa.print()
        self.pratoDisplay.display(700,450)
        self.bancadaGroup.draw(self.screen)
        self.cola.display(self.screen)
        
        
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

    def print_pointbar(self):
        # Preenche o retângulo com a cor de fundo
        pygame.draw.rect(self.screen, (200, 200, 200), 
                (self.score_bar_x, self.score_bar_y, self.score_bar_width, self.score_bar_height))
        
        score_percentage = min(self.score / self.max_score, 1)  # Calcula a porcentagem (máximo de 100%)
        current_width = int(self.score_bar_width * score_percentage)  # Largura atual da barra

        # Número de seções para o gradiente
        num_sections = len(self.gradient_colors) - 1
        section_width = self.score_bar_width // num_sections

        for i in range(num_sections):
            # Cor inicial e final para a seção
            start_color = self.gradient_colors[i]
            end_color = self.gradient_colors[i + 1]

            # Número de sub-seções dentro de cada seção
            sub_sections = section_width
            for j in range(sub_sections):
                # Interpola a cor entre start_color e end_color
                t = j / sub_sections
                red = int(start_color[0] + t * (end_color[0] - start_color[0]))
                green = int(start_color[1] + t * (end_color[1] - start_color[1]))
                blue = int(start_color[2] + t * (end_color[2] - start_color[2]))
                color = (red, green, blue)

                # Calcula a posição da sub-seção
                section_x = self.score_bar_x + i * section_width + j
                if section_x < self.score_bar_x + current_width:
                    pygame.draw.rect(self.screen, color, 
                                    (section_x, self.score_bar_y, 1, self.score_bar_height))


        # Desenha o contorno da barra
        pygame.draw.rect(self.screen, (233, 216, 166), 
                (self.score_bar_x, self.score_bar_y, self.score_bar_width, self.score_bar_height), 4)
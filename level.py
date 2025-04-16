import pygame, sys
from ClienteSpawner import ClienteSpawner
from fila import Fila
from filaMesa import FilaMesa
from introAnimation import IntroAnimation
from mesa import Mesa
from bancada import Bancada
from cliente import Cliente
from colaReceitas import ColaUI
from pratoDIsplay import PratoDisplay
from ui import UI
import maquina
from armazem import Geladeira, Despensa
from lixo import Lixo
from window import Window
from barata import Barata

class Level:
    def __init__(self, gc):
        #controle de jogo
        self.gc = gc


    def reset(self):
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("images\\cozinha\\cozinha_nivel1.png").convert_alpha()
        self.background = pygame.transform.scale2x(self.background)
        # controle de jogo
        self.ui = UI()
        self.score = 400
        self.max_score = 1000
        self.fim_de_jogo = False
        self.transicao_ativa = False
        self.transicao_alpha = 0

        self.intro = IntroAnimation(self.gc.screen)

        # Configuração da barra de pontuação
        self.shake_duration = 0  # Duração do shake em loops
        self.score_bar_width = 300  # Largura máxima da barra
        self.score_bar_height = 30  # Altura da barra
        self.score_bar_x = 10  # Posição X da barra
        self.score_bar_y = 16  # Posição Y da barra
        self.score_bar_color = (0, 75, 35)  # Cor da barra (verde)
        self.max_score = 1000  # Pontuação máxima para encher a barra
        self.gradient_colors = [
            (0, 75, 35),  # Vermelho
            (0, 100, 0),  # Laranja
            (0, 114, 0),  # Amarelo
            (56, 176, 0),  # Verde
            (112, 224, 0),  # Azul
            (158, 240, 26)  # Roxo
        ]

        self.cola = ColaUI(750, 280)
        self.janela = Window(730, 5)

        # Timer do jogo (em segundos)
        self.time_init = 100
        self.time_remaining = self.time_init
        self.last_time = pygame.time.get_ticks()
        self.font = pygame.font.Font("images\\DigitalDismay.otf", 36)
        self.font_point = pygame.font.Font(None, 22)

        self.pratoDisplay = PratoDisplay(self.gc.screen)

        # mesas

        self.filaMesa = FilaMesa()
        self.mesa1 = Mesa(360, 490, self.filaMesa)
        self.mesa2 = Mesa(100, 490, self.filaMesa)
        self.mesa3 = Mesa(220, 420, self.filaMesa)
        self.fila = Fila(self.gc, 64 * 7, 64 * 4.5, self.filaMesa)

        # as baratas
        self.barata = Barata(self.gc)

        # clientes
        self.cliente = Cliente(self.gc, 64 * 7, 64 * 4.5, 20, "Caponata", "bode", self.fila)
        self.clienteControl = ClienteSpawner(self.gc, self.fila, 0.2)
        self.fila.entra_cliente(self.cliente)

        # as máquinas da cozinha
        self.tabua = maquina.Tabua(self.gc, 64 * 3.5, 64 * 4.4)
        self.batedeira = maquina.Batedeira(self.gc, 348, 80)
        self.forno = maquina.Forno(self.gc, 64 * 8, 64 * 1.5)

        self.mesasGroup = pygame.sprite.Group()
        self.maquinasGroup = pygame.sprite.Group()
        self.bancadaGroup = pygame.sprite.Group()
        self.maquinasGroup.add(self.tabua)
        self.maquinasGroup.add(self.batedeira)
        self.maquinasGroup.add(self.forno)
        self.mesasGroup.add(self.mesa3)
        self.mesasGroup.add(self.mesa1)
        self.mesasGroup.add(self.mesa2)

        # bancada de pratos
        self.bancada = Bancada(self.gc, 64 * 6, 64 * 4.2)
        self.bancadaGroup.add(self.bancada)

        # despensa
        self.geladeira = Geladeira(self.gc, 64 * 3, 64)
        self.despensa = Despensa(self.gc, 64 * 9, 64 * 1.5)

        self.armazemGroup = pygame.sprite.Group()
        self.armazemGroup.add(self.geladeira)
        self.armazemGroup.add(self.despensa)

        # lixo
        self.lixo = Lixo(self.gc, 0, 227)
        self.lixoGroup = pygame.sprite.Group()
        self.lixoGroup.add(self.lixo)

        # musica
        pygame.mixer.music.stop()
        self.volume = 0.2
        self.music = pygame.mixer.Sound('sounds\\music.mp3')

        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.load('sounds\\music.mp3')

        self.musicNow = 0

    def run(self):
        self.reset()
        # Inicia a música de fundo
        pygame.mixer.music.play(-1)  # -1 para tocar em loop
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if not self.intro.transition_done:
                # Enquanto a intro não terminou: congelar o jogo
                self.intro.update()
                self.intro.draw()
            else:
                #atualização
                if self.time_remaining>0 and not self.fim_de_jogo:
                    self.update(events)

                #impressão na tela
                self.print()
                
                # Quando o tempo acabar e a transição ainda não tiver sido ativada
                if self.time_remaining <= 0 and not self.transicao_ativa:
                    self.transicao_ativa = True  # Inicia a transição de escurecimento

                if self.transicao_ativa:
                    # Cria a superfície preta semi-transparente
                    fade_surface = pygame.Surface(self.gc.screen.get_size()).convert_alpha()
                    fade_surface.fill((0, 0, 0, self.transicao_alpha))  # RGBA, com controle de opacidade

                    if self.transicao_alpha < 255:
                        self.transicao_alpha += 5  # Aumenta a opacidade lentamente
                    else:
                        self.fim_de_jogo = True  # Marca o fim definitivo do jogo
                        return self.score

                    # Aplica a camada preta em cima da tela
                    self.gc.screen.blit(fade_surface, (0, 0))



                    # Redesenha o player por cima da máscara, para que o player fique iluminado
                    self.gc.screen.blit(self.gc.player.skin, self.gc.player.screenposition)

            # Atualiza a tela e o FPS
            pygame.display.flip()
            self.clock.tick(60)

    def update(self, events):
        # Atualiza a lógica do jogo aqui
        self.mesasGroup.update(events)
        self.janela.update()
        self.gc.player.update()
        self.fila.update(events)
        self.maquinasGroup.update(events)
        self.bancadaGroup.update(events)
        self.lixoGroup.update(events)
        self.pratoDisplay.update_ingrediente(self.gc.player.prato)
        self.geladeira.update(events)
        self.despensa.update(events)
        self.clienteControl.update()
        self.update_music()
        self.update_timer()
        self.barata.update(events)

    def print(self):
        # Desenha o fundo
        self.gc.screen.blit(self.background, (0, 0))
        self.janela.print(self.gc.screen)
        
        
        self.mesasGroup.draw(self.gc.screen)
        for mesa in self.mesasGroup:
            mesa.print(self.gc.screen)
        # Exibe o timer na tela
        timer_text = self.font.render(f"{self.time_remaining}", True, (255, 255, 255))  # Texto branco
        self.gc.screen.blit(timer_text, (64*7.5+16, 14))  # Posição no mostrador

        # Exibe a pontuação na tela
        self.print_pointbar()
        score_text = self.font_point.render(f"EcoPoints: {self.score}", True, (255, 255, 255))  # Texto branco
        self.gc.screen.blit(score_text, (18, 22))  # Posição no canto superior esquerdo, abaixo do timer
        
        #imprime as máquinas na tela
        self.maquinasGroup.draw(self.gc.screen)
        self.armazemGroup.draw(self.gc.screen)
        self.lixoGroup.draw(self.gc.screen)
        
        
        #imprime a barata na tela
        if self.barata.live:
            self.gc.screen.blit(self.barata.image, (self.barata.x,self.barata.y))

        #imprime o coelho na tela
        self.gc.screen.blit(self.gc.player.skin, self.gc.player.screenposition)
        self.fila.draw()

        #imprime a interface
        self.geladeira.print()
        self.despensa.print()
        self.pratoDisplay.display(700,450)
        self.bancadaGroup.draw(self.gc.screen)
        self.cola.display(self.gc.screen)

        
        # Atualiza a tela
        #pygame.display.flip()
        #self.clock.tick(60)
    
    def update_music(self):
        if self.time_remaining <= self.time_init/2 and self.musicNow == 0:
            self.musicNow = 1
            pygame.mixer.music.fadeout(100)  # Fadeout da música atual (1 segundo)
            pygame.mixer.music.load('sounds\\music_fast.mp3')  # Carrega a nova música
            pygame.mixer.music.play(-1, fade_ms=100)  # Toca a nova música com fadein (1 segundo)


        if self.time_remaining <= self.time_init/4 and self.musicNow == 1:
            self.musicNow = 2
            pygame.mixer.music.fadeout(100)  # Fadeout da música atual (1 segundo)
            pygame.mixer.music.load('sounds\\music_muitofast.mp3')  # Carrega a nova música
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
        pygame.draw.rect(self.gc.screen, (200, 200, 200), 
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
                    pygame.draw.rect(self.gc.screen, color, 
                                    (section_x, self.score_bar_y, 1, self.score_bar_height))
        
        # Desenha o contorno da barra
        if self.shake_duration > 0:
            if self.shake_duration//4 % 2 == 0:
                color = (255, 0, 0)
            else:
                color = (255, 255, 255)
            pygame.draw.rect(self.gc.screen, color, 
                (self.score_bar_x, self.score_bar_y, self.score_bar_width, self.score_bar_height), 4)
            self.shake_duration -= 1

        elif self.shake_duration < 0:
            if self.shake_duration//4 % 2 == 0:
                color = (0, 255, 0)
            else:
                color = (255, 255, 255)
            pygame.draw.rect(self.gc.screen, color, 
                (self.score_bar_x, self.score_bar_y, self.score_bar_width, self.score_bar_height), 4)
            self.shake_duration += 1
        
        else:
            pygame.draw.rect(self.gc.screen, (233, 216, 166), 
                    (self.score_bar_x, self.score_bar_y, self.score_bar_width, self.score_bar_height), 4)
        
    def change_score(self, score):
        self.score += score
        if self.score < 0:
            self.score = 0
        if score <= 0:
            self.shake_duration = 50
        else:
            self.shake_duration = -50
        
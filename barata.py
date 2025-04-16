import pygame
import numpy as np
from HoverSprite import HoverSprite

class Barata(HoverSprite):
    def __init__(self, gc):
        self.image = pygame.image.load("images\\barata.png").convert_alpha()
        self.image= pygame.transform.scale(self.image, (32, 32))
        self.screen = gc.screen
        self.x0 = 100
        self.y0 = 300
        self.x = self.x0
        self.y = self.y0
        super().__init__(self.image, self.x, self.y, self.mirar, self.mirar)
        self.gc = gc

        #timer para descontar pontuação
        self.timer = 0
        self.timer_limit = 600  # 10 segundos (60 FPS * 10)
        self.spawn_time = 0
        self.spawn_limit = 60*5

        self.live = False  # Define se a barata está viva
        self.spawn_chance = 0.5  # Chance de respawn da barata (0.01%)
        
        #movimento da baratinha
        self.t = 0
        self.f1 = 2.3
        self.f2 = 4
        self.sound = pygame.mixer.Sound("sounds\\barataviva.mp3")

    def mirar(self):
        print("muda a mira")
        mirando = not self.gc.player.mira
        self.gc.player.mira = mirando

        if mirando:
            self.gc.player.engatilhar()

    def update(self, events):
        if self.live:
            super().update(events)  # <-- This brings back hover detection!
            #movimento da barata
            self.t += 1/60  # Atualiza o tempo (60 FPS)
            self.x = self.x0 + 20*np.cos(self.f1*self.t) + 10*np.cos(self.f2*self.t)
            self.y = self.y0 + 20*np.sin(self.f1*self.t) + 10*np.sin(self.f2*self.t)

            self.rect.x = self.x
            self.rect.y = self.y

            self.timer += 1  # Incrementa o timer a cada frame
            if self.timer >= self.timer_limit:
                # Se o tempo limite for atingido, reseta o timer e muda a posição da barata
                self.timer = 0
                self.gc.level.change_score(-10)  # Desconta 1 ponto

            #verifica se está com a arma
            if self.hovering:
                # Verifica se o mouse foi clicado
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # Se a mira estiver na barata, chama o método de atirar
                        self.gc.player.shoot()
                        self.live = False
                        self.sound.stop()  # Para o som da barata
                        self.changePlace()        
                        self.gc.player.mira = False
                        self.hovering = False  # Reseta o estado de hover após clicar
        else:
            # Se a barata não está viva, verifica o tempo de respawn
            self.spawn_time += 1
            if self.spawn_time >= self.spawn_limit:
                if np.random.random() < self.spawn_chance:  # 0.01% chance
                    self.live = True
                    self.sound.play(-1)  # Reproduz o som da barata em loop
                    self.timer = 0  # Reseta o timer para evitar que a barata reapareça imediatamente
                    self.changePlace()
                    self.spawn_time = 0

    def is_mouse_over(self, mouse_pos):
        # Override to include both sprite and its menu in hover area
        return self.rect.collidepoint(mouse_pos)

    def changePlace(self):
        # Altera a posição da barata para uma nova posição aleatória na tela
        self.x0 = np.random.randint(0, self.gc.screen.get_width() - self.image.get_width())
        self.y0 = np.random.randint(100, self.gc.screen.get_height() - self.image.get_height())
        self.x = self.x0
        self.y = self.y0
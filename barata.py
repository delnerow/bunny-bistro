import pygame
import numpy as np
from HoverSprite import HoverSprite

class Barata(HoverSprite):
    def __init__(self, gc):
        self.image = pygame.image.load("images/barata.png").convert_alpha()
        self.image= pygame.transform.scale(self.image, (32, 32))
        self.screen = gc.screen
        self.x0 = 100
        self.y0 = 300
        self.x = self.x0
        self.y = self.y0
        super().__init__(self.image, self.x, self.y, self.mirar, self.mirar)
        self.gc = gc

        self.live = True  # Define se a barata está viva
        
        #movimento da baratinha
        self.t = 0
        self.f1 = 2.3
        self.f2 = 3

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

            #verifica se está com a arma
            if self.hovering:
                # Verifica se o mouse foi clicado
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # Se a mira estiver na barata, chama o método de atirar
                        self.gc.player.shoot()
                        self.live = False
                        self.changePlace()        
                        self.gc.player.mira = False
                        self.hovering = False  # Reseta o estado de hover após clicar
        else:
            if np.random.random() < 0.01:  # 0.01% chance
                self.live = True
                self.changePlace()

    def is_mouse_over(self, mouse_pos):
        # Override to include both sprite and its menu in hover area
        return self.rect.collidepoint(mouse_pos)

    def changePlace(self):
        # Altera a posição da barata para uma nova posição aleatória na tela
        self.x0 = np.random.randint(0, self.gc.screen.get_width() - self.image.get_width())
        self.y0 = np.random.randint(100, self.gc.screen.get_height() - self.image.get_height())
        self.x = self.x0
        self.y = self.y0
import pygame
from HoverSprite import HoverSprite

class Barata(HoverSprite):
    def __init__(self, gc):
        self.image = pygame.image.load("images/barata.png").convert_alpha()
        self.image= pygame.transform.scale(self.image, (16, 16))
        self.screen = gc.screen
        self.x = 100
        self.y = 300
        super().__init__(self.image, self.x, self.y, self.mirar, self.mirar)
        self.gc = gc
        self.sound = pygame.mixer.Sound("sounds\gunPrepare.mp3")

    def mirar(self):
        print("muda a mira")
        mirando = not self.gc.player.mira
        self.gc.player.mira = mirando

        if mirando:
            self.sound.play()

    def update(self, events):
        super().update(events)  # <-- This brings back hover detection!
    
    def is_mouse_over(self, mouse_pos):
        # Override to include both sprite and its menu in hover area
        return self.rect.collidepoint(mouse_pos)
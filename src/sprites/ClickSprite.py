import pygame
 
# Sprite acionável ao clicar o mouse nele
class ClickableSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, callback):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.rect.x = x
        self.rect.y = y
        self.callback = callback
    # self.rect faz um collider em torno da imagem 
    # pro point&click do mouse detectar
    # Callback é a função a ser chamada quando for clicada
 
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.callback()
    # Atualiza em busca do evento do clique do mouse
    # Caso tenha clicado no collider
    # chamar callback
 

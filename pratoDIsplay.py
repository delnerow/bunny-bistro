import pygame


class PratoDisplay():
    def __init__(self, screen):
        self.screen = screen
        self.items = []  #lista de itens do menu
        #self.image = pygame.image.load("images/menu.png").convert_alpha()
        #self.group = pygame.sprite.Group()
        self.SLOT_SIZE = 16
        self.PADDING = 10
        self.width = 300
        self.height = 100
        self.receita = ""


    def update_ingrediente(self, prato):
        self.items=prato.ingredientes
        self.receita = prato.validar_receita()
        
        
    def display(self, x, y):
        background_rect = pygame.Rect(x - 5, y - 5, self.width + 10, self.height + 10)
        pygame.draw.rect(self.screen, (139, 69, 19), background_rect, border_radius=8)  # Brown with rounded corners

        #self.screen.blit(self.image, (x, y))
        #self.group.draw(self.screen)
        for item in self.items:
            self.screen.blit(item.sprite.image, (x, y))
            x += self.SLOT_SIZE + self.PADDING
    
    def update(self, events):
        pass
        #self.group.update(events)
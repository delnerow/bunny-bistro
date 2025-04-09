import pygame


class PratoDisplay():
    def __init__(self, screen):
        self.screen = screen
        self.items = []  #lista de itens do menu
        #self.image = pygame.image.load("images/menu.png").convert_alpha()
        #self.group = pygame.sprite.Group()
        self.SLOT_SIZE = 16
        self.PADDING = 10
        TEXT_AREA_WIDTH = 120
        self.width = 300
        self.height = 100
        self.receita = ""
        self.font = pygame.font.SysFont(None, 24)
        self.TEXT_COLOR = (255, 255, 255)


    def update_ingrediente(self, prato):
        self.items=prato.ingredientes
        self.receita = prato.validar_receita()
        
        
    def display(self, x, y):
        background_rect = pygame.Rect(x - 5, y - 5, self.width + 10, self.height + 10)
        pygame.draw.rect(self.screen, (139, 69, 19), background_rect, border_radius=8)  # Brown with rounded corners
        x0=x
        y0=y
        #self.screen.blit(self.image, (x, y))
        #self.group.draw(self.screen)
        for item in self.items:
            self.screen.blit(item.sprite.image, (x0, y0))
            x0 += self.SLOT_SIZE + self.PADDING
            text = self.font.render(f"{self.receita}", True, self.TEXT_COLOR)
            text_x = x + 40 + self.PADDING
            text_y = y + self.height // 2 - text.get_height() // 2
            self.screen.blit(text, (text_x, text_y))
    
    def update(self, events):
        pass
        #self.group.update(events)
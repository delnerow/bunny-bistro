import pygame


class PratoDisplay():
    def __init__(self, screen):
        self.screen = screen
        self.width = 300
        self.height = 100
        #
        # tela do jogo 
        # comprimento do menu 
        # altura do menu
        #
        
        self.items = []  
        self.tamanho_item = 16
        self.padding = 10
        
        #
        # items para serem displayados 
        # tamanho do sprite do item
        # espaço entre itens
        #
        
        self.receita = ""
        self.font = pygame.font.SysFont(None, 24)
        self.TEXT_COLOR = (255, 255, 255)
        
        #
        # receita a ser displayada 
        # fonte do texto
        # cor do texto
        #


    def update_ingrediente(self, prato):
        self.items=prato.ingredientes
        self.receita = prato.validar_receita()
        
        #
        # atualiza os itens pelos ingredientes do prato
        # atualiza receita pela validacao do prato
        #
        
        
    def display(self, x, y):
        background_rect = pygame.Rect(x - 5, y - 5, self.width + 10, self.height + 10)
        pygame.draw.rect(self.screen, (139, 69, 19), background_rect, border_radius=8)  # Brown with rounded corners
        x0=x
        y0=y
        for item in self.items:
            self.screen.blit(item.sprite.image, (x0, y0))
            x0 += self.tamanho_item + self.padding
        text = self.font.render(f"{self.receita}", True, self.TEXT_COLOR)
        text_x = x + 40 + self.padding
        text_y = y + self.height // 2 - text.get_height() // 2
        self.screen.blit(text, (text_x, text_y))
        #
        # menu eh um retangulo marrom 
        # texto
        #
    
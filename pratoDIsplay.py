import pygame
pedidos={"invalido":"images\prato.png", "Caponata":"images\pratos\caponata.png", "Hamburguer":"images\pratos\hamburguer.png","Quiche":"images\pratos\quiche.png"}


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
        self.receita_image = None
        
        #
        # receita a ser displayada 
        # fonte do texto
        # cor do texto
        #


    def update_ingrediente(self, prato):
        if(prato!= None):
            self.items=prato.ingredientes
            self.receita = prato.validar_receita()
            self.receita_image = pygame.image.load(pedidos[self.receita]).convert_alpha()
            self.receita_image = pygame.transform.scale_by(self.receita_image, 2.5)
        else:
            self.items=[]
            self.receita="sem prato"
            self.receita_image = None
        
        
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
        
        if self.receita_image:
            receita_x = x + 170 
            receita_y = y 
            self.screen.blit(self.receita_image, (receita_x,receita_y))
        #
        # menu eh um retangulo marrom 
        # texto
        #
    
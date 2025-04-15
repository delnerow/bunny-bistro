import pygame
pedidos={"invalido":"images\prato.png", "Caponata":"images\pratos\caponata.png", "Hamburguer":"images\pratos\hamburguer.png","Quiche":"images\pratos\quiche.png"}
preparos={1:"images\\knife.png", 2:"images\whisk42x42.png",3:"images\\fire16x16.png"}


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
        self.x_padding = 10
        self.y_padding=10
        
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
        
        x0=x+100
        y0=y-40
        for item in self.items:
            
            for estado in item.estadoNumerico():
                ye=y0
                xe=x0
                preparo_image = pygame.image.load(preparos[estado]).convert_alpha()
                factor = 1.5
                if estado==1:
                    factor=1.5
                    ye = y0-20
                    xe=x0-25
                if estado == 2:
                    factor =1.2
                elif estado == 3:
                    ye=y0+25
                    xe=x0+5
                    factor =2.5
                preparo_image = pygame.transform.scale_by(preparo_image,factor)
                self.screen.blit(preparo_image, (xe, ye))
            self.screen.blit(item.sprite.image, (x0, y0))
            x0 += self.tamanho_item + self.x_padding
            
            
        
        if self.receita_image:
            receita_x = x + 160
            receita_y = y +40
            self.screen.blit(self.receita_image, (receita_x,receita_y))
        #
        # menu eh um retangulo marrom 
        # texto
        #
    
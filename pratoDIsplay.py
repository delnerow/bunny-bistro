import pygame
pedidos={"invalido":"images\\cozinha\\prato.png", "Caponata":"images\\pratos\\caponata.png", "Hamburguer":"images\\pratos\\hamburguer.png","Quiche":"images\\pratos\\quiche.png"}
preparos={1:"images\\pratos\\preparos\\knife.png", 2:"images\\pratos\\preparos\\whisk42x42.png",3:"images\\pratos\\preparos\\fire16x16.png"}


# Display de UI com ingredientes atuais e possível prato feito
class PratoDisplay():
    def __init__(self, screen):
        self.screen = screen
        self.width = 300
        self.height = 100
        
        # :scree:       Tela do jogo 
        # :width:       Comprimento do menu 
        # :height:      Altura do menu

        
        self.items = []  
        self.tamanho_item = 16
        self.x_padding = 10
        self.y_padding=10
        
        # :items: Lista de ingredientes a serem exibidos
        # :tamanho_item: Tamanho do sprite de cada ingrediente
        # :x_padding: Espaço horizontal entre itens
        # :y_padding: Espaço vertical entre itens

        
        self.receita = ""
        self.receita_image = None
        
        # :receita: Nome da receita validada 
        # :receita_image: Imagem da receita a ser mostrada#


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
        
    # Atualiza os itens com os ingredientes do prato
    # e busca a imagem da receita validada, se houver
        
        
    def display(self, x, y):
        
        x0=x+100
        y0=y-40
        for item in self.items:
            
            for estado in item.estado_Numerico():
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
            self.screen.blit(item.image, (x0, y0))
            x0 += self.tamanho_item + self.x_padding
            
            
        
        if self.receita_image:
            receita_x = x + 160
            receita_y = y +40
            self.screen.blit(self.receita_image, (receita_x,receita_y))
    # Exibe os ingredientes e a imagem da receita (se houver)
    # na tela, com o layout definido
    
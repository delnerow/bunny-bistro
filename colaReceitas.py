import pygame

# Imagem de Receitas
class ColaUI():
    def __init__(self,x,y):
        self.image = pygame.image.load("images\\pratos\\colas.png").convert_alpha()  # carrega a imagem do balão
        self.image = pygame.transform.scale_by(self.image, 0.4)
        self.x=x
        self.y=y
        # :image:           Carrega e dimensiona imagem
        # :x:               Posição x do cliente 
        # :y:               Posição y do cliente
        
    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))
    # Desenha a cola das receitas
import pygame

class Menu:
    def __init__(self, gc, items,x,y):
        self.screen = gc.screen
        self.x=x
        self.y=y
        self.items = items 
        self.image = pygame.image.load("images/menu.png").convert_alpha()
        self.group = pygame.sprite.Group()
        padding = 32+16
        i =0
        for item in self.items:
            item.rect.x= self.x +(i%3)*padding+32+16-4
            item.rect.y= self.y +(i//3)*padding
            self.group.add(item)
            i=i+1
        # :screen: Superfície onde o menu será desenhado
        # :x: Posição X do menu na tela
        # :y: Posição Y do menu na tela
        # :items: Lista de itens que compõem o menu
        # :image: Imagem de fundo do menu
        # :group: Grupo de sprites que serão desenhadas no menu
        # :padding: Espaçamento horizontal e vertical entre os itens
        
    def get_rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        self.group.draw(self.screen)
    
    def update(self, events):
        self.group.update(events)
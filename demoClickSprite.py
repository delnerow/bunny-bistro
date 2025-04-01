import pygame

from ClickSprite import ClickableSprite
from gameController import GameController
from ingrediente import Cebola, Tomate
from maquina import Batedeira, Forno, Tabua




pygame.init()
screen = pygame.display.set_mode((800, 600))
coelinho = GameController()
tabua = Tabua(coelinho,50,50)
forno = Forno(coelinho,50,230)

batedeira = Batedeira(coelinho,50,400)
tomate = Tomate(coelinho, 400,100)
cebola = Cebola(coelinho,400,300)

#sprite = ClickableSprite(pygame.image.load('images/tabua.png').convert_alpha(), 50, 50, on_click)
group = pygame.sprite.Group()
group.add(tabua.sprite)
group.add(forno.sprite)
group.add(batedeira.sprite)
group.add(tomate.sprite)
group.add(cebola.sprite)
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
 
    group.update(events)
    screen.fill((255, 255, 255))
    group.draw(screen)
    pygame.display.update()
 
pygame.quit()
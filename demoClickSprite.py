import pygame

from ClickSprite import ClickableSprite
from gameController import GameController
from ingrediente import Cebola, Tomate
from maquina import Batedeira, Forno, Tabua
from lixo import Lixo




pygame.init()
screen = pygame.display.set_mode((800, 600))
#iniciando objetos
coelinho = GameController()

tabua = Tabua(coelinho,50,50)
forno = Forno(coelinho,50,230)
batedeira = Batedeira(coelinho,50,400)
lixo = Lixo(coelinho, 700, 150)

tomate = Tomate(coelinho, 400,100)
cebola = Cebola(coelinho,400,300)

#fazendo os sprites renderizarem
group = pygame.sprite.Group()
group.add(tabua.sprite)
group.add(forno.sprite)
group.add(batedeira.sprite)
group.add(tomate.sprite)
group.add(cebola.sprite)
group.add(lixo.sprite)
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    # update dos sprites
    group.update(events)
    screen.fill((255, 255, 255))
    group.draw(screen)
    pygame.display.update()
 
pygame.quit()
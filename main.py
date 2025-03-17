# importando modulos
import pygame
import sys

pygame.init()

# criando display
display = pygame.display.set_mode((500, 500))

# criando image surface
image = pygame.image.load('exemplo.png')

# colocando image surface no display surface
display.blit(image,(1000,1000))

pygame.time.wait(5000)

while True:
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
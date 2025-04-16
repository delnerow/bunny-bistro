import pygame, sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("tituloo")
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("images\\cozinha_demo.png").convert_alpha()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            #atualização
            self.update()

            #impressão na tela
            self.print()

    def update(self):
        # Atualiza a lógica do jogo aqui
        pass

    def print(self):
        # Desenha o fundo
        self.screen.blit(self.background, (0, 0))

        # Atualiza a tela
        pygame.display.flip()
        self.clock.tick(60)
    

game = Game()
game.run()
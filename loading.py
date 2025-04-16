import pygame
import sys

class LoadingScreen:
    def __init__(self, screen):
        self.screen = screen
        self.spritesheet = pygame.image.load("images\\loading_spritesheet.png").convert_alpha()
        
        # Definir as dimensões dos frames da animação
        self.frame_width = 64  # Largura de cada frame na spritesheet
        self.frame_height = 64  # Altura de cada frame na spritesheet
        self.frames = []  # Lista para armazenar os frames extraídos

        # Extrair os frames da spritesheet
        num_frames = 4  # Número de frames na spritesheet
        for i in range(num_frames):
            frame = self.spritesheet.subsurface(i * self.frame_width, 0, self.frame_width, self.frame_height)
            self.frames.append(frame)

        self.current_frame = 0
        self.frame_speed = 10  # Velocidade da animação (quanto maior, mais rápido)
        self.frame_counter = 0

    def update(self):
        # Atualizar a animação, alternando os frames
        self.frame_counter += 1
        if self.frame_counter >= self.frame_speed:
            self.frame_counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)

    def draw(self):
        # Desenha o frame atual da animação no centro da tela
        frame = self.frames[self.current_frame]
        frame_x = self.screen.get_width() // 2 - self.frame_width // 2
        frame_y = self.screen.get_height() // 2 - self.frame_height // 2
        self.screen.blit(frame, (frame_x, frame_y))

    def display(self):
        # Método para rodar a cena de loading
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Atualiza o frame da animação
            self.update()

            # Preenche a tela com a cor preta
            self.screen.fill((0, 0, 0))

            # Desenha o frame atual da animação
            self.draw()

            # Atualiza a tela
            pygame.display.flip()

            # Simula um processo de carregamento (diminua o tempo de execução para testar)
            pygame.time.wait(50)

# Código para rodar a tela de loading
pygame.init()
screen = pygame.display.set_mode((800, 600))
loading_screen = LoadingScreen(screen)
loading_screen.display()

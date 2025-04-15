
import pygame


def get_image(sheet, width, height, scale, colour, position):
    # retira uma fração de uma imagem maior para utilizar
    # como sprite, usado para elementos pequenos na tela

    image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
    image.blit(sheet, (0, 0), (width * position[0], height * position[1], width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    if colour is not None:
        image.set_colorkey(colour)
    return image

class Window():
    def __init__(self,x,y):
        self.image = pygame.image.load("images\window.png").convert_alpha()
        frame_height = self.image.get_height() // 66
        frame_width = self.image.get_width()
        self.frames = [get_image(self.image, frame_width, frame_height, 3, None, (0, i)) for i in range(66)]
        self.current_frame = 0
        self.timer = 0
        self.frame_counter = 0
        self.frame_speed = 8
        self.frame_duration = 0.05  # time between frames, adjust for speed
        self.skin = self.frames[self.current_frame]
        self.skin = pygame.transform.scale_by(self.skin, 0.15)
        
        self.x=x
        self.y=y
        
    def update(self):
        self.frame_counter += 1
        if self.frame_counter >= self.frame_speed:
            self.frame_counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.skin = self.frames[self.current_frame]
            self.skin = pygame.transform.scale_by(self.skin, 0.15)


    def print(self,screen):
        screen.blit(self.skin, (self.x, self.y))
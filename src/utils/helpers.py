import pygame


def get_image(sheet, width, height, scale, colour, position):
    image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
    image.blit(sheet, (0, 0), (width * position[0], height * position[1], width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    if colour is not None:
        image.set_colorkey(colour)
    return image
    # Retira uma fração de uma imagem maior (spritesheet) para utilizar
    # como sprite animados
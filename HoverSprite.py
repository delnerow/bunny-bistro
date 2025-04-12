import pygame


class HoverSprite(pygame.sprite.Sprite):
    def __init__(self,image,x,y,callback, exit_callback):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

        self.rect.x = x
        self.rect.y = y
        self.callback = callback
        self.exit_callback = exit_callback

        self.hovering = False  # Tracks hover state from previous frame

    def is_mouse_over(self, mouse_pos):
        print("ooon")
        return self.rect.collidepoint(mouse_pos)
    
    def update(self,events):
        mouse_pos = pygame.mouse.get_pos()
        is_hovering_now = self.is_mouse_over(mouse_pos)

        # Detect new hover
        if is_hovering_now and not self.hovering:
            self.hovering = True
            print("hoover")
            self.callback()
        elif not is_hovering_now and self.hovering:
            self.hovering = False  # mouse exited
            if(self.exit_callback()):   
                self.exit_callback()

    
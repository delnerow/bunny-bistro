import pygame


class IntroAnimation:
    def __init__(self, screen):
        self.screen = screen
        self.overlay_alpha = 255
        self.fade_speed = 3

        self.logo = pygame.image.load("images\\animacoes\\logo.png").convert_alpha()
        self.logo = pygame.transform.scale_by(self.logo, 0.5)

        self.spritesheet = pygame.image.load("images\\animacoes\\animacao.png").convert_alpha()
        self.num_frames = 5
        self.frame_width = self.spritesheet.get_width()
        self.frame_height = self.spritesheet.get_height() // self.num_frames
        self.frames = [
            self.spritesheet.subsurface((0, i * self.frame_height, self.frame_width, self.frame_height))
            for i in range(self.num_frames)
        ]

        self.current_frame = 0
        self.frame_counter = 0
        self.frame_duration = 10
        self.plaque_done = False

        self.logo_alpha = 255
        self.logo_fade_out = False
        self.transition_done = False

    def update(self):
        if not self.plaque_done:
            if self.overlay_alpha > 0:
                self.overlay_alpha -= self.fade_speed
            else:
                self.frame_counter += 1
                if self.frame_counter >= self.frame_duration:
                    self.frame_counter = 0
                    if self.current_frame < len(self.frames) - 1:
                        self.current_frame += 1
                    else:
                        self.plaque_done = True
                        self.logo_fade_out = True

        elif self.logo_fade_out:
            if self.logo_alpha > 0:
                self.logo_alpha -= self.fade_speed
            else:
                self.transition_done = True

    def draw(self):
        self.screen.fill((0, 0, 0))

        # Logo
        logo_copy = self.logo.copy()
        logo_copy.set_alpha(self.logo_alpha if self.logo_fade_out else 255)
        lx = self.screen.get_width() // 2 - logo_copy.get_width() // 2
        ly = self.screen.get_height() // 2 - logo_copy.get_height() // 2 - 100
        self.screen.blit(logo_copy, (lx, ly))

        # Plaquinha
        if self.overlay_alpha <= 0:
            plaque_copy = self.frames[self.current_frame].copy()
            plaque_copy.set_alpha(self.logo_alpha if self.logo_fade_out else 255)
            px = self.screen.get_width() // 2 - self.frame_width // 2
            py = self.screen.get_height() // 2 - self.frame_height // 2 + 50
            self.screen.blit(plaque_copy, (px, py))

        # White overlay
        if self.overlay_alpha > 0:
            fade_surface = pygame.Surface(self.screen.get_size()).convert_alpha()
            fade_surface.fill((255, 255, 255))
            fade_surface.set_alpha(self.overlay_alpha)
            self.screen.blit(fade_surface, (0, 0))
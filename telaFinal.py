import pygame

class TelaFinal:
    def __init__(self, gc):
        self.gc = gc
        self.background_bad = pygame.image.load("images\\tela_final\\tela_bad_end.jpg")
        self.background_bad = pygame.transform.scale(self.background_bad, (16 * 64, 9 * 64))
        self.background_good = pygame.image.load("images\\tela_final\\tela_good_end.jpg")
        self.background_good = pygame.transform.scale(self.background_good, (16 * 64, 9 * 64))
        self.clock = pygame.time.Clock()

        self.botao_tente_novamente = self.load_scaled("images\\tela_final\\botao_tente_novamente.png", 1.5)
        self.botao_tente_hover = self.load_scaled("images\\tela_final\\botao_tente_novamente.png", 1.7)

        self.botao_sair_normal = self.load_scaled("images\\tela_final\\botao_sair.png", 1.5)
        self.botao_sair_hover = self.load_scaled("images\\tela_final\\botao_sair.png", 1.7)

        self.tentar_rect_base = pygame.Rect(360, 248, *self.botao_tente_novamente.get_size())
        self.sair_rect_base = pygame.Rect(360, 360, *self.botao_sair_normal.get_size())

    def load_scaled(self, path, scale):
        img = pygame.image.load(path)
        size = img.get_size()
        return pygame.transform.scale(img, (int(size[0] * scale), int(size[1] * scale)))


    def run_bad(self):
        running = True
        self.gc.music_Manager.tocar_musica("sounds\\bad.mp3")
        while running:
            self.gc.screen.blit(self.background_bad, (0, 0))
            mouse_pos = pygame.mouse.get_pos()
            cursor_changed = False

            # TENTAR
            if self.tentar_rect_base.collidepoint(mouse_pos):
                botao = self.botao_tente_hover
                rect = botao.get_rect(center=self.tentar_rect_base.center)
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                cursor_changed = True
            else:
                botao = self.botao_tente_novamente
                rect = self.tentar_rect_base
            self.gc.screen.blit(botao, rect.topleft)

            # SAIR
            if self.sair_rect_base.collidepoint(mouse_pos):
                botao = self.botao_sair_hover
                rect = botao.get_rect(center=self.sair_rect_base.center)
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                cursor_changed = True
            else:
                botao = self.botao_sair_normal
                rect = self.sair_rect_base
            self.gc.screen.blit(botao, rect.topleft)

            if not cursor_changed:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.fadeout(1000)  # Fade ao sair
                    return "sair"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.tentar_rect_base.collidepoint(event.pos):
                        pygame.mixer.music.fadeout(1000)  # Fade ao sair
                        pygame.time.delay(1000)
                        pygame.mixer.music.load("sounds\\music.mp3")
                        print("tentar")
                        return "tentar"
                    elif self.sair_rect_base.collidepoint(event.pos):
                        pygame.mixer.music.fadeout(1000)  # Fade ao sair
                        return "sair"

            pygame.display.flip()
            self.clock.tick(60)

    def run_good(self):
        running = True
        self.gc.music_Manager.tocar_musica("sounds\\good.mp3")
        self.sair_rect_base = pygame.Rect(670, 395, *self.botao_sair_normal.get_size())

        while running:
            self.gc.screen.blit(self.background_good, (0, 0))
            mouse_pos = pygame.mouse.get_pos()
            cursor_changed = False

            # SAIR
            if self.sair_rect_base.collidepoint(mouse_pos):
                botao = self.botao_sair_hover
                rect = botao.get_rect(center=self.sair_rect_base.center)
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                cursor_changed = True
            else:
                botao = self.botao_sair_normal
                rect = self.sair_rect_base
            self.gc.screen.blit(botao, rect.topleft)

            if not cursor_changed:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.fadeout(1000)  # Fade ao sair
                    return "sair"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.sair_rect_base.collidepoint(event.pos):
                        pygame.mixer.music.fadeout(1000)  # Fade ao sair
                        return "sair"

            pygame.display.flip()
            self.clock.tick(60)


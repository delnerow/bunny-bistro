import pygame

class TelaInicial:
    def __init__(self, gc):
        self.gc = gc
        self.background = pygame.image.load("images\\tela-inicial\\tela-fundo.png")
        self.background = pygame.transform.scale(self.background, (16*64, 9*64))
        self.clock = pygame.time.Clock()

        self.botao_jogar_normal = self.load_scaled("images\\tela-inicial\\botao-jogar.png", 1.5)
        self.botao_jogar_hover = self.load_scaled("images\\tela-inicial\\botao-jogar.png", 1.7)

        self.botao_instrucoes_normal = self.load_scaled("images\\tela-inicial\\botao-instrucoes.png", 1.5)
        self.botao_instrucoes_hover = self.load_scaled("images\\tela-inicial\\botao-instrucoes.png", 1.7)

        self.botao_sair_normal = self.load_scaled("images\\tela-inicial\\botao-sair.png", 1.5)
        self.botao_sair_hover = self.load_scaled("images\\tela-inicial\\botao-sair.png", 1.7)

        self.jogar_rect_base = pygame.Rect(550, 200, *self.botao_jogar_normal.get_size())
        self.instrucoes_rect_base = pygame.Rect(550, 310, *self.botao_instrucoes_normal.get_size())
        self.sair_rect_base = pygame.Rect(550, 420, *self.botao_sair_normal.get_size())
        self.tocar_musica()

    def load_scaled(self, path, scale):
        img = pygame.image.load(path)
        size = img.get_size()
        return pygame.transform.scale(img, (int(size[0]*scale), int(size[1]*scale)))
    def tocar_musica(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load("sounds\\telaStart.mp3")  # seu arquivo de música
        pygame.mixer.music.set_volume(0.5)  # volume de 0.0 até 1.0
        pygame.mixer.music.play(-1)  # -1 = loop infinito
        
    def run(self):
        running = True

        while running:
            self.gc.screen.blit(self.background, (0, 0))
            mouse_pos = pygame.mouse.get_pos()
            cursor_changed = False

            # JOGAR
            if self.jogar_rect_base.collidepoint(mouse_pos):
                botao = self.botao_jogar_hover
                rect = botao.get_rect(center=self.jogar_rect_base.center)
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                cursor_changed = True
            else:
                botao = self.botao_jogar_normal
                rect = self.jogar_rect_base
            self.gc.screen.blit(botao, rect.topleft)

            # INSTRUÇÕES
            if self.instrucoes_rect_base.collidepoint(mouse_pos):
                botao = self.botao_instrucoes_hover
                rect = botao.get_rect(center=self.instrucoes_rect_base.center)
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                cursor_changed = True
            else:
                botao = self.botao_instrucoes_normal
                rect = self.instrucoes_rect_base
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
                    if self.jogar_rect_base.collidepoint(event.pos):
                        pygame.mixer.music.fadeout(1000)  # Fade ao sair
                        pygame.time.delay(1000)
                        pygame.mixer.music.load("sounds\\music.mp3")
                        return "jogar"
                    elif self.instrucoes_rect_base.collidepoint(event.pos):
                        return "instrucoes"
                    elif self.sair_rect_base.collidepoint(event.pos):
                        pygame.mixer.music.fadeout(1000)  # Fade ao sair
                        return "sair"

            pygame.display.flip()
            self.clock.tick(60)

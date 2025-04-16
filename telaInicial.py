import pygame
import sys
from gameController import GameController
def mostrar_tela_inicial():
    pygame.init()

    screen = pygame.display.set_mode((16*64, 9*64))

    background = pygame.image.load("images/tela-inicial/tela-fundo.png")
    background = pygame.transform.scale(background, (16*64, 9*64))

    def load_scaled(path, scale):
        img = pygame.image.load(path)
        size = img.get_size()
        return pygame.transform.scale(img, (int(size[0]*scale), int(size[1]*scale)))

    botao_jogar_normal = load_scaled("images/tela-inicial/botao-jogar.png", 1.5)
    botao_jogar_hover = load_scaled("images/tela-inicial/botao-jogar.png", 1.7)

    botao_instrucoes_normal = load_scaled("images/tela-inicial/botao-instrucoes.png", 1.5)
    botao_instrucoes_hover = load_scaled("images/tela-inicial/botao-instrucoes.png", 1.7)

    botao_sair_normal = load_scaled("images/tela-inicial/botao-sair.png", 1.5)
    botao_sair_hover = load_scaled("images/tela-inicial/botao-sair.png", 1.7)

    jogar_rect_base = pygame.Rect(550, 200, *botao_jogar_normal.get_size())
    instrucoes_rect_base = pygame.Rect(550, 310, *botao_instrucoes_normal.get_size())
    sair_rect_base = pygame.Rect(550, 420, *botao_sair_normal.get_size())

    clock = pygame.time.Clock()
    running = True
    while running:
        screen.blit(background, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        cursor_changed = False

        # JOGAR
        if jogar_rect_base.collidepoint(mouse_pos):
            botao = botao_jogar_hover
            rect = botao.get_rect(center=jogar_rect_base.center)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            cursor_changed = True
        else:
            botao = botao_jogar_normal
            rect = jogar_rect_base
        screen.blit(botao, rect.topleft)

        # INSTRUÇÕES
        if instrucoes_rect_base.collidepoint(mouse_pos):
            botao = botao_instrucoes_hover
            rect = botao.get_rect(center=instrucoes_rect_base.center)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            cursor_changed = True
        else:
            botao = botao_instrucoes_normal
            rect = instrucoes_rect_base
        screen.blit(botao, rect.topleft)

        # SAIR
        if sair_rect_base.collidepoint(mouse_pos):
            botao = botao_sair_hover
            rect = botao.get_rect(center=sair_rect_base.center)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            cursor_changed = True
        else:
            botao = botao_sair_normal
            rect = sair_rect_base
        screen.blit(botao, rect.topleft)

        # Reset cursor se não estiver sobre nenhum botão
        if not cursor_changed:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if jogar_rect_base.collidepoint(event.pos):
                    print("Clicou em Jogar!")
                    pygame.quit()  
                    game = GameController()
                    game.run()    
                    return 
                elif instrucoes_rect_base.collidepoint(event.pos):
                    print("Clicou em Instruções!")
                elif sair_rect_base.collidepoint(event.pos):
                    print("Clicou em Sair!")
                    running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
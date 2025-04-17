import pygame
import os

class Tela:
    def __init__(self, gc, background_path):
        self.gc = gc
        self.screen = gc.screen
        self.screen_size = self.screen.get_size()
        self.clock = pygame.time.Clock()
        self.background = self._load_background(background_path, self.screen_size)
        self.buttons = [] # Lista para armazenar informações dos botões
        self.running = False
        self.next_state = None # Para onde ir depois que a tela terminar

    def _load_background(self, path, size):
        #Carrega e escala a imagem de fundo.
        try:
            image = pygame.image.load(path).convert()
            return pygame.transform.scale(image, size)
        except pygame.error as e:
            print(f"Erro ao carregar a imagem de fundo: {path}")
            print(e)
            # Retorna uma superfície preta como fallback
            fallback_surface = pygame.Surface(size)
            fallback_surface.fill((0, 0, 0))
            return fallback_surface

    def load_scaled(self, path, scale):
        #Carrega uma imagem e a escala.
        try:
            img = pygame.image.load(path).convert_alpha()
            size = img.get_size()
            new_size = (int(size[0] * scale), int(size[1] * scale))
            return pygame.transform.scale(img, new_size)
        except pygame.error as e:
            print(f"Erro ao carregar/escalar imagem: {path}")
            print(e)
            # Retorna uma pequena superfície transparente como fallback
            fallback_surface = pygame.Surface((50, 20), pygame.SRCALPHA)
            fallback_surface.fill((0, 0, 0, 0))
            return fallback_surface

    def add_button(self, name, normal_path, hover_path, position, action, scale_normal=1.5, scale_hover=1.7):
        #Adiciona um botão à tela.
        img_normal = self.load_scaled(normal_path, scale_normal)
        img_hover = self.load_scaled(hover_path, scale_hover)
        rect_base = pygame.Rect(position, img_normal.get_size())

        button_info = {
            'name': name,
            'img_normal': img_normal,
            'img_hover': img_hover,
            'rect_base': rect_base,
            'action': action,
            # Estado atual (será atualizado no loop)
            'current_img': img_normal,
            'current_rect': rect_base
        }
        self.buttons.append(button_info)

    def on_enter(self):
        #Chamado quando a tela começa a rodar. Subclasses podem sobrescrever.
        pass

    def on_exit(self, action):
        #Chamado antes da tela retornar uma ação. Subclasses podem sobrescrever.
        # Exemplo: fazer fadeout da música ao sair
        if action == "sair" and hasattr(self.gc, 'music_Manager'):
             pygame.mixer.music.fadeout(1000)
        # Outras ações podem ter fadeouts específicos
        pass

    def _handle_input(self):
        #Processa eventos de input (mouse, teclado, fechar janela).
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.next_state = "sair"
                return # Sai do processamento de eventos

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Botão esquerdo
                for button in self.buttons:
                    # Usar current_rect para checar clique, pois pode estar centralizado
                    if button['current_rect'].collidepoint(mouse_pos):
                        self.running = False
                        self.next_state = button['action']
                        return # Sai do processamento de eventos

        # Atualiza estado do cursor baseado no hover fora do loop de eventos
        cursor_changed = False
        for button in self.buttons:
            if button['rect_base'].collidepoint(mouse_pos):
                 # A lógica de qual imagem/rect usar é feita no _update_and_draw
                 pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                 cursor_changed = True
                 break # Apenas um botão pode ter hover para o cursor

        if not cursor_changed:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def _update_and_draw(self):
        #Atualiza estado dos botões (hover) e desenha tudo na tela.
        self.screen.blit(self.background, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        for button in self.buttons:
            if button['rect_base'].collidepoint(mouse_pos):
                button['current_img'] = button['img_hover']
                # Centraliza a imagem maior no centro da base rect
                button['current_rect'] = button['img_hover'].get_rect(center=button['rect_base'].center)
            else:
                button['current_img'] = button['img_normal']
                button['current_rect'] = button['rect_base'] # Volta ao rect original

            self.screen.blit(button['current_img'], button['current_rect'].topleft)

        pygame.display.flip()

    def run(self):
        #Loop principal da tela.
        self.running = True
        self.next_state = None
        self.on_enter() # Hook para ações de entrada (ex: tocar música)

        while self.running:
            self._handle_input()
            if not self.running: # Se _handle_input definiu running = False
                break
            self._update_and_draw()
            self.clock.tick(60)

        self.on_exit(self.next_state) # Hook para ações de saída (ex: fadeout)
        # Reset cursor para o padrão ao sair da tela
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        return self.next_state

# --- Helper para caminhos de assets ---
def asset_path(relative_path):
    #Retorna o caminho absoluto para um asset, lidando com barras.
    # Constrói o caminho base relativo ao script atual ou diretório de trabalho
    # Ajuste 'base_path' se seus assets estiverem em outro lugar
    base_path = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    # Junta as partes do caminho de forma segura
    return os.path.join(base_path, *relative_path.split('/')) # Use '/' no código e os.path.join corrige
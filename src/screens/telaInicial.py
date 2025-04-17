from src.screens.tela import Tela
from src.screens.tela import asset_path

class TelaInicial(Tela):
    def __init__(self, gc):
        background_p = asset_path("assets/images/tela/tela_inicial.png")
        super().__init__(gc, background_p)

        # Adicionar botões
        self.add_button('jogar',
                        asset_path("assets/images/tela/botao_jogar.png"),
                        asset_path("assets/images/tela/botao_jogar.png"), # Mesmo path, scale diferente
                        (550, 200),
                        "jogar", # Ação retornada
                        scale_normal=1.5, scale_hover=1.7)
        self.add_button('instrucoes',
                        asset_path("assets/images/tela/botao_instrucoes.png"),
                        asset_path("assets/images/tela/botao_instrucoes.png"),
                        (550, 310),
                        "instrucoes",
                        scale_normal=1.5, scale_hover=1.7)
        self.add_button('sair',
                        asset_path("assets/images/tela/botao_sair.png"),
                        asset_path("assets/images/tela/botao_sair.png"),
                        (550, 420),
                        "sair",
                        scale_normal=1.5, scale_hover=1.7)

    def on_enter(self):
        #Toca a música da tela inicial.
        if hasattr(self.gc, 'music_Manager'):
            self.gc.music_Manager.tocar_musica(asset_path("assets/sounds/telaStart.mp3"))

    def on_exit(self, action):
        #Faz fadeout em algumas transições.
        super().on_exit(action) # Chama o on_exit base (para o caso 'sair')

class TelaInstrucoes(Tela):
    def __init__(self, gc):
        background_p = asset_path("assets/images/tela/tela_instrucoes.png")
        super().__init__(gc, background_p)

        self.add_button('voltar',
                        asset_path("assets/images/tela/botao_voltar.png"),
                        asset_path("assets/images/tela/botao_voltar.png"),
                        (350, 420),
                        "voltar",
                        scale_normal=1.5, scale_hover=1.7)
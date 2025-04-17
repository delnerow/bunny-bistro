import pygame
from src.screens.tela import Tela
from src.screens.tela import asset_path

class TelaFinal(Tela):
    def __init__(self, gc, end_type): # Recebe 'good' or 'bad'
        self.end_type = end_type
        if end_type == "good":
            background_p = asset_path("assets/images/tela/tela_final_good.jpg")
            music_path = asset_path("assets/sounds/good.mp3")
        else: # Assume "bad"
            background_p = asset_path("assets/images/tela/tela_final_bad.jpg")
            music_path = asset_path("assets/sounds/bad.mp3")

        super().__init__(gc, background_p)
        self.music_path = music_path # Armazena para usar no on_enter

        # Adicionar botões baseado no tipo de final
        if end_type == "good":
            self.add_button('sair',
                            asset_path("assets/images/tela/botao_sair.png"), # Reutiliza botão sair
                            asset_path("assets/images/tela/botao_sair.png"),
                            (670, 395), # Posição específica do Good End
                            "sair",
                            scale_normal=1.5, scale_hover=1.7)
        else: # Bad End
            self.add_button('tentar',
                            asset_path("assets/images/tela/botao_tente_novamente.png"),
                            asset_path("assets/images/tela/botao_tente_novamente.png"),
                            (360, 248),
                            "tentar", # Ação para reiniciar ou voltar
                            scale_normal=1.5, scale_hover=1.7)
            self.add_button('sair',
                            asset_path("assets/images/tela/botao_sair.png"),
                            asset_path("assets/images/tela/botao_sair.png"),
                            (360, 360), # Posição específica do Bad End
                            "sair",
                            scale_normal=1.5, scale_hover=1.7)

    def on_enter(self):
        #Toca a música apropriada para o final.
        if hasattr(self.gc, 'music_Manager'):
            self.gc.music_Manager.tocar_musica(self.music_path)

    def on_exit(self, action):
        #Fadeout para sair ou tentar novamente.
        super().on_exit(action) # Chama o on_exit base (trata 'sair')
        if action == "tentar": # Ação específica do Bad End
             if hasattr(self.gc, 'music_Manager'):
                 pygame.mixer.music.fadeout(1000)

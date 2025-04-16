import pygame


class MusicManager:
    def __init__(self):
        self.current_track = None
        self.volume = 0.2
        pygame.mixer.music.set_volume(self.volume)

    def tocar_musica(self, path, loop=-1, fade_ms=500):
        if self.current_track != path:
            if pygame.mixer.music.get_busy():  # Se alguma música está tocando
                pygame.mixer.music.fadeout(fade_ms)  # Faz o fade out antes de trocar
            self.current_track = path
            pygame.mixer.music.load(path)
            pygame.mixer.music.play(loop, fade_ms=fade_ms)

    def parar_musica(self, fade_ms=500):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(fade_ms)
            self.current_track = None

    def set_volume(self, volume):
        self.volume = volume
        pygame.mixer.music.set_volume(self.volume)
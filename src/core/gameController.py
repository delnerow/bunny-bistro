from src.core.musicManager import MusicManager
from src.screens.level import Level
from src.entities.player import Player
import pygame
from src.screens.telaInicial import TelaInicial, TelaInstrucoes
from src.screens.telaFinal import TelaFinal
class GameController:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        icon = pygame.image.load("assets\\images\\icon.bmp")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Bunny-Bistro")

        self.largura_tela = 16 * 64
        self.altura_tela = 9 * 64
        self.screen = pygame.display.set_mode((self.largura_tela, self.altura_tela))

        self.music_Manager = MusicManager()
        self.player = Player()
        self.tela_inicial = TelaInicial(self)
        self.tela_instrucoes = TelaInstrucoes(self)
        self.level = Level(self)

    
    def run(self):
        #Executa o loop principal do jogo como uma máquina de estados.
        estado_atual = "inicial"

        while estado_atual != "sair":

            if estado_atual == "inicial":
                proximo_estado = self.tela_inicial.run()
                estado_atual = proximo_estado

            elif estado_atual == "instrucoes":
                proximo_estado = self.tela_instrucoes.run()
                if proximo_estado == "voltar":
                    estado_atual = "inicial"  # Volta para a tela inicial
                else:
                    break  # Deve ser "sair"

            elif estado_atual == "jogar":
                self.level.reset()  # Garante que o nível comece do zero
                resultado_level = self.level.run()  # Deve retornar pontuação ou "sair"

                if isinstance(resultado_level, (int, float)):  # Verifica se é um número (pontuação)
                    score = resultado_level
                    if score >= 1000:  # Condição de vitória
                        estado_atual = "final_bom"
                    else:  # Condição de derrota
                        estado_atual = "final_ruim"
                elif resultado_level == "sair":  # Se o próprio nível puder ser encerrado
                    estado_atual = "sair"
                else:
                    print(f"Aviso: Level retornou valor inesperado: {resultado_level}. Indo para final ruim.")
                    estado_atual = "final_ruim"  # Fallback seguro

            elif estado_atual == "final_bom":
                tela_final_boa = TelaFinal(self, "good")
                proximo_estado = tela_final_boa.run()
                estado_atual = proximo_estado  # Retorna "sair"

            elif estado_atual == "final_ruim":
                tela_final_ruim = TelaFinal(self, "bad")
                proximo_estado = tela_final_ruim.run()  # Retorna "tentar" ou "sair"
                if proximo_estado == "tentar":
                    estado_atual = "inicial"  # Volta para a tela inicial
                else:  # "sair" ou outro erro
                    estado_atual = proximo_estado  # "sair"

            else:
                print(f"Erro: Estado desconhecido '{estado_atual}'. Encerrando.")
                estado_atual = "sair"

        print("Encerrando Pygame...")
        pygame.quit()
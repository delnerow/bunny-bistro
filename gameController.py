from prato import Prato
from level import Level
from player import Player
import pygame
from telaInicial import TelaInicial, TelaInstrucoes
from telaFinal import TelaFinal
class GameController:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        icon = pygame.image.load("images\\icon.bmp")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Bunny-Bistro")
        self.screen = pygame.display.set_mode((16*64, 9*64))

        self.time=0
        self.player = Player()
        self.level = Level(self)
        self.start = TelaInicial(self)
        self.end = TelaFinal(self)

        self.state = "menu"  # <- Começa pelo menu
        self.clock = pygame.time.Clock()

        

    def run(self):
        escolha_inicial = self.start.run()
        if escolha_inicial == "instrucoes":
            tela_instrucoes = TelaInstrucoes(self)
            resultado_instrucoes = tela_instrucoes.run()
            if resultado_instrucoes == "voltar":
                self.run()
                return
        if escolha_inicial == "sair":
            return  # Sai se não escolher jogar na primeira vez

        # Loop para jogar e tentar novamente
        while True:
            score = self.level.run()
            if score == 1000:
                self.end.run_good()
                break  # Ganhou, sai do loop de jogar/tentar
            else:
                escolha_final = self.end.run_bad()
                if escolha_final == "tentar":
                    escolha_inicial = self.start.run()
                    if escolha_inicial != "jogar":
                        if escolha_inicial == "instrucoes":
                            self.run()
                        break
                    pass
                else:
                    break



    def printOI(self):
        print("oi\n")
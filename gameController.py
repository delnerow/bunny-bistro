
from prato import Prato
#falta bastante coisa, já criei pra não dar catapora na maquina.py
#
#

class GameController:
    def __init__(self):
        self.holderPrato = Prato()
        self.time=0
    def printarPrato(self):
        print("=====Prato atual=====")
        for c in self.holderPrato.ingredientes:
            print(c.nome+"("+str(c.estadoNumerico())+")", end='')
            print("")
        print(" = ", self.holderPrato.validar_receita())
    #
    # atualiza o prato nas mãos do Chef
    #
        
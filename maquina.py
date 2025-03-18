maquinas={"tabua":"C", "batedeira":"B","forno":"F"}
from prato import Prato
from gameController import GameController
class Maquina:
    def __init__(self,tipo):
        self.tipo=tipo
        self.prato_atual= Prato()
    #
    # inicializa uma máqina com tipo definido
    # e desocupada, (acho q pode virar bool)
    # e sabendo qual o gameController
    
    def ocupar(self, bandeja):
        if bandeja.ingredientes != []:
            self.prato_atual.ingredientes= bandeja.ingredientes
            bandeja.limpar_comida()
        else:
            print("Erro: nada na bandeja")
    #
    # esvazia ingredientes da bandeja
    # e ocupa a máquina
    #
    
    def cook(self):
        if(self.prato_atual.ingredientes != []):
            cooked = True
            #lançar minigame
            if cooked:
                for i in range(len(self.prato_atual.ingredientes)):
                   self.prato_atual.ingredientes[i]=self.prato_atual.ingredientes[i]+maquinas[self.tipo]
            else:
                print("Erro: nada para cozinhar")
    # atualiza estados dos ingredientes do prato atual
    # 
    #
    
    def free(self, bandeja):
        if bandeja.ingredientes!=[] and self.prato_atual.ingredientes !=  []:
            bandeja.ingredientes=self.prato_atual.ingredientes
            self.prato_atual.limpar_comida()
        else:
            print("Erro: bandeja cheia/maquina já vazia")
    #
    # retorna ingredientes a bandeja
    # e se desocupa
    #
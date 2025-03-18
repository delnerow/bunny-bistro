maquinas={"tabua":"C", "batedeira":"B","forno":"F"}
from prato import Prato
from gameController import GameController
class Maquina:
    def __init__(self,tipo):
        self.tipo=tipo
        self.prato_atual= Prato() #acho que isso inicializa como vazia
    #
    # inicializa uma máqina com tipo definido
    # e desocupada, (acho q pode virar bool)
    # e sabendo qual o gameController
    
    def ocupar(self, bandeja):
        if bandeja is not None:
            self.prato_atual.ingredientes= bandeja.ingredientes
            bandeja.ingredientes=[]
    #
    # esvazia ingredientes da bandeja
    # e ocupa a máquina
    #
    
    def cook(self):
        if(self.prato_atual is not None):
            cooked = True
            #lançar minigame
            if cooked:
                for i in range(len(self.prato_atual.ingredientes)):
                   self.prato_atual.ingredientes[i]=self.prato_atual.ingredientes[i]+maquinas[self.tipo]
    #
    # atualiza estados dos ingredientes do prato atual
    # 
    #
    
    def free(self, bandeja):
        if bandeja != None and self.prato_atual !=  bandeja:
            bandeja.ingredientes=self.prato_atual.ingredientes
            self.prato_atual= Prato()
    #
    # retorna ingredientes a bandeja
    # e se desocupa
    #
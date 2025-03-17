maquinas={"tabua":"C", "batedeira":"B","forno":"F"}
from prato import Prato
from gameController import GameController
class Maquina:
    def _init(self,tipo, gc):
        self.tipo=tipo
        self.prato_atual= Prato() #acho que isso inicializa como vazia
        self.gc=gc
    #
    # inicializa uma máqina com tipo definido
    # e desocupada, (acho q pode virar bool)
    # e sabendo qual o gameController
    
    def ocupar(self):
        if self.gc.holderPrato is not None:
            self.prato_atual= self.gc.holderPrato
            self.gc.holderPrato=None
    #
    # rouba prato do gameController
    # e ocupa a máquina
    #
    
    def cook(self):
        if(self.prato_atual is not None):
            self.prato_atual
            cooked = False
            #lançar minigame
            if cooked:
                for i in range(len(self.prato_atual.ingredientes)):
                   self.prato_atual.ingredientes[i]=self.prato_atual.ingredientes.append(maquinas[self.tipo]) 
    #
    # atualiza estados dos ingredientes do prato atual
    # 
    #
    
    def free(self):
        if self.gc.holderPrato is not None and self.prato_atual is not None:
            self.gc.holderPrato=self.prato_atual
            self.prato_atual= Prato()
    #
    # retorna prato ao GameController
    # e se desocupa
    #
maquinas={"tabua":"C", "batedeira":"B","forno":"F"}
from prato import Prato
class Maquina:
    def _init(self,tipo):
        self.tipo=tipo
        self.prato_atual= Prato() #acho que isso inicializa como vazia
    #
    # inicializa uma máqina com tipo definido
    # e desocupada, (acho q pode virar bool)
    #
    
    def ocupar(self):
        if GameControler.holderPrato is not None:
            self.prato_atual= GameControler.holderPrato
            GameControler.holderPrato=None
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
        if GameControler.holderPrato is not None and self.prato_atual is not None:
            GameControler.holderPrato=self.prato_atual
            self.prato_atual= Prato()
    #
    # retorna prato ao GameController
    # e se desocupa
    #
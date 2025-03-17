especies=("humano","cao","gato")
from gameController import GameController

class Clientes:
    def __init__(self, paciencia, pedido, especie, gc):
        self.paciencia = paciencia
        self.pedido = pedido
        self.especie = especie
        self.score=0
        self.gc=gc
    #
    # inicializa um cliente com tempo de paciencia
    # pedido desejado, especie do cliente
    # score do pedido
    # e sabendo qual o gameController
    
    def comer(self, prato):
        if(self.pedido is prato.validar_receita()):
            self.score=(100/(self.paciencia-self.gc.time))
        else:
            self.score=0
        return self.score
    #
    # interacao do cliente com oq tem no prato
    # se for oq pediu, brasil
    # 
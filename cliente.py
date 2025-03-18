especies=("humano","cao","gato")
from gameController import GameController
from prato import Prato

class Clientes:
    def __init__(self, paciencia, pedido, especie):
        self.paciencia = paciencia
        self.pedido = pedido
        self.especie = especie
        self.score=0
    #
    # inicializa um cliente com tempo de paciencia
    # pedido desejado, especie do cliente
    # score do pedido
    # e sabendo qual o gameController
    
    def comer(self, prato):
        if(self.pedido is prato.validar_receita()):
            self.score=100
        else:
            self.score=0
        prato.ingredientes = []
        return self.score

    #
    # interacao do cliente com oq tem no prato
    # se for oq pediu, brasil
    #  os ingredientes são consumidos no processo
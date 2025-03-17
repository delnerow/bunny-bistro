especies=("humano","cao","gato")
from gameController import GameController

class Clientes:
    def __init__(self, paciencia, pedido, especie, gc):
        self.paciencia = paciencia
        self.pedido = pedido
        self.especie = especie
        self.score=0
        self.gc=gc
    def comer(self, prato):
        if(self.pedido is prato):
            self.score=(100/(self.gc.time-self.paciencia))
        else:
            self.score=0
        return self.score
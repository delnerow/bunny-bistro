



import random


class FilaMesa():
    def __init__(self):

        self.disponiveis=[]
        self.max=6
        
    def alocar_cliente(self,cliente):
        if(len(self.disponiveis)<self.max):
            #cadeira = random.choice(self.disponiveis)
            cadeira = self.disponiveis[1]
            self.disponiveis.remove(cadeira)
            cadeira.senta(cliente)
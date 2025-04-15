



import random


class FilaMesa():
    def __init__(self):
        self.disponiveis=[]
        self.max=6
        
    def alocar_cliente(self,cliente):
        if(len(self.disponiveis)>0):
            cadeira = random.choice(self.disponiveis)
            self.disponiveis.remove(cadeira)
            cadeira.senta(cliente)
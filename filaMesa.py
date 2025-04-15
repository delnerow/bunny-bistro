import random

# Estrutura que controla o fluxo de clientes servidos certo nas mesas
class FilaMesa():
    def __init__(self):
        self.disponiveis=[]
        # :disponiveis: as cadeiras das mesas disponíveis
        
    def alocar_cliente(self,cliente):
        if(len(self.disponiveis)>0):
            cadeira = random.choice(self.disponiveis)
            self.disponiveis.remove(cadeira)
            cadeira.senta(cliente)
    # Verifica se há cadeiras disponíveis, se sim escolhe uma aleatória, 
    # torna ela indisponível e faz o cliente sentar na cadeira
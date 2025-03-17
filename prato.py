
#muito basico, da pra trocar as strings por números no futuro e melhorar o desempenho
pratos={("tomateC","cebolaC"):"Caponata de Tomate", ("graoCB","farinhaB","leiteB"):"hamburguer",("brocolisCBF","farinhaBF","leiteBF"):"quiche"}

# DISCLAIMER:
# Pensei em duas dinâmicas: o prato sempre tem ingredientes e vc leva o prato as maquinas
# e elas atualizam o estado de tudo que tá la, ou a maquina rouba o ingrediente,
# atualiza ele e depois retorna ao prato. adotei a primeira incialmente
# Agora, uma máquina rouba um prato pra poder liberar espaço do chef e ele fazer
# pratos em paralelo

class Prato:
    def __init__(self):
        self.ingredientes = []
        self.receita = ""
    # 
    # inicializa um prato vazio, sem ingredientes
    # nem receita definida
    #
    
    def add_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)
    # 
    # adiciona um ingrediente ao prato
    #
    
    def prepara_ingrediente(self, tecnica):
        for i in range(len(self.ingredientes)):
            self.ingredientes[i]=self.ingredientes[i]+tecnica
    # 
    # atualiza todos os ingredientes apos
    # cortar, bater ou fornear
    #
    
    def validar_receita(self):
        if tuple(self.ingredientes) in pratos:
            self.receita=pratos[self.ingredientes]
        else:
            self.receita="invalido"
        return self.receita
            
    # 
    # busca uma receita com os
    # ingredientes atuais
    # e retorna oq for achado
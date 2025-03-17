
#muito basico, da pra trocar as strings por números no futuro e melhorar o desempenho
pratos={("tomateC","cebolaC"):"Caponata de Tomate", ("graoCB","farinhaB","leiteB"):"hamburguer",("brocolisCBF","farinhaBF","leiteBF"):"quiche"}

class Prato:
    def __init__(self, ingredientes, receita):
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
    # 
    # busca uma receita com os
    # ingredientes atuais
    #
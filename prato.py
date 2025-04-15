
#Código numérico para relacionar receitas
pratos={((1,),(1,),(0),(0),(0),(0)):"Caponata", ((0),(0),(1,2),(2,),(2,),(0)):"Hamburguer",((0),(0),(0),(2,3),(2,3),(1,2,3)):"Quiche"}
#tomate cebola grao farinha leite brocolis
interface={1:"cortado",2:"batido",3:"assado",12:"cortado e batido",13:"cortado e assado",23:"batido e assado",123:"cortado, assado e batido"}
# Código das receitas (T de tomate, C de cebola... / C de corte, B de bater e A de assar...)
# TCGFLB       C B A  CB CA  ...
# 000000       1 2 3  12 13  ...
# Caponata:   110000
# Hamburguer: 004220
# Quiche :    000667

# DISCLAIMER:
# Pensei em duas dinâmicas: o prato sempre tem ingredientes e vc leva o prato as maquinas
# e elas atualizam o estado de tudo que tá la, ou a maquina rouba o ingrediente,
# atualiza ele e depois retorna ao prato. adotei essa última
# 


#proibir de pegar mais de um ingrediente

class Prato:
    def __init__(self):
        self.ingredientes = []
        self.receita = ""
    # 
    # inicializa um prato vazio, sem ingredientes
    # nem receita definida
    #
    
    def add_ingrediente(self, ingrediente):
        if(len(self.ingredientes)<5):
            self.ingredientes.append(ingrediente)
            print("works")
        else:
            print("Prato cheio! joga no lixo")
    # 
    # adiciona um ingrediente ao prato
    #
    
    def limpar_comida(self):
        self.ingredientes = []
        self.receita = ""
    # 
    # esvazia o prato
    #

    def restaurar_prato(self):
        for ing in self.ingredientes:
            ing.restaurar()
     
    def validar_receita(self):
        receitaNumerica=[(0),(0),(0),(0),(0),(0)]
        for ingrediente in self.ingredientes:
            receitaNumerica[ingrediente.indiceReceita]=ingrediente.estadoNumerico()
        if tuple(receitaNumerica) in pratos:
            self.receita=pratos[tuple(receitaNumerica)]
        else:
            self.receita="invalido"
        return self.receita 
    # 
    # busca uma receita com os
    # ingredientes atuais
    # e retorna oq for achado
    #
    
    
    def esta_vazio(self):
        return self.ingredientes == []
    # 
    # retorna se o prato esta vazio
    #
            

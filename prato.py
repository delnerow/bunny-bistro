
#Código numérico para relacionar receitas
pratos={(1,1,0,0,0,0):"Caponata", (0,0,4,2,2,0):"hamburguer",(0,0,0,6,6,7):"quiche"}
# Código das receitas (T de tomate, C de cebola... / C de corte, B de bater e A de assar...)
# TCGFLB       C B A  CB CA BA CBA
# 000000       1 2 3  4  5  6  7
# Caponata: 110000
# Hamburguer: 004220
# Quiche : 000667

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
    
    def limpar_comida(self):
        self.ingredientes = []
        self.receita = ""
    # 
    # esvazia o prato
    #   
     
    def validar_receita(self):
        receitaNumerica=[0,0,0,0,0,0]
        for ingrediente in self.ingredientes:
            receitaNumerica[ingrediente.indiceNumerico]=ingrediente.estadoNumerico()
        if tuple(receitaNumerica) in pratos:
            self.receita=pratos[tuple(receitaNumerica)]
        else:
            self.receita="invalido"
        return self.receita
            
    # 
    # busca uma receita com os
    # ingredientes atuais
    # e retorna oq for achado
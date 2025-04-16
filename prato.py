
#Código numérico para relacionar receitas
pratos={((1,),(1,),(0),(0),(0),(0)):"Caponata", ((0),(0),(1,2),(2,),(2,),(0)):"Hamburguer",((0),(0),(0),(2,3),(2,3),(1,2,3)):"Quiche"}
#tomate cebola grao farinha leite brocolis
# Código das receitas (T de tomate, C de cebola... / C de corte, B de bater e A de assar...)
# TCGFLB       C B A  CB CA  ...
# 000000       1 2 3  12 13  ...
# Caponata:   110000
# Hamburguer: 004220
# Quiche :    000667



# Objeto que aceita mistura de ingredientes e extrai receita da combinação
class Prato:
    def __init__(self):
        self.ingredientes = []
        self.receita = ""
        # :ingredientes: lista de ingredientes no prato
        # :receita: nome da receita atual validada (ou vazio se não houver)
    
    def add_ingrediente(self, ingrediente):
        if(len(self.ingredientes)<5):
            self.ingredientes.append(ingrediente)
        else:
            print("Prato cheio! joga no lixo")
    # Adiciona um ingrediente ao prato se esse não estiver cheio
    
    def limpar_comida(self):
        self.ingredientes = []
        self.receita = ""  
    # Esvazia o prato dos ingredientes

    def validar_receita(self):
        receita_Numerica=[(0),(0),(0),(0),(0),(0)]
        for ingrediente in self.ingredientes:
            receita_Numerica[ingrediente.indice_Receita]=ingrediente.estado_Numerico()
        if tuple(receita_Numerica) in pratos:
            self.receita=pratos[tuple(receita_Numerica)]
        else:
            self.receita="invalido"
        return self.receita 
    # Busca uma receita com os ingredientes atuais 
    # no map de pratos possíveis e retonar o que foi achado
    
    def esta_vazio(self):
        return self.ingredientes == []
    # Retorna se o prato esta vazio
            

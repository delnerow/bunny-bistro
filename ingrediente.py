
class Ingrediente:
    def __init__(self, nome, indiceNumerico):
        self.nome=nome
        self.indiceNumerico = indiceNumerico
        self.cortado=False
        self.batido=False
        self.assado=False
    #
    # Um nome para identificar o ingrediente
    # o índice no código carteado de receita
    # bools indicando o estado culinário do ingrediente
    #
    def cortar(self):
        self.cortado= True
    #
    # corta o ingrediente
    #
    
    def bater(self):
        self.batido= True
    #
    # bate o ingrediente
    #
    def assar(self):
        self.assado= True
    #
    # assa o ingrediente
    #
    
    def estadoNumerico(self):
        if(self.cortado):
            if(self.assado):
                if(self.batido):return 7
                else:return 5
            elif(self.batido): return 4
            else: return 1
        else:
            if(self.assado):
                if(self.batido):return 6
                else:return 3
            elif (self.batido): return 2
            else: return -1
    #
    # definindo qual o estado culinário do ingrediente
    # 
    #
class Tomate(Ingrediente):
    def __init__(self):
        super().__init__("Tomate", 0)   
 
class Cebola(Ingrediente):
    def __init__(self):
        super().__init__("Cebola", 1)    

class Grao(Ingrediente):
    def __init__(self):
        super().__init__("Grão de Bico", 2) 
        
class Farinha(Ingrediente):
    def __init__(self):
        super().__init__("Farinha", 3) 
        
class Leite(Ingrediente):
    def __init__(self):
        super().__init__("Leite Vegetal", 4)    
        
class Brocolis(Ingrediente):
    def __init__(self):
        super().__init__("Brócolis", 5) 
        
        
       
from prato import Prato

class Maquina:
    def __init__(self):
        self.prato_atual= Prato()
        self.ocupada=False
    #
    # inicializa uma máqina (superclasse)
    # e desocupada
    # 
    
    def ocupar(self, bandeja):
        if(not self.ocupada):
            if bandeja.ingredientes != []:
                self.prato_atual.ingredientes= bandeja.ingredientes
                bandeja.limpar_comida()
                self.__operar()
            else:
                print("Erro: nada na bandeja")
        else:
            print("Erro: máquina ocupada")
        
    #
    # esvazia ingredientes da bandeja
    # ocupa a máquina
    # começa a operar
    #
    
    def __operar(self):
        if(self.prato_atual.ingredientes != []):
            #lançar minigame
            success = True
            if success:
                self.cook()
            else:
                print("Erro: falhou no minigame")   
                
    # Iniciaria minigame para ver se irá realmente cozinhar
    # e começa a cozinhar
    #
    
    def cook(self):
        
        raise NotImplementedError("Subclasses must implement this method")
    # 
    # Cada subclasse tem o seu próprio
    # dependendo da maquina da cozinha
    #
    
    def free(self, bandeja):
        if bandeja.ingredientes==[] and self.prato_atual.ingredientes !=  []:
            bandeja.ingredientes=self.prato_atual.ingredientes
            self.prato_atual.limpar_comida()
        else:
            print("Erro: bandeja cheia/maquina já vazia")
    #
    # retorna ingredientes à bandeja
    # e se desocupa
    #
class Tabua(Maquina):
    def __init__(self):
        super().__init__()
    def cook(self):
        for i in range(len(self.prato_atual.ingredientes)):
            self.prato_atual.ingredientes[i].cortar()
    #
    # tabua de corte
    # ela corta
    #
               
class Batedeira(Maquina):
    def __init__(self):
        super().__init__()
    def cook(self):
        for i in range(len(self.prato_atual.ingredientes)):
            self.prato_atual.ingredientes[i].bater()
    #
    # batedeira
    # ela bate
    #
class Forno(Maquina):
    def __init__(self):
        super().__init__()
    def cook(self):
        for i in range(len(self.prato_atual.ingredientes)):
            self.prato_atual.ingredientes[i].assar()
    #
    # forno
    # ele assa
    #
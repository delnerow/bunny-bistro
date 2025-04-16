from cliente import Clientes
from ingrediente import Cebola, Tomate, Grao, Brocolis, Leite, Farinha
from maquina import Maquina, Batedeira, Forno, Tabua
from prato import Prato
import os

#a
# 
# USE O DEMOCLICKSPRITE.PY
# 
# Obsoleto, pois imagems foram adicionadas aos objetos
# Não roda
# 
# 
# 
# 
bandeja = Prato()
score=0

carlos = Clientes(0, "Caponata","humano")
jose = Clientes(0, "Caponata","cao")
altair = Clientes(0, "hamburguer","amongus")
beto = Clientes(0, "quiche","don quixote")
balcao =[carlos,jose,altair,beto]

tabua = Tabua()
batedeira = Batedeira()
forno = Forno()

def printCliente():
    print("=====Clientes=====")
    for i in range(len(balcao)):
        c = balcao[i]
        print("[",i,"]",c.especie," esta pedindo ", c.pedido)
def printIngredientes():
    print("=====Prato atual=====")
    for c in bandeja.ingredientes:
        print(c.nome+"("+str(c.estadoNumerico())+")", end='')
        print("")
    print(" = ", bandeja.validar_receita())
while len(balcao)>0:
    os.system('cls')
    print("Score:", score)   
    print("[t] Tábua de Corte")
    print("[b] Batedeira")
    print("[f] Forno")
    print("[n] Novo Prato")
    print("[i] Ingredientes")
    printIngredientes()
    printCliente()
    action = input("o que coelhinho deseja fazer?")
    if action == "t":
        tabua.ocupar(bandeja)
        tabua.desocupar(bandeja)
    elif action == "b":
        batedeira.ocupar(bandeja)
        batedeira.desocupar(bandeja)
    elif action == "f":
        forno.ocupar(bandeja)
        forno.desocupar(bandeja)
    elif action == "n":
        bandeja.limpar_comida()
    elif action == "i":
        print("[1] Tomate")
        print("[2] Cebola")
        print("[3] Brocolis")
        print("[4] Leite Vegetal")
        print("[5] Farinha")
        print("[6] Grão de Bico")
        action = input("o que coelhinho deseja fazer?")
        tomate = Tomate()
        cebola = Cebola()
        brocolis = Brocolis()
        leite = Leite()
        farinha = Farinha()
        grao = Grao()
        conversaofodase={"1":tomate,"2":cebola,"3":brocolis,"4":leite,"5":farinha,"6":grao}
        bandeja.add_ingrediente(conversaofodase[action])
    else:
        score = score + balcao[int(action)].comer(bandeja) 
        del balcao[int(action)]
os.system('cls')
print("boa camarada, conseguiu ", score)
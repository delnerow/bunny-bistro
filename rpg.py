from cliente import Clientes
from maquina import Maquina
from prato import Prato
import os


bandeja = Prato()
score=0

carlos = Clientes(0, "Caponata","humano")
jose = Clientes(0, "Caponata","cao")
altair = Clientes(0, "hamburguer","amongus")
beto = Clientes(0, "quiche","don quixote")
balcao =[carlos,jose,altair,beto]

tabua = Maquina("tabua")
batedeira = Maquina("batedeira")
forno = Maquina("forno")

def printCliente():
    print("=====Clientes=====")
    for i in range(len(balcao)):
        c = balcao[i]
        print("[",i,"]",c.especie," esta pedindo ", c.pedido)
def printIngredientes():
    print("=====Prato atual=====")
    for c in bandeja.ingredientes:
        print(c, end='')
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
    print("[b] Atender balcão")
    printIngredientes()
    printCliente()
    action = input("o que coelhinho deseja fazer?")
    if action == "t":
        tabua.ocupar(bandeja)
        tabua.cook()
        tabua.free(bandeja)
        
    elif action == "b":
        batedeira.ocupar(bandeja)
        batedeira.cook()
        batedeira.free(bandeja)
    elif action == "f":
        forno.ocupar(bandeja)
        forno.cook()
        forno.free(bandeja)
    elif action == "n":
        bandeja = Prato()
    elif action == "i":
        print("[1] Tomate")
        print("[2] Cebola")
        print("[3] Brocolis")
        print("[4] Leite Vegetal")
        print("[5] Farinha")
        print("[6] Grão de Bico")
        action = input("o que coelhinho deseja fazer?")
        conversaofodase={"1":"tomate","2":"cebola","3":"brocolis","4":"leite","5":"farinha","6":"grao"}
        bandeja.add_ingrediente(conversaofodase[action])
    else:
        score = score + balcao[int(action)].comer(bandeja) 
        del balcao[int(action)]
os.system('cls')
print("boa camara, conseguiu ", score)
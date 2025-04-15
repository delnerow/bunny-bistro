import pygame
import random

from cliente import Cliente

class ClienteSpawner:
    def __init__(self,gc, fila, taxa_chegada):
        self.gc=gc
        self.fila = fila
        self.taxa = taxa_chegada  # λ = clientes por segundo
        self.tempo_proximo_cliente = pygame.time.get_ticks() + self._gerar_intervalo()

    def _gerar_intervalo(self):
        # Tempo entre clientes em ms
        intervalo_segundos = random.expovariate(self.taxa)
        return int(intervalo_segundos * 1000)

    def update(self):
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual >= self.tempo_proximo_cliente:
            self.spawn_cliente()
            self.tempo_proximo_cliente = tempo_atual + self._gerar_intervalo()

    def spawn_cliente(self):
        print("Novo cliente chegou!")
        # Aqui você criaria um cliente real e colocaria na fila
        paciencias =(20,30,40)
        pedidos=("Caponata", "Hamburguer","Quiche")
        especies=("humano","cao","gato")
        cliente = Cliente(self.cg,0,0,random.choice(paciencias),random.choice(pedidos),random.choice(especies),self.fila)
        self.fila.entra_cliente(cliente)


import pygame
import random

from cliente import Cliente

# Gerenciador de spawn de clientes aleatórios baseado em uma taxa de chegada (Poisson)
class ClienteSpawner:
    def __init__(self,gc, fila, taxa_chegada):
        self.gc=gc
        self.fila = fila
        self.taxa = taxa_chegada  
        self.tempo_proximo_cliente = pygame.time.get_ticks() + self._gerar_intervalo()
        # :gc:                     GameController, para acessar contexto geral do jogo
        # :fila:                   Referência à fila de clientes
        # :taxa:                   Taxa lambda para distribuição de chegadas (clientes por segundo)
        # :tempo_proximo_cliente:  Timestamp do próximo cliente a ser gerado (em ms)
    
    def _gerar_intervalo(self):
        intervalo_segundos = random.expovariate(self.taxa)
        return int(intervalo_segundos * 1000)
        # Converte o intervalo de segundos para milissegundos, para alinhar com o pygame.time.get_ticks()

    def update(self):
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual >= self.tempo_proximo_cliente:
            self.spawn_cliente()
            self.tempo_proximo_cliente = tempo_atual + self._gerar_intervalo()
        # Checa se o tempo atual ultrapassou o tempo de spawn do próximo 
        # cliente. Caso sim, cria um cliente e define o próximo 
        # intervalo de spawn

    def spawn_cliente(self):
        # Se a fila não estiver cheia, instancia um novo cliente e adiciona à fila
        if(not self.fila.cheia()):
            paciencias =(15,20,30)
            pedidos=("Caponata", "Hamburguer","Quiche")
            especies=("lady","bode","galinha","gato","macaco","morcego","porco","touro","vaca")
            
            cliente = Cliente(self.gc,0,0,random.choice(paciencias),random.choice(pedidos),random.choice(especies),self.fila)
            
            # Adiciona o cliente criado na fila
            self.fila.entra_cliente(cliente)


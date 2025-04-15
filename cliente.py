pedidos={"Caponata":"images\pratos\caponata.png", "Hamburguer":"images\pratos\hamburguer.png","Quiche":"images\pratos\quiche.png"}

import pygame
from ClickSprite import ClickableSprite
from prato import Prato


def get_image(sheet, width, height, scale, colour, position):
    image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
    image.blit(sheet, (0, 0), (width * position[0], height * position[1], width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    if colour is not None:
        image.set_colorkey(colour)
    return image
    # Retira uma fração de uma imagem maior (spritesheet) para utilizar
    # como sprite animados


# Objeto Cliente, pede comida numa fila e pode se sentar numa mesa
class Cliente(ClickableSprite):
    def __init__(self,gc,x,y,paciencia, pedido, especie,fila):
        self.fila=fila
        self.tempo_entrada = pygame.time.get_ticks()
        self.pedido = pedido
        self.especie = especie
        self.paciencia = paciencia
        self.tempo_alerta=10
        self.cadeira=None
        self.inicio_comer=0
        self.__score=0
        self.gc=gc
        self.x=x
        self.y=y
        # :fila:            Fila que armazena o cliente 
        # :tempo_entrada:   Timestamp em que ele entrou
        # :pedido:          Pedido que precisa ser preparado 
        # :especie:         Especie da arte do sprite 
        # :paciencia:       Paciencia, quantos segundos até desistir do pedido  
        # :tempo_alerta:    Ultimos segundos da paciencia, onde o balão de pedido fica vermelho
        # :cadeira:         Cadeira que ele estiver sentado
        # :inicio_comer:    Timestamp em que ele se sentou numa mesa
        # :score:           O score do prato, 0 ou 100
        # :gc:              GameController para acessar prato e score 
        # :x:               Posição x do cliente 
        # :y:               Posição y do cliente
    
        self.servido=False
        self.servido_certo=False
        self.comido=False
        self.virar=False
        # Se o cliente foi servido, com qualquer coisa ou não
        # Se o cliente foi servido com o pedido certo 
        # Se o cliente servido certo já terminou de comer na mesa 
        # Se a cadeira exige que o cliente vire pra direita

        diretorio = especie+".png"
        self.image = pygame.image.load("images\clientes\\"+diretorio).convert_alpha()
        self.skinVector = [get_image(self.image, 27, 30, 3, None, (i, 0)) for i in range(2)]
        self.skin = self.skinVector[0]
        self.frame = 0
        # Carregar caminho da imagem com base na especie
        # vetor de sprites vindo da spritesheet imagem (2 frames para cliente)
        # Inicializar uma skin
        # Frame organiza a animação da spritesheet
        
        self.balao_image = pygame.image.load("images/balao.png").convert_alpha()  # carrega a imagem do balão
        self.balao_image = pygame.transform.scale_by(self.balao_image, 2)
        self.balao_offset = pygame.Vector2(-30, -70)
        # Carregar imagem do balão de pedido e dimensionar
        # Offset do cliente, na diagonal esquerda
        
        self.pedido_image = pygame.image.load(pedidos[pedido]).convert_alpha()  # carrega a imagem do balão
        self.pedido_image = pygame.transform.scale_by(self.pedido_image, 1.5)
        self.pedido_offset = pygame.Vector2(-28, -70)
        # Carregar imagem do pedido e dimensionar
        # Offset do cliente, na diagonal esquerda
        
        super().__init__(self.skin, x, y,self.comer)
        # Chamada pra construir ClickableSprite, com callback de comer()

    def comer(self):
        if(not self.servido):
            prato = self.gc.player.prato
            if(prato):
                self.servido=True
                if(self.pedido == prato.validar_receita()):
                    self.servido_certo=True
                    self.__score=100
                else:
                    self.__score=0
                prato.ingredientes = []
                self.gc.player.prato = None
                self.gc.level.score= self.gc.level.score+self.satisfacao()
                self.fila.sai_cliente(self)

    # Só come se não estiver servido e se existir um prato com o coelinho
    # Se for verdade, então o cliente está servido
    # Se o prato corresponder com seu pedido, 
    # ele foi servido certo e o score é 100
    # Caso não seja, o score é 0
    # Sempre que comer o cliente zera o prato do player
    # atualiza o score atual e sai da fila

    
    
    def satisfacao(self):
        return self.__score
    # Retornar qualidade do prato
 
    def update(self, events):
        tempo_percorrido= (pygame.time.get_ticks()-self.tempo_entrada)/1000
        if not self.servido and tempo_percorrido >= self.paciencia:
            print("restaurante de bosta!")
            self.servido=True
            self.comido=True
            self.fila.sai_cliente(self)
        # Calcula se o tempo já passou da paciencia do cliente 
        # e remove ele da fila caso seja

        super().update(events)
        if(self.virar):
            self.skinVector = [pygame.transform.flip(frame, True, False) for frame in self.skinVector]
            self.skin=self.skinVector[1]
            self.virar=False  
        # Espelhar horizontalmente o lado do cliente( padrão é esquerdo ) caso esteja numa cadeira esquerda
        
        self.frame += 1             
        if self.frame == 40:
            self.skin = self.skinVector[1]
            self.image = self.skin
        elif self.frame == 80:
            self.skin = self.skinVector[0]
            self.image = self.skin
            self.frame = 0
        # Atualiza a posição do cliente na tela
        # A cada 10 frames, muda a imagem do cliente
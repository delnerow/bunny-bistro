import pygame

# Sprite acionável ao passar o mouse nele
class HoverSprite(pygame.sprite.Sprite):
    def __init__(self,image,x,y,callback, exit_callback):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.rect.x = x
        self.rect.y = y
        self.callback = callback
        self.exit_callback = exit_callback
        self.hovering = False  # Tracks hover state from previous frame
        # Inicializa imagem do sprite e seu collider 
        # além de função de callback para entrada do Hover e 
        # callback para saída do Hover 
        # O bool hovering indica se o mouse se encontra no collider

    def is_mouse_over(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    # Retorna se o mouse está no collider da imagem
    
    def update(self,events):
        mouse_pos = pygame.mouse.get_pos()
        is_hovering_now = self.is_mouse_over(mouse_pos)

        if is_hovering_now and not self.hovering:
            self.hovering = True
            self.callback()
            
        elif not is_hovering_now and self.hovering:
            self.hovering = False  
            if(self.exit_callback()):   
                self.exit_callback()
    # Atualiza se o mouse está no collider 
    # se sim nesse exato instante hovering_now é True, 
    # e se já não alteramos hovering, hovering é True e chamamos uma vez callback. 
    # Se num exato instante hovering_now deixa de ser True, 
    # mas hovering é True então o mouse acaba de deixar o collider 
    # e hovering é False e chamamos callback de saida
    
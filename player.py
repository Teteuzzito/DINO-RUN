
import pygame

class Player:
    def __init__(self, x, y):
        self.dino_normal = [
            pygame.transform.scale(pygame.image.load('assets/dino1.png').convert_alpha(), (60, 60)),
            pygame.transform.scale(pygame.image.load('assets/dino2.png').convert_alpha(), (60, 60)),
        ]
        self.dino_invertido = [
            pygame.transform.scale(pygame.image.load('assets/dino_inverted1.png').convert_alpha(), (60, 60)),
            pygame.transform.scale(pygame.image.load('assets/dino_inverted2.png').convert_alpha(), (60, 60)),
        ]
        
        self.imagens_atuais = self.dino_normal
        self.indice_imagem = 0
        self.imagem = self.imagens_atuais[self.indice_imagem]
        
        self.retangulo = self.imagem.get_rect(center=(x, y))

    def draw(self, tela):
        tela.blit(self.imagem, self.retangulo)

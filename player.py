
import pygame

class Player:
    def __init__(self, x, y):
        self.imagem = pygame.image.load("assets/dino1.png").convert_alpha()
        self.retangulo = self.imagem.get_rect(center=(x, y))

    def draw(self, tela):
        tela.blit(self.imagem, self.retangulo)

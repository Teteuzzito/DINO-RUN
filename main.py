
import pygame
import sys
from config import *

pygame.init()
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption(TITULO)

relogio = pygame.time.Clock()
rodando = True


def menu_principal():
    while True:
        janela.fill((0, 0, 0))
        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    return
menu_principal()

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    janela.fill((255, 255, 255))  
    pygame.display.update()
    relogio.tick(FPS)

pygame.quit()
sys.exit()


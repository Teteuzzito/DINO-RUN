# main.py
import pygame
import sys
from config import *

pygame.init()
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption(TITULO)

relogio = pygame.time.Clock()
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    janela.fill((255, 255, 255))  # Fundo branco temporário
    pygame.display.update()
    relogio.tick(FPS)

pygame.quit()
sys.exit()


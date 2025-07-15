
import pygame
import sys
from config import *
from player import Player

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

player = Player(LARGURA // 2, ALTURA - 100)

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    janela.fill((255, 255, 255))  
    pygame.display.update()
    relogio.tick(FPS)
    player.draw(janela)


pygame.quit()
sys.exit()


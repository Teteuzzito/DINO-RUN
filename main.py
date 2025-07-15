import pygame
import sys
from config import *
from player import Player
from obstaculo import Obstaculo

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('assets/sounds/musica_jogo.wav')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

musica_jogo = 'assets/sounds/musica_jogo.wav'

janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption(TITULO)
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont(nome_fonte, tamanho_fonte)

tela_inicio = pygame.image.load('assets/start.png').convert()
tela_gameover = pygame.image.load('assets/game-over.png').convert()

def menu_principal():
    while True:
        janela.blit(tela_inicio, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load(musica_jogo)
                    pygame.mixer.music.set_volume(0.1)
                    pygame.mixer.music.play(-1)
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
menu_principal()

pontuacao = 0
player = Player(LARGURA // 2, ALTURA - 100)
obstaculos = []

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    janela.fill((255, 255, 255))  
    pygame.display.update()
    relogio.tick(FPS)
    player.draw(janela)


pygame.quit()
sys.exit()


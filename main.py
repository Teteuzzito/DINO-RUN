import pygame
import sys
import random
from config import *
from player import Player
from obstaculo import Obstaculo
from dados_manager import carregarPontuacao, salvarRecorde

pygame.init()
pygame.mixer.init()

# SONS / MÚSICA
pygame.mixer.music.load('assets/sounds/musica_jogo.wav')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

som_pulo = pygame.mixer.Sound('assets/sounds/som_pulo.wav')
musica_jogo = 'assets/sounds/musica_jogo.wav'
musica_gameover = 'assets/sounds/musica_gameover.wav'
som_explosao = pygame.mixer.Sound('assets/sounds/explosao.wav')

def modo_cor(pontuacao):
    if (pontuacao // 5000) % 2 == 0:
        return {'fundo': branco, 'texto': preto}
    else:
        return {'fundo': preto, 'texto': branco}

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
recorde = carregarPontuacao()
player = Player(LARGURA // 2, ALTURA - 100)
obstaculos = []
tempo_obstaculos = 0

Obstaculo.carregar_imagem()

rodando = True
while rodando:
    dt = relogio.tick(fps) / 1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    player.velocidade_animacao = velocidade_inicial_obstaculo / 200
    player.update(dt)
    
    tempo_obstaculos += dt
    if tempo_obstaculos >= intervalo_spawn_obstaculo:
        x = random.randint(50, LARGURA - 50)
        modo_invertido = (pontuacao // 5000) % 2 == 1
        obstaculos.append(Obstaculo(x, -40, velocidade_inicial_obstaculo, invertido=modo_invertido))
        tempo_obstaculos = 0
        
    if pontuacao >0 and pontuacao % 1000 == 0:
        velocidade_inicial_obstaculo += 15

    janela.fill((255, 255, 255))  
    pygame.display.update()
    relogio.tick(fps)
    player.draw(janela)


pygame.quit()
sys.exit()


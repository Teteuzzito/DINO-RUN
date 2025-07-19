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

def tela_gameover():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(musica_gameover)
    pygame.mixer.music.play()
    while True:
        janela.blit(tela_gameover, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                if event.key == pygame.K_ESCAPE:
                    return False

def tela_explosao():
    pygame.mixer.music.stop()
    som_explosao.play()
    fonte = pygame.font.SysFont(nome_fonte, 36)
    pequeno = pygame.font.SysFont(nome_fonte, tamanho_fonte)
    texto = fonte.render('EXTINCÃO DOS DINOSSAUROS!', True, cor_explosao)
    mensagem = pequeno.render('VOCÊ ZEROU O JOGO! Parabéns!', False, branco)
    for _ in range(60):
        janela.fill((random.randint(200, 255), random.randint(50, 100), 0))
        janela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, ALTURA // 2 - 40))
        janela.blit(mensagem, (LARGURA // 2 - mensagem.get_width() // 2, ALTURA // 2 + 10))
        pygame.display.update()
        pygame.time.delay(16)

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
player = Player(LARGURA // 2, ALTURA - 200, som_pulo = som_pulo)
obstaculos = []
tempo_obstaculos = 0

Obstaculo.carregar_imagem()

rodando = True
while rodando:
    dt = relogio.tick(FPS) / 1000
    
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
        
    for obs in obstaculos[:]:
        obs.update(dt)
        if obs.fora_tela(ALTURA):
            obstaculos.remove(obs)
        elif obs.retangulo.colliderect(player.retangulo) and player.no_chao():
            salvarRecorde(recorde)
            if tela_gameover():
                pontuacao = 0
                player = Player(LARGURA // 2, ALTURA - 100, som_pulo = som_pulo)
                obstaculos = []
                tempo_obstaculos = 0
                velocidade_inicial_obstaculo = 200
                indice_dino = 0
                tempo_animacao = 0
                pygame.mixer.music.load(musica_jogo)
                pygame.mixer.music.play(-1)
                continue
            else:
                rodando = False
        
    pontuacao += 1
    if pontuacao > recorde:
        recorde = pontuacao
    
    if pontuacao >= pontuacao_maxima:
        salvarRecorde(recorde)
        tela_explosao()
        rodando = False
        
    cores = modo_cor(pontuacao)
    janela.fill(cores['fundo'])
    
    for obs in obstaculos:
        obs.draw(janela)
    
    modo_invertido = (pontuacao // 5000) % 2 == 1
    player.set_mode(invertido=modo_invertido)
    
    player.draw(janela)
    
    texto_pontuacao = fonte.render(f'Recorde: {recorde}', True, cores['texto'])
    texto_recorde = fonte.render(f'Recorde: {recorde}', True, cores['texto'])
    janela.blit(texto_pontuacao, (10, 10))
    janela.blit(texto_recorde, (10, 40))
    
    pygame.display.update()

pygame.quit()
sys.exit()
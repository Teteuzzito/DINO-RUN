
import pygame
from config import LARGURA

class Player:
    def _init_(self, x, y, som_pulo=None):
        self.som_pulo = som_pulo
        
        self.dino_normal = [
            pygame.transform.scale(pygame.image.load("assets/dino1.png").convert_alpha(), (60, 60)),
            pygame.transform.scale(pygame.image.load("assets/dino2.png").convert_alpha(), (60, 60)),
        ]
        self.dino_invertido = [
            pygame.transform.scale(pygame.image.load("assets/dino_inverted1.png").convert_alpha(), (60, 60)),
            pygame.transform.scale(pygame.image.load("assets/dino_inverted2.png").convert_alpha(), (60, 60)),
        ]

        self.imagens_atuais = self.dino_normal
        self.indice_imagem = 0
        self.imagem = self.imagens_atuais[self.indice_imagem]

        self.y_base = y
        self.deslocamento_y = 0
        self.retangulo = self.imagem.get_rect(center=(x, y))

        self.speed = 500
        self.pulando = False
        self.velocidade_pulo = 0
        self.gravidade = 1000
        self.forca_pulo = 500

        self.tempo_animacao = 0
        self.intervalo_base_animacao = 0.5
        self.velocidade_animacao = 1.0  # padrão

    def update(self, dt):
        keys = pygame.key.get_pressed()
        deslocamento_x = 0

        # MOVIMENTAÇÃO
        if keys[pygame.K_a]:
            deslocamento_x -= self.speed * dt
        if keys[pygame.K_d]:
            deslocamento_x += self.speed * dt

        # PULO
        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and not self.pulando:
            self.pulando = True
            self.velocidade_pulo = -self.forca_pulo
            if self.som_pulo:
                self.som_pulo.play()

        # LÓGICA PULO
        if self.pulando:
            self.velocidade_pulo += self.gravidade * dt
            self.deslocamento_y += self.velocidade_pulo * dt
            if self.deslocamento_y > 0:
                self.deslocamento_y = 0
                self.pulando = False

        self.retangulo.x += int(deslocamento_x)

        # LIMITAR TELA
        if self.retangulo.left < 0:
            self.retangulo.left = 0
        if self.retangulo.right > LARGURA:
            self.retangulo.right = LARGURA
        self.retangulo.y = int(self.y_base + self.deslocamento_y)

        # ANIMAÇÃO
        self.tempo_animacao += dt
        intervalo = max(0.1, self.intervalo_base_animacao / self.velocidade_animacao)
        if self.tempo_animacao >= intervalo:
            self.indice_imagem = (self.indice_imagem + 1) % len(self.imagens_atuais)
            self.imagem = self.imagens_atuais[self.indice_imagem]
            self.tempo_animacao = 0

    def draw(self, tela):
        tela.blit(self.imagem, self.retangulo)

    def no_chao(self):
        return self.deslocamento_y >= 0

    def set_mode(self, invertido=False):
        imagens_novas = self.dino_invertido if invertido else self.dino_normal
        if imagens_novas != self.imagens_atuais:
            self.imagens_atuais = imagens_novas
            self.indice_imagem = 0
            self.tempo_animacao = 0
        self.imagem = self.imagens_atuais[self.indice_imagem]
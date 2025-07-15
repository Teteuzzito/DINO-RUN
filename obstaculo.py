import pygame
import random

class Obstaculo:
  cacto_normal = []
  cacto_invertido = []
  
  def carregar_imagem():
    Obstaculo.cacto_normal = [
      pygame.transform.scale(pygame.image.load('assets/cactus1.png').convert_alpha(), (30, 50)),
      pygame.transform.scale(pygame.image.load('assets/cactus2.png').convert_alpha(), (50, 50)),
      pygame.transform.scale(pygame.image.load('assets/cactus3.png').convert_alpha(), (70, 50)),
    ]
    Obstaculo.cacto_invertido = [
      pygame.transform.scale(pygame.image.load('assets/cactus1_inverted.png').convert_alpha(), (30, 50)),
      pygame.transform.scale(pygame.image.load('assets/cactus2_inverted.png').convert_alpha(), (50, 50)),
      pygame.transform.scale(pygame.image.load('assets/cactus3_inverted.png').convert_alpha(), (70, 50)),
    ]
    
  def __init__(self, x, y, speed, invertido=False):
    if not self.cacto_normal:
      self.carregar_imagem()
    imagens = self.cactp_invertido if invertido else self.cacto_normal
    self.imagem = random.choice(imagens)
    self.retangulo = self.imagem.get_rect(center = (x, y))
    self.speed = speed
    
  def update(self, dt):
    self.retangulo.y += int(self.speed * dt)
    
  def draw(self, tela):
    tela.blit(self.imagem, self.retangulo)
import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo de Corrida com Carro Quadrado")

# Cores
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Carro do jogador (representado por um quadrado)
carro_largura = 50
carro_altura = 100
carro_x = largura_tela // 2 - carro_largura // 2
carro_y = altura_tela - carro_altura - 20
carro_velocidade = 5

# Oponentes (também quadrados)
oponente_largura = 50
oponente_altura = 100
oponente_x = random.randint(0, largura_tela - oponente_largura)
oponente_y = random.randint(-altura_tela, 0)
oponente_velocidade = 3

# Função para desenhar o carro
def desenhar_carro(x, y):
    pygame.draw.rect(tela, vermelho, (x, y, carro_largura, carro_altura))

# Função para desenhar o oponente
def desenhar_oponente(x, y):
    pygame.draw.rect(tela, branco, (x, y, oponente_largura, oponente_altura))

# Loop principal do jogo
jogo_ativo = True
while jogo_ativo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo_ativo = False

    # Controles do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and carro_x > 0:
        carro_x -= carro_velocidade
    if teclas[pygame.K_RIGHT] and carro_x < largura_tela - carro_largura:
        carro_x += carro_velocidade

    # Movimento do oponente
    oponente_y += oponente_velocidade
    if oponente_y > altura_tela:
        oponente_x = random.randint(0, largura_tela - oponente_largura)
        oponente_y = random.randint(-altura_tela, 0)

    # Verifica colisões
    if carro_x + carro_largura > oponente_x and carro_x < oponente_x + oponente_largura:
        if carro_y < oponente_y + oponente_altura and carro_y + carro_altura > oponente_y:
            jogo_ativo = False

    # Preenche a tela
    tela.fill(branco)

    # Desenha o jogador e o oponente
    desenhar_carro(carro_x, carro_y)
    desenhar_oponente(oponente_x, oponente_y)

    # Atualiza a tela
    pygame.display.update()

# Encerra o Pygame
# Encerra o Pygame
pygame.quit()

import pygame
pygame.init()

tamanho_tela = (650, 650)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Brick Breaker")

cores = {
    "branca": (255, 255, 255),
    "preta": (0, 0, 0),
    "azul": (0, 0, 255),
    "verde": (0, 255, 0),
    "vermelha": (255, 0, 0),
    "amarela": (255, 255, 0)
}

tamanho_bola = 15
bola = pygame.Rect(300, 300, tamanho_bola, tamanho_bola)

tamanho_jogador = 100
jogador = pygame.Rect(275, 630, tamanho_jogador, 15)

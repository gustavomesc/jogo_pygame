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

qtde_blocos_linha = 8
qtde_linhas_blocos = 5
qtde_total_blocos = qtde_blocos_linha * qtde_linhas_blocos

def criar_blocos():
    largura_tela = tamanho_tela[0]
    distancia_entre_blocos = 5
    largura_bloco = (largura_tela - (qtde_blocos_linha + 1) * distancia_entre_blocos) / qtde_blocos_linha
    altura_bloco = 15
    distancia_entre_linhas = altura_bloco + 10

    blocos = []
    for j in range(qtde_linhas_blocos):
        for i in range(qtde_blocos_linha):
            bloco = pygame.Rect(
                i * (largura_bloco + distancia_entre_blocos) + distancia_entre_blocos,
                j * distancia_entre_linhas + distancia_entre_blocos,
                largura_bloco,
                altura_bloco
            )
            blocos.append(bloco)
    return blocos


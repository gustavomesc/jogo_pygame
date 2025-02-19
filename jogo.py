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

def desenhar_texto(texto, tamanho, cor, y):
    fonte = pygame.font.Font(None, tamanho)
    texto_renderizado = fonte.render(texto, True, cor)
    texto_rect = texto_renderizado.get_rect(center=(tamanho_tela[0] // 2, y))
    tela.blit(texto_renderizado, texto_rect)

def tela_inicial():
    while True:
        tela.fill(cores["preta"])
        desenhar_texto("Brick Breaker", 64, cores["branca"], 200)
        desenhar_texto("Pressione F para Fácil ou D para Difícil", 36, cores["branca"], 400)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_f:
                    return "facil"
                if evento.key == pygame.K_d:
                    return "dificil"

        pygame.display.flip()

def tela_vitoria():
    while True:
        tela.fill(cores["preta"])
        desenhar_texto("Você Venceu!", 64, cores["verde"], 300)
        desenhar_texto("Pressione ESPAÇO para voltar ao menu", 36, cores["branca"], 400)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    return

        pygame.display.flip()

def tela_derrota():
    while True:
        tela.fill(cores["preta"])
        desenhar_texto("Você Perdeu!", 64, cores["vermelha"], 300)
        desenhar_texto("Pressione ESPAÇO para voltar ao menu", 36, cores["branca"], 400)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    return

        pygame.display.flip()

def jogo_principal(modo):
    blocos = criar_blocos()
    movimento_bola = [5, -5]
    vidas = 3 if modo == "facil" else 0
    clock = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if (jogador.x + tamanho_jogador) < tamanho_tela[0]:
                jogador.x += 5
        if keys[pygame.K_LEFT]:
            if jogador.x > 0:
                jogador.x -= 5

        bola.x += movimento_bola[0]
        bola.y += movimento_bola[1]


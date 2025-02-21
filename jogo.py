import pygame
import random

pygame.init()
pygame.mixer.init()


def iniciar_musica():
    pygame.mixer.music.load('musica_fundo.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1, 0.0)  

def iniciar_musica_derrota():
    pygame.mixer.music.load('musica_derrota.mp3')  
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1, 0.0)  

def iniciar_musica_tela_inicial():
    pygame.mixer.music.load('musica_tela_inicial.mp3')  # Música da tela inicial
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1, 0.0)  # Loop infinito a partir de 0.0 segundos

# Função para iniciar a música de vitória
def iniciar_musica_vitoria():
    pygame.mixer.music.load('musica_vitoria.mp3')  # Música de vitória
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(0, 0.0)  # Toca uma vez, sem loop

tamanho_tela = (650, 650)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Brick Breaker")

cores = {
    "branca": (255, 255, 255),
    "preta": (0, 0, 0),
    "azul": (0, 0, 255),
    "verde": (0, 255, 0),
    "vermelha": (255, 0, 0),
    "amarela": (255, 255, 0),
    "roxo": (128, 0, 128),
    "Rosa":(255, 192, 203)
}

tamanho_bola = 15
bola = pygame.Rect(300, 300, tamanho_bola, tamanho_bola)

tamanho_jogador = 100
jogador = pygame.Rect(275, 630, tamanho_jogador, 15)

qtde_blocos_linha = 8
qtde_linhas_blocos = 5
qtde_total_blocos = qtde_blocos_linha * qtde_linhas_blocos

PODERES = {
    "aumentar_jogador": {"cor": cores["roxo"], "duracao": 5000},  
    "diminuir_jogador": {"cor": cores["vermelha"], "duracao": 5000},
    "aumentar_velocidade": {"cor": cores["amarela"], "duracao": 5000},
    "vida_extra": {"cor": cores["Rosa"], "duracao": 0} 
}

blocos_especiais = []

def criar_blocos():
    largura_tela = tamanho_tela[0]
    distancia_entre_blocos = 5
    largura_bloco = (largura_tela - (qtde_blocos_linha + 1) * distancia_entre_blocos) / qtde_blocos_linha
    altura_bloco = 15
    distancia_entre_linhas = altura_bloco + 10

    blocos = []
    for j in range(qtde_linhas_blocos):
        for i in range(qtde_blocos_linha):
            bloco_rect = pygame.Rect(
                i * (largura_bloco + distancia_entre_blocos) + distancia_entre_blocos,
                j * distancia_entre_linhas + distancia_entre_blocos,
                largura_bloco,
                altura_bloco
            )

            if random.random() < 0.2:
                poder = random.choice(list(PODERES.keys()))
                bloco = {
                    "rect": bloco_rect,
                    "cor": PODERES[poder]["cor"],
                    "poder": poder
                }
                blocos_especiais.append(bloco)
            else:
                bloco = {
                    "rect": bloco_rect,
                    "cor": cores["verde"],
                    "poder": None
                }
            blocos.append(bloco)
    return blocos

def desenhar_texto(texto, tamanho, cor, y):
    fonte = pygame.font.Font(None, tamanho)
    texto_renderizado = fonte.render(texto, True, cor)
    texto_rect = texto_renderizado.get_rect(center=(tamanho_tela[0] // 2, y))
    tela.blit(texto_renderizado, texto_rect)

def tela_inicial():
    iniciar_musica_tela_inicial()
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
    iniciar_musica_vitoria()
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
    iniciar_musica_derrota()
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
    vidas = 3 if modo == "facil" else 1 
    clock = pygame.time.Clock()

    poder_ativo = None
    tempo_poder = 0
    iniciar_musica()

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

        if bola.x <= 0 or bola.x + tamanho_bola >= tamanho_tela[0]:
            movimento_bola[0] = -movimento_bola[0]
        if bola.y <= 0:
            movimento_bola[1] = -movimento_bola[1]
        if bola.y + tamanho_bola >= tamanho_tela[1]:
            vidas -= 1
            if vidas <= 0:
                tela_derrota()
                return
            else:
                bola.x, bola.y = 300, 200 

        if jogador.colliderect(bola):
            movimento_bola[1] = -movimento_bola[1]

        for bloco in blocos[:]:
            if bloco["rect"].colliderect(bola):
                blocos.remove(bloco)
                movimento_bola[1] = -movimento_bola[1]

                if bloco["poder"]:
                    poder_ativo = bloco["poder"]
                    tempo_poder = pygame.time.get_ticks() + PODERES[poder_ativo]["duracao"]
                    if poder_ativo == "aumentar_jogador":
                        jogador.width *= 2
                    elif poder_ativo == "diminuir_jogador":
                        jogador.width /= 2
                    elif poder_ativo == "aumentar_velocidade":
                        movimento_bola[0] *= 1.5
                        movimento_bola[1] *= 1.5
                    elif poder_ativo == "vida_extra":
                        vidas += 1  
                break

        if poder_ativo and pygame.time.get_ticks() > tempo_poder:
            if poder_ativo == "aumentar_jogador":
                jogador.width = tamanho_jogador
            elif poder_ativo == "diminuir_jogador":
                jogador.width = tamanho_jogador
            elif poder_ativo == "aumentar_velocidade":
                movimento_bola[0] /= 1.5
                movimento_bola[1] /= 1.5
            poder_ativo = None

        if len(blocos) == 0:
            tela_vitoria()
            return

        tela.fill(cores["preta"])
        pygame.draw.rect(tela, cores["azul"], jogador)
        pygame.draw.rect(tela, cores["branca"], bola)
        for bloco in blocos:
            pygame.draw.rect(tela, bloco["cor"], bloco["rect"])

        desenhar_texto(f"Vidas: {vidas}", 36, cores["amarela"], 620)

        pygame.display.flip()
        clock.tick(60)

while True:
    modo = tela_inicial()
    jogo_principal(modo)
    tamanho_jogador = 100 #ainda tem que ajustar o tamanho de um jogo para outro

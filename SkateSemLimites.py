import sys, pygame
from pygame.locals import *
from random import *

# Inicializa a biblioteca pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Carregar a imagem de fundo
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (screen_width, screen_height * 2))

# Variáveis para o movimento do fundo
background_y = 0
background_speed = 5

# Define um título para a janela
pygame.display.set_caption("Tela Principal")

# Define as cores em RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Declarando a fonte do placar e variável contadora
font = pygame.font.SysFont('sans', 40)
placar = 0

# Variável para contagem de tempo, utilizado para controlar a velocidade de quadros
clock = pygame.time.Clock()

# Criando objeto Clock
CLOCKTICK = pygame.USEREVENT + 1
pygame.time.set_timer(CLOCKTICK, 1000)
temporizador = 60

# Carrega a imagem do personagem e define sua posição inicial
player_image = pygame.image.load('character.png')  # Substitua pelo caminho da imagem do personagem
player_image = pygame.transform.scale(player_image, (50, 50))  # Redimensiona se necessário
player_x = screen_width // 2  # Começa no centro horizontal da tela
player_y = screen_height - 80  # Posiciona próximo à parte inferior da tela
player_speed = 10  # Velocidade de movimento do personagem

# Função do menu principal
def menu():
    menu_font = pygame.font.SysFont('sans', 50)
    start_text = menu_font.render("Pressione ENTER para iniciar", True, WHITE)
    
    while True:
        screen.fill(BLACK)
        
        # Desenha o texto do menu
        screen.blit(start_text, (screen_width / 2 - start_text.get_width() / 2, screen_height / 2 - start_text.get_height() / 2))
        
        pygame.display.flip()
        
        # Verifica eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Inicia o jogo ao pressionar Enter
                    return  # Sai da função menu e começa o jogo

# Chama a tela de menu antes do loop principal do jogo
menu()

# Loop principal do jogo
while temporizador > 0:  # O loop roda enquanto o temporizador não acaba
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == CLOCKTICK:
            temporizador -= 1

    # Movimento do fundo
    background_y -= background_speed
    if background_y <= -screen_height:
        background_y = 0

    # Movimento do personagem com limite de bordas
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[K_RIGHT] and player_x < screen_width - player_image.get_width():
        player_x += player_speed

    # Desenha o fundo
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y + screen_height))

    # Desenha o personagem
    screen.blit(player_image, (player_x, player_y))

    # Renderizando as fontes do placar e do cronômetro na tela
    score1 = font.render('Placar ' + str(placar), True, WHITE)
    screen.blit(score1, (600, 50))

    timer1 = font.render('Tempo ' + str(temporizador), True, YELLOW)
    screen.blit(timer1, (50, 50))

    # Atualiza a tela visível ao usuário
    pygame.display.flip()

    # Limita a taxa de quadros a 60 fps
    clock.tick(60)

# Final de jogo - Exibe a mensagem final após o fim do temporizador
screen.fill(BLACK)
textofinal = font.render('Fim de Jogo - Placar final: ' + str(placar), True, RED)
screen.blit(textofinal, (screen_width / 2 - textofinal.get_width() / 2, screen_height / 2 - textofinal.get_height() / 2))

# Atualiza a tela com a mensagem final
pygame.display.flip()

# Pequeno loop para aguardar o encerramento
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
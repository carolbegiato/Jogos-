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
background = pygame.transform.scale(background, (screen_width * 2, screen_height))  # Redimensiona a imagem para cobrir o dobro da largura da tela

#Atualizado
#background = pygame.transform.scale(background, (screen_width, screen_height * 2))

# Variáveis para o movimento do fundo
background_x = 0

#Atualizado
#background_y = 0

background_speed = 5

# Define um titulo para a janela
pygame.display.set_caption("Tela Principal")

# Define as cores em RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Declarando a fonte do placar e variável contadora
font = pygame.font.SysFont('sans', 40)
placar = 0

# Variável para contagem de tempo, utilizado para controlar a velocidade de quadros (de atualizações da tela)
clock = pygame.time.Clock()

# Criando objeto Clock
CLOCKTICK = pygame.USEREVENT + 1
pygame.time.set_timer(CLOCKTICK, 1000)  # configurado o timer do Pygame para execução a cada 1 segundo
temporizador = 60

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
while True:
    # Verifica se algum evento aconteceu
    for event in pygame.event.get():
        # Verifica se foi um evento de saída (pygame.QUIT), 
        # em caso afirmativo, fecha a aplicação
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Capturando evento de relógio a cada 1 segundo e atualizando a variável contadora
        if event.type == CLOCKTICK:
            temporizador -= 1

    # Atualiza a posição do fundo
    background_x -= background_speed
    if background_x <= -screen_width:
        background_x = 0
        
    #Atualizado
    #background_y -= background_speed
    #if background_y <= -screen_height:
        #background_y = 0
    
    # Desenha o fundo
    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + screen_width, 0))

    #Atualizado
    #screen.blit(background, (0, background_y))
    #screen.blit(background, (0, background_y + screen_height))

    # Renderizando as fontes do placar na tela
    score1 = font.render('Placar ' + str(placar), True, WHITE)
    screen.blit(score1, (600, 50))

    # Renderizando as fontes do cronômetro na tela do usuário
    timer1 = font.render('Tempo ' + str(temporizador), True, YELLOW)
    screen.blit(timer1, (50, 50))

    # Atualiza a tela visível ao usuário
    pygame.display.flip()

    # Limita a taxa de quadros (framerate) a 60 quadros por segundo (60fps)
    clock.tick(60)

# Final de jogo
textofinal = font.render('Fim de Jogo - Placar final: ' + str(placar), True, RED)
size = font.size(str(textofinal))
screen.blit(textofinal, (size[0] / 2., size[1] / 2.))

# Atualizamos a tela com uma nova tela de informação final ao jogador
pygame.display.flip()

# Pequeno loop game esperando o usuário encerrar
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

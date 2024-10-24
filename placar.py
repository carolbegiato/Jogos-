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

# Variáveis para o movimento do fundo
background_x = 0
background_speed = 5

# Cria a surface 
size = (800, 600)
screen = pygame.display.set_mode(size)

# Define um titulo para a janela
pygame.display.set_caption("Tela Principal")

# Define as cores em RGB
BLACK  = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Declarando a fonte do placar e variável contadora
font = pygame.font.SysFont('sans',40)
placar = 0

# Variável para contagem de tempo, utilizado para controlar a velocidade de quadros (de atualizações da tela)
clock = pygame.time.Clock()

#criando objeto Clock
CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) # configurado o timer do Pygame para execução a cada 1 segundo
temporizador = 60

# Loop principal do jogo
while True:

     # Verifica se algum evento aconteceu
    for event in pygame.event.get():
        # Verifica se foi um evento de saida (pygame.QUIT), 
        # em caso afirmativo fecha a aplicacao
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #capturando evendo de relogio a cada 1 segundo e atualizando a variável contadora
        if event.type == CLOCKTICK:
            temporizador = temporizador -1

    # Atualiza a posição do fundo
    background_x -= background_speed
    if background_x <= -screen_width:
        background_x = 0

    # Desenha o fundo
    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + screen_width, 0))
    
    # renderizando as fontes do placar na tela
    score1 = font.render('Placar '+str(placar), True, (WHITE))
    screen.blit(score1, (600, 50))

    #rendrizando as fontes do cronometro na tela do usuario
    timer1 = font.render('Tempo ' + str(temporizador), True, (YELLOW))
    screen.blit(timer1, (50, 50))

    # Atualiza a tela visivel ao usuario
    pygame.display.flip()

    # Limita a taxa de quadros (framerate) a 60 quadros por segundo (60fps)
    clock.tick(60)

#final de jogo


textofinal = font.render('Fim de Jogo - Placar final: ' + str(placar), True, (RED))
size = font.size(str(textofinal))
screen.blit(textofinal, (size[0]/2., size[1]/2.))


#atualizamos a tela com uma nova tela de informação final ao jogador
pygame.display.flip()
#pequeno loop game esperando o usuario encerrar
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
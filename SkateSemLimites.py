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
<<<<<<< HEAD
try:
    background = pygame.image.load('background.jpeg')  # Troque para 'background.png' se necessário
    background = pygame.transform.scale(background, (screen_width, screen_height))  # Ajusta o tamanho da imagem
except pygame.error as e:
    print(f"Erro ao carregar imagem de fundo: {e}")
    pygame.quit()
    sys.exit()

# Variáveis para o movimento do fundo
background_y = 0
background_speed = 5  # Fundo vai descer agora
=======
background = pygame.image.load('background.png')
#Atualizado
background = pygame.transform.scale(background, (screen_width, screen_height * 2))

# Variáveis para o movimento do fundo
#Atualizado
background_y = 0
background_speed = 5
>>>>>>> 6cc8db8 (atuialização)

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
CLOCKTICK = pygame.USEREVENT + 1
pygame.time.set_timer(CLOCKTICK, 1000)
temporizador = 60

# Carrega a imagem do personagem e define sua posição inicial
<<<<<<< HEAD
player_image = pygame.image.load('character.png')
player_image = pygame.transform.scale(player_image, (50, 50))
player_x = screen_width // 2
player_y = screen_height - 150
player_speed = 10

# Limites para o movimento do personagem
left_limit = 165
right_limit = screen_width - 120 - player_image.get_width()

# Imagens dos obstáculos
obstacle_images = {
    'lixo': pygame.image.load('lixo.png'),
    'poça': pygame.image.load('poca.png'),
    'buraco': pygame.image.load('buraco.png'),
    'rachadura': pygame.image.load('rachadura.png')
}

# Tamanho dos obstáculos
obstacle_size = (50, 50)

# Valores dos obstáculos (efeito da colisão ou desvio)
obstacle_values = {
    'lixo': 10,  # Subtrai pontos
    'poça': 5,   # Subtrai tempo
    'buraco': 6, # Subtrai pontos
    'rachadura': 3  # Subtrai pontos
}

# Lista de obstáculos
obstacles = []

# Função para criar novos obstáculos
def create_obstacle():
    # Escolher um tipo aleatório de obstáculo
    obstacle_type = choice(list(obstacle_images.keys()))
    img = obstacle_images[obstacle_type]
    img = pygame.transform.scale(img, obstacle_size)  # Ajustar o tamanho do obstáculo
    x_pos = randint(left_limit, right_limit)
    y_pos = -50  # Começa fora da tela
    value = obstacle_values[obstacle_type]
    return {'type': obstacle_type, 'image': img, 'x': x_pos, 'y': y_pos, 'value': value}
=======
player_image = pygame.image.load('character.png')  # Substitua pelo caminho da imagem do personagem
player_image = pygame.transform.scale(player_image, (50, 50))  # Redimensiona se necessário
player_x = screen_width // 2  # Começa no centro horizontal da tela
player_y = screen_height - 100  # Posiciona próximo à parte inferior da tela
player_speed = 10  # Velocidade de movimento do personagem
>>>>>>> 6cc8db8 (atuialização)

# Função do menu principal
def menu():
    menu_font = pygame.font.SysFont('sans', 50)
    start_text = menu_font.render("Pressione ENTER para iniciar", True, WHITE)
    
    while True:
        screen.fill(BLACK)
        screen.blit(start_text, (screen_width / 2 - start_text.get_width() / 2, screen_height / 2 - start_text.get_height() / 2))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

# Função para o menu de fim de jogo
def end_game_menu(final_score):
    end_font = pygame.font.SysFont('sans', 50)
    score_text = font.render(f'Placar final: {final_score}', True, RED)
    restart_text = end_font.render("Pressione ENTER para reiniciar", True, WHITE)
    exit_text = end_font.render("Pressione DELETE para sair", True, WHITE)

    while True:
        screen.fill(BLACK)
        screen.blit(score_text, (screen_width / 2 - score_text.get_width() / 2, screen_height / 2 - score_text.get_height() - 20))
        screen.blit(restart_text, (screen_width / 2 - restart_text.get_width() / 2, screen_height / 2 + 10))
        screen.blit(exit_text, (screen_width / 2 - exit_text.get_width() / 2, screen_height / 2 + 60))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Reinicia o jogo
                    return True
                elif event.key == pygame.K_DELETE:  # Sai do jogo
                    pygame.quit()
                    sys.exit()

# Chama a tela de menu antes do loop principal do jogo
menu()

# Loop principal do jogo
<<<<<<< HEAD
while True:
    # Reinicia as variáveis do jogo
    temporizador = 60
    placar = 0
    obstacles.clear()
    player_x = screen_width // 2  # Reseta posição do jogador

    # Criação de obstáculos
    pygame.time.set_timer(pygame.USEREVENT + 2, 1500)  # Cria um novo obstáculo a cada 1.5 segundos
    
    while temporizador > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == CLOCKTICK:
                temporizador -= 1
            if event.type == pygame.USEREVENT + 2:  # Criação periódica de obstáculos
                obstacles.append(create_obstacle())

        # Movimento do fundo (para baixo)
        background_y += background_speed
        if background_y >= screen_height:
            background_y = 0

        # Movimento do personagem com limite de bordas
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and player_x > left_limit:
            player_x -= player_speed
        if keys[K_RIGHT] and player_x < right_limit:
            player_x += player_speed

        # Atualização dos obstáculos
        for obstacle in obstacles[:]:
            obstacle['y'] += 5  # Velocidade do obstáculo
            
            # Verifica colisão
            player_rect = pygame.Rect(player_x, player_y, player_image.get_width(), player_image.get_height())
            obstacle_rect = pygame.Rect(obstacle['x'], obstacle['y'], obstacle['image'].get_width(), obstacle['image'].get_height())
            
            if player_rect.colliderect(obstacle_rect):
                if obstacle['type'] == 'poça':
                    temporizador -= 5  # Perde 5 segundos
                else:
                    placar -= obstacle['value']  # 
                obstacles.remove(obstacle)
            elif obstacle['y'] > screen_height:
                placar += obstacle['value']  # Soma o valor se desviar
                obstacles.remove(obstacle)
=======
while temporizador > 0:  # O loop roda enquanto o temporizador não acaba
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == CLOCKTICK:
            temporizador -= 1

    # Movimento do fundo
    #Atualizado
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
    #Atualizado
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y + screen_height))

    # Desenha o personagem
    screen.blit(player_image, (player_x, player_y))

    # Renderizando as fontes do placar e do cronômetro na tela
    score1 = font.render('Placar ' + str(placar), True, WHITE)
    screen.blit(score1, (600, 50))

    timer1 = font.render('Tempo ' + str(temporizador), True, YELLOW)
    screen.blit(timer1, (50, 50))
>>>>>>> 6cc8db8 (atuialização)

        # Desenha o fundo
        screen.blit(background, (0, background_y))  # Desenha fundo na posição Y
        screen.blit(background, (0, background_y - screen_height))  # Desenha fundo duplicado para criar efeito de movimento

<<<<<<< HEAD
        # Desenha o personagem
        screen.blit(player_image, (player_x, player_y))

        # Desenha os obstáculos
        for obstacle in obstacles:
            screen.blit(obstacle['image'], (obstacle['x'], obstacle['y']))

        # Renderizando as fontes do placar e do cronômetro na tela
        score1 = font.render('Placar: ' + str(placar), True, WHITE)
        screen.blit(score1, (600, 50))
        timer1 = font.render('Tempo: ' + str(temporizador), True, YELLOW)
        screen.blit(timer1, (50, 50))

        # Atualiza a tela visível ao usuário
        pygame.display.flip()

        # Limita a taxa de quadros a 60 fps
        clock.tick(60)

    # Chama o menu de fim de jogo e decide se reinicia ou encerra
    if not end_game_menu(placar):
        break
=======
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
>>>>>>> 6cc8db8 (atuialização)

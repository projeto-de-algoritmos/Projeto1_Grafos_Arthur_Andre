import time

import pygame
start = True
# definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (128,128,128)
NAVY = (0,0,128)
#iniciando pygame
pygame.init()
# carregando fonte
font = pygame.font.SysFont(None, 55)
#tamanho da tela
display_x =640
display_y = 480
screen = pygame.display.set_mode((display_x, display_y))
#fps
frame = pygame.time.Clock()
clicks=[]
#inicio do jogo
def valida_click(x,y,posicao_x,posicao_y):
    if x <= posicao_x and x>= posicao_x+ 60 and posicao_y <= y and y<= posicao_y +5:
        clicks.append([x,y])
        print(clicks)
def tabuleiro(posicao_x,posicao_y):
     #horizontal
        for y in range(0,300,75):
            for x in range(0,500,84):
                pygame.draw.rect(screen, GRAY ,[y+160, x+40, 60, 5])
                valida_click(x,y,posicao_x,posicao_y)
        for y in range(0,375,75):
            for x in range(0,504,84):
                
                pygame.draw.ellipse(screen, NAVY, [y+145, x+35, 15, 15])
        #vertical
        for y in range(0,375,75):
            for x in range(0,420,84):
                pygame.draw.rect(screen, GRAY, [y+150, x+50, 5, 70])
                valida_click(x,y,posicao_x,posicao_y)
#menu
def menu():
    # preenchendo o fundo
    screen.fill(WHITE) 
    pygame.draw.rect(screen, RED, [display_x/2-100, display_y/2, 200, 40])
    # definindo o texto
    text = font.render('Play Game', True, WHITE)
    # copiando o texto para a superfície
    screen.blit(text, [display_x/2-100, display_y/2])
def Game(start):
    sair = True
    while sair:
        # PROCESSAMENTO DE ENTRADA
        mouse_x =0
        mouse_y = 0
        # capturando eventos
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
              mouse_x =pygame.mouse.get_pos()[0]
              mouse_y = pygame.mouse.get_pos()[1]
       
           
        # caso o evento QUIT (clicar no x da janela) seja disparado
        if event.type == pygame.QUIT:
            sair = False
        #titulo
        pygame.display.set_caption('Olá mundo')

        # preenchendo o fundo com preto
        screen.fill(WHITE)

        # desenhando na superfície 
        if(start):
            menu()
        if(start and mouse_x >= display_x/2-100 and mouse_x <= display_x/2-100+200 and mouse_y >= display_y/2 and mouse_y <= display_y/2+40 ):
            start = False
        if(not(start)):
            tabuleiro(mouse_x,mouse_y)
            
        # atualizando a tela
        
        pygame.display.flip()

        # atualizando a tela
        pygame.display.update()
        frame.tick(25)


Game(start)
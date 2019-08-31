import time

import pygame

# definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()
sair = True
    #fps
frame = pygame.time.Clock()
while sair:
    # PROCESSAMENTO DE ENTRADA

    # capturando eventos
    for event in pygame.event.get():
       
    # caso o evento QUIT (clicar no x da janela) seja disparado
        if event.type == pygame.QUIT:
            sair = False

   
    screen = pygame.display.set_mode((640, 480))
    # carregando fonte
    font = pygame.font.SysFont(None, 55)

    pygame.display.set_caption('Olá mundo')

    # preenchendo o fundo com preto
    screen.fill(BLACK)

    # desenhando na superfície 
    #horizontal
    for y in range(0,300,75):
        for x in range(0,500,84):
            pygame.draw.rect(screen, RED, [y+260, x+40, 60, 5])
            
        #vertical
    for y in range(0,375,75):
        for x in range(0,504,84):
            
            pygame.draw.ellipse(screen, WHITE, [y+245, x+35, 15, 15])

    for y in range(0,375,75):
        for x in range(0,420,84):
            pygame.draw.rect(screen, BLUE, [y+250, x+50, 5, 70])
    # atualizando a tela
    pygame.display.flip()

  

    # preenchendo o fundo com preto
    

    # atualizando a tela
    pygame.display.update()
    frame.tick(25)

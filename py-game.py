# coding: utf-8
import time
import pygame
from main import Graph

# definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (30, 30, 29)

pygame.init()
sair = True
    #fps
frame = pygame.time.Clock()

graph = Graph()
graph.create(6, 5, 0)

while sair:
    # PROCESSAMENTO DE ENTRADA
    screen = pygame.display.set_mode((800, 600))

    # carregando fonte
    font = pygame.font.SysFont(None, 55)
    #titulo da janela
    pygame.display.set_caption('Dots & Boxes')

    # preenchendo o fundo com preto
    screen.fill(BLACK)

## desenhando na superficie 
    # arestas horizontais
    for y in range(0,300,75):
        for x in range(0,500,84):
            pygame.draw.rect(screen, GRAY, [y+260, x+40, 60, 5])
            
    #vértices
    for y in range(0,375,75):
        for x in range(0,504,84): 
            pygame.draw.ellipse(screen, WHITE, [y+245, x+35, 15, 15])

    for y in range(0,375,75):
        for x in range(0,420,84):
            pygame.draw.rect(screen, GRAY, [y+250, x+50, 5, 70])

    #arestas verticaiscapturando eventos
    for event in pygame.event.get():
       
    # caso o evento QUIT (clicar no x da janela) seja disparado
        if event.type == pygame.QUIT:
            sair = False

        if event.type == pygame.MOUSEBUTTONDOWN:            
            
            mx, my = pygame.mouse.get_pos()
            print('(', mx, ') (', my, ')') #337

            #horizontal first line
            
            if mx >= 262 and mx <= 315 and my >= 32 and my <= 50: 
                graph.connect_egde(0, 1)
                pygame.draw.rect(screen, RED, [260, 40, 60, 5])
            elif mx >= 337 and mx <= 390 and my >= 32 and my <= 50:
                graph.connect_egde(1, 2)
                pygame.draw.rect(screen, RED, [335, 40, 60, 5])
            elif mx >= 412 and mx <= 465 and my >= 32 and my <= 50:
                graph.connect_egde(2, 3)
                pygame.draw.rect(screen, RED, [410, 40, 60, 5])
            elif mx >= 487 and mx <= 540 and my >= 32 and my <= 50:
                graph.connect_egde(3, 4)
                pygame.draw.rect(screen, RED, [485, 40, 60, 5])
                
           #horizontal second line

            if mx >= 262 and mx <= 315 and my >= 116 and my <= 134:
                pygame.draw.rect(screen, RED, [260, 124, 60, 5])
            elif mx >= 337 and mx <= 390 and my >= 116 and my <= 134:
                pygame.draw.rect(screen, RED, [335, 124, 60, 5])
            elif mx >= 412 and mx <= 465 and my >= 116 and my <= 134:
                pygame.draw.rect(screen, RED, [410, 124, 60, 5])
            elif mx >= 487 and mx <= 540 and my >= 116 and my <= 134:
                pygame.draw.rect(screen, RED, [485, 124, 60, 5])

            #horizontal third line

            if mx >= 262 and mx <= 315 and my >= 200 and my <= 218:
                pygame.draw.rect(screen, RED, [260, 208, 60, 5])
            elif mx >= 337 and mx <= 390 and my >= 200 and my <= 218:
                pygame.draw.rect(screen, RED, [335, 208, 60, 5])
            elif mx >= 412 and mx <= 465 and my >= 200 and my <= 218:
                pygame.draw.rect(screen, RED, [410, 208, 60, 5])
            elif mx >= 487 and mx <= 540 and my >= 200 and my <= 218:
                pygame.draw.rect(screen, RED, [485, 208, 60, 5])
            

            #horizontal fourty line

            if mx >= 262 and mx <= 315 and my >= 284 and my <= 300:
                pygame.draw.rect(screen, RED, [260, 292, 60, 5])
            elif mx >= 337 and mx <= 390 and my >= 284 and my <= 300:
                pygame.draw.rect(screen, RED, [335, 292, 60, 5])
            elif mx >= 412 and mx <= 465 and my >= 284 and my <= 300:
                pygame.draw.rect(screen, RED, [410, 292, 60, 5])
            elif mx >= 487 and mx <= 540 and my >= 284 and my <= 300:
                pygame.draw.rect(screen, RED, [485, 292, 60, 5])

            #horizontal fifty line

            if mx >= 262 and mx <= 315 and my >= 368 and my <= 386:
                pygame.draw.rect(screen, RED, [260, 376, 60, 5])
            elif mx >= 337 and mx <= 390 and my >= 368 and my <= 386:
                pygame.draw.rect(screen, RED, [335, 376, 60, 5])
            elif mx >= 412 and mx <= 465 and my >= 368 and my <= 386:
                pygame.draw.rect(screen, RED, [410, 376, 60, 5])
            elif mx >= 487 and mx <= 540 and my >= 368 and my <= 386:
                pygame.draw.rect(screen, RED, [485, 376, 60, 5])

            #horizontal sixty line

            if mx >= 262 and mx <= 315 and my >= 452 and my <= 470:
                pygame.draw.rect(screen, RED, [260, 460, 60, 5])
            elif mx >= 337 and mx <= 390 and my >= 452 and my <= 470:
                pygame.draw.rect(screen, RED, [335, 460, 60, 5])
            elif mx >= 412 and mx <= 465 and my >= 452 and my <= 470:
                pygame.draw.rect(screen, RED, [410, 460, 60, 5])
            elif mx >= 487 and mx <= 540 and my >= 452 and my <= 470:
                pygame.draw.rect(screen, RED, [485, 460, 60, 5])

            #vertical first line

            if mx >= 244 and mx <= 262 and my >= 50 and my <= 117:
                pygame.draw.rect(screen, RED, [251, 50, 5, 70])
            elif mx >= 244 and mx <= 262 and my >= 134 and my <= 201:
                pygame.draw.rect(screen, RED, [251, 134, 5, 70])
            elif mx >= 244 and mx <= 262 and my >= 218 and my <= 285:
                pygame.draw.rect(screen, RED, [251, 218, 5, 70])
            elif mx >= 244 and mx <= 262 and my >= 302 and my <= 369:
                pygame.draw.rect(screen, RED, [251, 302, 5, 70])
            elif mx >= 244 and mx <= 262 and my >= 386 and my <= 453:
                pygame.draw.rect(screen, RED, [251, 386, 5, 70])

            #vertical second line

            if mx >= 318 and mx <= 336 and my >= 50 and my <= 117:
                pygame.draw.rect(screen, RED, [326, 50, 5, 70])
            elif mx >= 318 and mx <= 336 and my >= 134 and my <= 201:
                pygame.draw.rect(screen, RED, [326, 134, 5, 70])
            elif mx >= 318 and mx <= 336 and my >= 218 and my <= 285:
                pygame.draw.rect(screen, RED, [326, 218, 5, 70])
            elif mx >= 318 and mx <= 336 and my >= 302 and my <= 369:
                pygame.draw.rect(screen, RED, [326, 302, 5, 70])
            elif mx >= 318 and mx <= 336 and my >= 386 and my <= 453:
                pygame.draw.rect(screen, RED, [326, 386, 5, 70])


            #vertical third line

            if mx >= 393 and mx <= 411 and my >= 50 and my <= 117:
                pygame.draw.rect(screen, RED, [401, 50, 5, 70])
            elif mx >= 393 and mx <= 411 and my >= 134 and my <= 201:
                pygame.draw.rect(screen, RED, [401, 134, 5, 70])
            elif mx >= 393 and mx <= 411 and my >= 218 and my <= 285:
                pygame.draw.rect(screen, RED, [401, 218, 5, 70])
            elif mx >= 393 and mx <= 411 and my >= 302 and my <= 369:
                pygame.draw.rect(screen, RED, [401, 302, 5, 70])
            elif mx >= 393 and mx <= 411 and my >= 386 and my <= 453:
                pygame.draw.rect(screen, RED, [401, 386, 5, 70])


            #vertical fourty line

            if mx >= 468 and mx <= 486 and my >= 50 and my <= 117:
                pygame.draw.rect(screen, RED, [476, 50, 5, 70])
            elif mx >= 468 and mx <= 486 and my >= 134 and my <= 201:
                pygame.draw.rect(screen, RED, [476, 134, 5, 70])
            elif mx >= 468 and mx <= 486 and my >= 218 and my <= 285:
                pygame.draw.rect(screen, RED, [476, 218, 5, 70])
            elif mx >= 468 and mx <= 486 and my >= 302 and my <= 369:
                pygame.draw.rect(screen, RED, [476, 302, 5, 70])
            elif mx >= 468 and mx <= 486 and my >= 386 and my <= 453:
                pygame.draw.rect(screen, RED, [476, 386, 5, 70])

            
            #vertical fifty line

            if mx >= 543 and mx <= 561 and my >= 50 and my <= 117:
                pygame.draw.rect(screen, RED, [551, 50, 5, 70])
            elif mx >= 543 and mx <= 561 and my >= 134 and my <= 201:
                pygame.draw.rect(screen, RED, [551, 134, 5, 70])
            elif mx >= 543 and mx <= 561 and my >= 218 and my <= 285:
                pygame.draw.rect(screen, RED, [551, 218, 5, 70])
            elif mx >= 543 and mx <= 561 and my >= 302 and my <= 369:
                pygame.draw.rect(screen, RED, [551, 302, 5, 70])
            elif mx >= 543 and mx <= 561 and my >= 386 and my <= 453:
                pygame.draw.rect(screen, RED, [551, 386, 5, 70])



    pygame.display.flip()

    pygame.display.update()
    frame.tick(25)
    
    # atualizando a tela
    #

  

    # preenchendo o fundo com preto
    

    # atualizando a tela
    

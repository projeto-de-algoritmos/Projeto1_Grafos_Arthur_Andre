# coding: utf-8
import time
import pygame
from main import Graph, Game
import time
import sys

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
graph.create(5, 5)
bot = Game()


# PROCESSAMENTO DE ENTRADA
screen = pygame.display.set_mode((640, 480))
contador = 0
# carregando fonte
font = pygame.font.SysFont(None, 55)
#titulo da janela
pygame.display.set_caption('Dots & Boxes')

# preenchendo o fundo com preto
screen.fill(BLACK)

#vértices
for y in range(0,300,75):
    for x in range(0,416,84):
        pygame.draw.rect(screen, GRAY, [y+160, x+40, 60, 5])

#vértices
for y in range(0,375,75):
    for x in range(0,420,84): 
        pygame.draw.ellipse(screen, WHITE, [y+145, x+35, 15, 15])

for y in range(0,375,75):
    for x in range(0,336,84):
        pygame.draw.rect(screen, GRAY, [y+150, x+50, 5, 70])


def collor(aux):
    
    if aux['orientation'] == 'horizontal':
        x = aux['axis']['list'][0]
        y = aux['axis']['list'][1]
        pygame.draw.rect(screen, RED ,[x+160, y+40, 60,5])
    
    else:
        x = aux['axis']['list'][0]
        y = aux['axis']['list'][1]
        pygame.draw.rect(screen, RED ,[x+150, y+50, 5, 70])


    
repeat = False
bots_turn = False
#arestas verticaiscapturando eventos
while sair:
    for event in pygame.event.get():
       graph.points(graph.get_vertexs())
    # caso o evento QUIT (clicar no x da janela) seja disparado
        if event.type == pygame.QUIT:
            sair = False

        if event.type == pygame.MOUSEBUTTONDOWN:            
            repeat = False
            bots_turn = False
            mx, my = pygame.mouse.get_pos()
            #print('(', mx, ') (', my, ')') #337
            for vertex in graph.get_vertexs():
                x_r = vertex['axis']['right']['list'][0]
                y_r = vertex['axis']['right']['list'][1]
                x_d = vertex['axis']['down']['list'][0]
                y_d = vertex['axis']['down']['list'][1]

                        
                if mx >= x_r+160 and mx <= x_r+160+70 and my >= y_r+40 and my<= y_r+40+5: 
                    #se os vertices ja tiverem conectados, o jogador tem que jogar de novo
                    if graph.is_connected(vertex['value'], vertex['value'] + 1):
                        print('repeat')
                        repeat = True
                        break
                    repeat = False
                    
                    graph.connect_egde(vertex['value'], vertex['value'] + 1, 'horizontal')
                    vertex['axis']['right']['clicked'] = 1
                    pygame.draw.rect(screen, BLUE ,[x_r+160, y_d+40, 60,5])
                    bots_turn = True


                elif mx >= x_d+150 and mx <= x_d+150+5 and my >= y_d+50 and my<= y_d+50+60:
                    if graph.is_connected(vertex['value'], vertex['value'] + graph.get_columns()):
                        print('repeat')
                        repeat = True
                        break
                    repeat = False
                    pygame.draw.rect(screen, BLUE ,[x_d+150, y_d+50, 5, 70])
                    vertex['axis']['down']['clicked'] = 1
                    graph.connect_egde(vertex['value'], vertex['value'] + graph.get_columns(), 'vertical')
                    bots_turn = True

            if repeat:
                continue

          #parte em que o algoritmo "joga" (aleatorio)
            if bots_turn:
                
                while True:
                    #recebe as coordenadas da jogada
                    play = bot.machine_action_easy(graph.get_vertexs())
                    
                    if play['orientation'] == 'horizontal':
                        a = play['vertex']
                        if a == 4 or a == 9 or a == 14 or a == 19 or a == 24:
                            continue
                        if not graph.is_connected(play['vertex'], play['vertex'] + 1):
                            graph.connect_egde(play['vertex'], play['vertex'] + 1, 'horizontal')
                            play['axis']['right']['clicked'] = 1
                            print '(', play['vertex'], ') (', play['vertex'] + 1, ')'
                            collor(play)
                        else:
                            print('finding another edge')
                            print '(', play['vertex'], ') (', play['vertex'] + 1, ')'
                            continue
                    else:
                        a = play['vertex']
                        if a == 20 or a == 21 or a == 22 or a == 23 or a == 24:
                            continue
                        if not graph.is_connected(play['vertex'], play['vertex'] + graph.get_columns()):
                            graph.connect_egde(play['vertex'], play['vertex'] + graph.get_columns(), 'vertical')
                            play['axis']['down']['clicked'] = 1
                            print '(', play['vertex'], ') (', play['vertex'] + graph.get_columns() , ')'
                            collor(play)
                        else:
                            print('finding another edge')
                            print '(', play['vertex'], ') (', play['vertex'] + 1, ')'
                            continue

                    
                    break
                
                    

    pygame.display.update()
    pygame.display.flip()
    frame.tick(25)


    
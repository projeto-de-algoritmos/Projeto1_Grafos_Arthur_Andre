# coding: utf-8
import time
import pygame
from main import Graph, Game
import time

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
bot = Game()


# PROCESSAMENTO DE ENTRADA
screen = pygame.display.set_mode((800, 600))
contador = 0
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


def collor(play):
    pygame.draw.rect(screen, BLUE, [play['axis'][0], play['axis'][1], play['k'], play['t']])
    



#arestas verticaiscapturando eventos
while sair:
    for event in pygame.event.get():
       
    # caso o evento QUIT (clicar no x da janela) seja disparado
        if event.type == pygame.QUIT:
            sair = False

        if event.type == pygame.MOUSEBUTTONDOWN:            
            
            mx, my = pygame.mouse.get_pos()
            print('(', mx, ') (', my, ')') #337

            #horizontal first line
            
            if mx >= 262 and mx <= 315 and my >= 32 and my <= 50: 
                if not graph.is_connected(0, 1):
                    graph.connect_egde(0, 1)
                    pygame.draw.rect(screen, RED, [260, 40, 60, 5]) 
                else:
                    print('ja esta conectado')
                    continue         
            elif mx >= 337 and mx <= 390 and my >= 32 and my <= 50:
                if not graph.is_connected(1, 2):
                    graph.connect_egde(1, 2)
                    pygame.draw.rect(screen, RED, [335, 40, 60, 5])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 412 and mx <= 465 and my >= 32 and my <= 50:
                if not graph.is_connected(2, 3):
                    graph.connect_egde(2, 3)
                    pygame.draw.rect(screen, RED, [410, 40, 60, 5])
                else:
                    print('ja esta conectado')
                    continue      
            elif mx >= 487 and mx <= 540 and my >= 32 and my <= 50:
                if not graph.is_connected(3, 4):
                    graph.connect_egde(3, 4)
                    pygame.draw.rect(screen, RED, [485, 40, 60, 5])
                else:
                    print('ja esta conectado')
                    continue  
            # else:
            #     continue
                
           #horizontal second line

            if mx >= 262 and mx <= 315 and my >= 116 and my <= 134:
                if not graph.is_connected(5, 6):
                    graph.connect_egde(5, 6)
                    pygame.draw.rect(screen, RED, [260, 124, 60, 5])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 337 and mx <= 390 and my >= 116 and my <= 134:
                if not graph.is_connected(6, 7):
                    graph.connect_egde(6, 7)
                    pygame.draw.rect(screen, RED, [335, 124, 60, 5])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 412 and mx <= 465 and my >= 116 and my <= 134:
                if not graph.is_connected(7, 8):
                    graph.connect_egde(7, 8)
                    pygame.draw.rect(screen, RED, [410, 124, 60, 5])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 487 and mx <= 540 and my >= 116 and my <= 134:
                if not graph.is_connected(8, 9):
                    graph.connect_egde(8, 9)
                    pygame.draw.rect(screen, RED, [485, 124, 60, 5])
                else:
                    print('ja esta conectado')
                    continue  

            #horizontal third line

            if mx >= 262 and mx <= 315 and my >= 200 and my <= 218:
                if not graph.is_connected(10, 11):
                    graph.connect_egde(10, 11)
                    pygame.draw.rect(screen, RED, [260, 208, 60, 5])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 337 and mx <= 390 and my >= 200 and my <= 218:
                if not graph.is_connected(11, 12):
                    graph.connect_egde(11, 12)
                    pygame.draw.rect(screen, RED, [335, 208, 60, 5])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 412 and mx <= 465 and my >= 200 and my <= 218:
                if not graph.is_connected(12, 13):
                    graph.connect_egde(12, 13)
                    pygame.draw.rect(screen, RED, [410, 208, 60, 5])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 487 and mx <= 540 and my >= 200 and my <= 218:
                if not graph.is_connected(13, 14):
                    graph.connect_egde(13, 14)
                    pygame.draw.rect(screen, RED, [485, 208, 60, 5])
                else:
                    print('ja esta conectado')
                    continue  
            
            

            #horizontal fourty line

            if mx >= 262 and mx <= 315 and my >= 284 and my <= 300:
                if not graph.is_connected(15, 16):
                    graph.connect_egde(15, 16)
                    pygame.draw.rect(screen, RED, [260, 292, 60, 5])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 337 and mx <= 390 and my >= 284 and my <= 300:
                if not graph.is_connected(16, 17):
                    graph.connect_egde(16, 17)
                    pygame.draw.rect(screen, RED, [335, 292, 60, 5])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 412 and mx <= 465 and my >= 284 and my <= 300:
                if not graph.is_connected(17, 18):
                    graph.connect_egde(17, 18)
                    pygame.draw.rect(screen, RED, [410, 292, 60, 5])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 487 and mx <= 540 and my >= 284 and my <= 300:
                if not graph.is_connected(18, 19):
                    graph.connect_egde(18, 19)
                    pygame.draw.rect(screen, RED, [485, 292, 60, 5])
                else:
                    print('ja esta conectado')
                    continue  

            #horizontal fifty line

            if mx >= 262 and mx <= 315 and my >= 368 and my <= 386:
                if not graph.is_connected(20, 21):
                    graph.connect_egde(20, 21)
                    pygame.draw.rect(screen, RED, [260, 376, 60, 5])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 337 and mx <= 390 and my >= 368 and my <= 386:
                if not graph.is_connected(21, 22):
                    graph.connect_egde(21, 22)
                    pygame.draw.rect(screen, RED, [335, 376, 60, 5])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 412 and mx <= 465 and my >= 368 and my <= 386:
                if not graph.is_connected(22, 23):
                    graph.connect_egde(22, 23)
                    pygame.draw.rect(screen, RED, [410, 376, 60, 5])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 487 and mx <= 540 and my >= 368 and my <= 386:
                if not graph.is_connected(23, 24):
                    graph.connect_egde(23, 24)
                    pygame.draw.rect(screen, RED, [485, 376, 60, 5])
                else:
                    print('ja esta conectado')
                    continue  
            #horizontal sixty line

            if mx >= 262 and mx <= 315 and my >= 452 and my <= 470:
                if not graph.is_connected(25, 26):
                    graph.connect_egde(25, 26)
                    pygame.draw.rect(screen, RED, [260, 460, 60, 5])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 337 and mx <= 390 and my >= 452 and my <= 470:
                if not graph.is_connected(26, 27):
                    graph.connect_egde(26, 27)
                    pygame.draw.rect(screen, RED, [335, 460, 60, 5])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 412 and mx <= 465 and my >= 452 and my <= 470:
                if not graph.is_connected(27, 28):
                    graph.connect_egde(27, 28)
                    pygame.draw.rect(screen, RED, [410, 460, 60, 5])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 487 and mx <= 540 and my >= 452 and my <= 470:
                if not graph.is_connected(28, 29):
                    graph.connect_egde(28, 29)
                    pygame.draw.rect(screen, RED, [485, 460, 60, 5])
                else:
                    print('ja esta conectado')
                    continue  

            #vertical first column

            if mx >= 244 and mx <= 262 and my >= 50 and my <= 117:
                if not graph.is_connected(0, 5):
                    graph.connect_egde(0, 5)
                    pygame.draw.rect(screen, RED, [251, 50, 5, 70])   
                else:
                    print('ja esta conectado')
                    continue        
            elif mx >= 244 and mx <= 262 and my >= 134 and my <= 201:
                if not graph.is_connected(5, 10):
                    graph.connect_egde(5, 10)
                    pygame.draw.rect(screen, RED, [251, 134, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 244 and mx <= 262 and my >= 218 and my <= 285:
                if not graph.is_connected(10, 15):
                    graph.connect_egde(10, 15)
                    pygame.draw.rect(screen, RED, [251, 218, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 244 and mx <= 262 and my >= 302 and my <= 369:
                if not graph.is_connected(15, 20):
                    graph.connect_egde(15, 20)
                    pygame.draw.rect(screen, RED, [251, 302, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 244 and mx <= 262 and my >= 386 and my <= 453:
                if not graph.is_connected(20, 25):
                    graph.connect_egde(20, 25)
                    pygame.draw.rect(screen, RED, [251, 386, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  

            #vertical second line

            if mx >= 318 and mx <= 336 and my >= 50 and my <= 117:
                if not graph.is_connected(1, 6):
                    graph.connect_egde(1, 6)
                    pygame.draw.rect(screen, RED, [326, 50, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 318 and mx <= 336 and my >= 134 and my <= 201:
                if not graph.is_connected(6, 11):
                    graph.connect_egde(6, 11)
                    pygame.draw.rect(screen, RED, [326, 134, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 318 and mx <= 336 and my >= 218 and my <= 285:
                if not graph.is_connected(11, 16):
                    graph.connect_egde(11, 16)
                    pygame.draw.rect(screen, RED, [326, 218, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 318 and mx <= 336 and my >= 302 and my <= 369:
                if not graph.is_connected(16, 21):
                    graph.connect_egde(16, 21)
                    pygame.draw.rect(screen, RED, [326, 302, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 318 and mx <= 336 and my >= 386 and my <= 453:
                if not graph.is_connected(21, 26):
                    graph.connect_egde(21, 26)
                    pygame.draw.rect(screen, RED, [326, 386, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  


            #vertical third line

            if mx >= 393 and mx <= 411 and my >= 50 and my <= 117:
                if not graph.is_connected(2, 7):
                    graph.connect_egde(2, 7)
                    pygame.draw.rect(screen, RED, [401, 50, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 393 and mx <= 411 and my >= 134 and my <= 201:
                if not graph.is_connected(7, 12):
                    graph.connect_egde(7, 12)
                    pygame.draw.rect(screen, RED, [401, 134, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 393 and mx <= 411 and my >= 218 and my <= 285:
                if not graph.is_connected(12, 17):
                    graph.connect_egde(12, 17)
                    pygame.draw.rect(screen, RED, [401, 218, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 393 and mx <= 411 and my >= 302 and my <= 369:
                if not graph.is_connected(17, 22):
                    graph.connect_egde(17, 22)
                    pygame.draw.rect(screen, RED, [401, 302, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 393 and mx <= 411 and my >= 386 and my <= 453:
                if not graph.is_connected(22, 27):
                    graph.connect_egde(22, 27)
                    pygame.draw.rect(screen, RED, [401, 386, 5, 70])


            #vertical fourty line

            if mx >= 468 and mx <= 486 and my >= 50 and my <= 117:
                if not graph.is_connected(3, 8):
                    graph.connect_egde(3, 8)
                    pygame.draw.rect(screen, RED, [476, 50, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 468 and mx <= 486 and my >= 134 and my <= 201:
                if not graph.is_connected(8, 13):
                    graph.connect_egde(8, 13)
                    pygame.draw.rect(screen, RED, [476, 134, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 468 and mx <= 486 and my >= 218 and my <= 285:
                if not graph.is_connected(13, 18):
                    graph.connect_egde(13, 18)
                    pygame.draw.rect(screen, RED, [476, 218, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 468 and mx <= 486 and my >= 302 and my <= 369:
                if not graph.is_connected(18, 23):
                    graph.connect_egde(18, 23)
                    pygame.draw.rect(screen, RED, [476, 302, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 468 and mx <= 486 and my >= 386 and my <= 453:
                if not graph.is_connected(23, 28):
                    graph.connect_egde(23, 28)
                    pygame.draw.rect(screen, RED, [476, 386, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  

            
            #vertical fifty line

            if mx >= 543 and mx <= 561 and my >= 50 and my <= 117:
                if not graph.is_connected(4, 9):
                    graph.connect_egde(4, 9)
                    pygame.draw.rect(screen, RED, [551, 50, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 543 and mx <= 561 and my >= 134 and my <= 201:
                if not graph.is_connected(9, 14):
                    graph.connect_egde(9, 14)
                    pygame.draw.rect(screen, RED, [551, 134, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 543 and mx <= 561 and my >= 218 and my <= 285:
                if not graph.is_connected(14, 19):
                    graph.connect_egde(14, 19)
                    pygame.draw.rect(screen, RED, [551, 218, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 543 and mx <= 561 and my >= 302 and my <= 369:
                if not graph.is_connected(19, 24):
                    graph.connect_egde(19, 24)
                    pygame.draw.rect(screen, RED, [551, 302, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  
            elif mx >= 543 and mx <= 561 and my >= 386 and my <= 453:
                if not graph.is_connected(24, 29):
                    graph.connect_egde(24, 29)
                    pygame.draw.rect(screen, RED, [551, 386, 5, 70])
                else:
                    print('ja esta conectado')
                    continue  


            #time.sleep(3)
          
            while True:
                play = bot.machine_action_easy(graph.get_vertexs())
                print(play['vertexs'][0], ' **-> ', play['vertexs'][1])
                if graph.is_connected(play['vertexs'][0], play['vertexs'][1]):
                    continue
                else:
                    graph.connect_egde(play['vertexs'][0], play['vertexs'][1])
                    collor(play)
                    break
                    

    
    
    # atualizando a tela
    #
    pygame.display.update()
    pygame.display.flip()
    frame.tick(25)


    # preenchendo o fundo com preto
    

    # atualizando a tela
    

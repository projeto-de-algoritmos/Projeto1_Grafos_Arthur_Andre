from random import randint
from game import *
x_inicial = 160
y_inicial = 150

class Graph:

    vertexs = []

    def __init__(self):
        pass

    def create(self,lines, column):
        self.total_vertexs = lines * column

        valor_x = x_inicial
        valor_y = y_inicial
        for y in range(lines):
            for x in range(lines):
                vertex = {
                    'value': i,
                    'neighbors': [],
                    'clicked': False,
                    'axis': [valor_x,valor_y]
                    
                }
                valor_x += 84
            valor_y += 75

        self.vertexs.append(vertex)

        def connect_egde(self, origin, destiny):  # graph bidirected
            self.vertexs[origin]['neighbors'].append(destiny)
            self.vertexs[destiny]['neighbors'].append(origin)

    def get_vertex(self):
        return self.total_vertexs

    def get_vertexs_value(self):
        values = []
        for vertex in self.vertexs:
            values.append(vertex[axis])

        return values

    def print_grid(self):
        for i in range(self.total_vertexs):
            print('{:02d}'.format(self.vertexs[i]['value']), ' ', end="")
            if i == 4 or i == 9 or i == 14:
                print('\n')

    def print_list(self):
        print('\n\n\n -- adjacency list --\n')
        for vertex in self.vertexs:
            if not vertex['neighbors'] == []:
                print(vertex['value'], ' - > ', end="")
                for neigh in vertex['neighbors']:
                    print('{:02}'.format(neigh), ' - ', end="")
                print('\n')

        print('\n')
    create(4,4)
    print(get_vertexs_value(vertexs))
Game(True)
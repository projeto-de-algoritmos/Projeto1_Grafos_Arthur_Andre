from random import randint

x_inicial = 150
y_inicial = 50

class Graph:

    vertexs = []
    plays = 0
    lines = 0
    columns = 0
    index = 0

    def __init__(self):
        pass
    def create(self, lines, columns):
        self.lines = lines
        self.columns = columns
        self.total_vertexs = lines * columns

        valor_x = x_inicial
        valor_y = y_inicial
        for i in range(self.total_vertexs):
            vertex = {
                    'value': i,
                    'neighbors': [],
                    'clicked': {'left': 0, 'up': 0, 'down': 0, 'right': 0},
                    'axis':{'right': {'list': [], 'clicked': 0}, 'down': {'list': [], 'clicked': 0}}
                }
            self.vertexs.append(vertex)
        
        self.index = 0

        for y in range(0,lines*84,84):
            for x in range(0,columns*75,75):
                self.vertexs[self.index]['axis']['right']['list'].append(x)
                self.vertexs[self.index]['axis']['right']['list'].append(y)

                self.index = self.index + 1
                

        self.index = 0
        for x in range(0,columns*84,84):  
            for y in range(0,lines*75,75):
                self.vertexs[self.index]['axis']['down']['list'].append(y)
                self.vertexs[self.index]['axis']['down']['list'].append(x)

                self.index = self.index + 1


    def connect_egde(self, origin, destiny, orientation): #graph bidirected 
        self.vertexs[origin]['neighbors'].append(destiny)
        self.vertexs[destiny]['neighbors'].append(origin)
        if orientation == 'horizontal':
            self.vertexs[origin]['clicked']['right'] = 1
            self.vertexs[destiny]['clicked']['left'] = 1
        else:
            self.vertexs[origin]['clicked']['down'] = 1
            self.vertexs[destiny]['clicked']['up'] = 1

        self.plays = self.plays + 1
    
    def get_vertexs(self):
        return self.vertexs

    def get_lines(self):
        return self.lines
    
    def get_columns(self):
        return self.columns

    def get_vertex_count(self):
        return self.total_vertexs

	def get_vertexs_value(self):
		values = []
		for vertex in self.vertexs:
			values.append(vertex['value'])

		return values
    
    def get_number_plays(self):
        return self.plays

    def is_connected(self, origin, destiny):
        if not self.vertexs[origin]['neighbors'] == []:
            for element in self.vertexs[origin]['neighbors']:
                if element == destiny:
                    return True
        return False

    def print_graph(self):
        for vertex in self.vertexs:
            if vertex['neighbors'] != []:
                print vertex['value'],
                for neigh in vertex['neighbors']:
                    print ' ->', neigh,
                print('\n------------')

class Game:
    
    plays = []

    def __init__(self):
        pass


    def machine_action_easy(self, vertexs):
        
        #percorrer a lista de vertices e ir salvando as coordenadas das jogadas
        for vertex in vertexs:
            play = {
                'vertex': vertex['value'],
                'orientation': 'horizontal',
                'axis': vertex['axis']['right']['list']
            }
            self.plays.append(play)
           
        for vertex in vertexs:
            play = {
                'vertex': vertex['value'],
                'orientation': 'vertical',
                'axis': vertex['axis']['down']['list']
            }
            self.plays.append(play)

        # escolher um numero aleatorio para jogada    
        random = randint(0, len(self.plays) - 1)
        

        return self.plays[random]

#funcao tirada de: https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
    def dfs(self, graph, start):
        visited, stack = set(), [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(graph[vertex] - visited)
        return visited
###

    def points(self, vertexs):
        if
        pass
        
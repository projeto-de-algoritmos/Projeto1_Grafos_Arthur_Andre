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
                    'clicked': False,
                    'axis':{'right': [], 'down': []}
                }
            self.vertexs.append(vertex)
        
        self.index = 0

        for y in range(0,lines*84,84):
            for x in range(0,columns*75,75):
                self.vertexs[self.index]['axis']['right'].append(x)
                self.vertexs[self.index]['axis']['right'].append(y)

                self.index = self.index + 1
                

        self.index = 0
        for x in range(0,columns*84,84):  
            for y in range(0,lines*75,75):
                self.vertexs[self.index]['axis']['down'].append(y)
                self.vertexs[self.index]['axis']['down'].append(x)

                self.index = self.index + 1


    def connect_egde(self, origin, destiny): #graph bidirected 
        self.vertexs[origin]['neighbors'].append(destiny)
        self.vertexs[destiny]['neighbors'].append(origin)
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
                'axis': vertex['axis']['right']
            }
            self.plays.append(play)
           
        for vertex in vertexs:
            play = {
                'vertex': vertex['value'],
                'orientation': 'vertical',
                'axis': vertex['axis']['down']
            }
            self.plays.append(play)

        # escolher um numero aleatorio para jogada    
        random = randint(0, len(self.plays) - 1)
        

        return self.plays[random]


    def bfs(self):
        pass


    def search_edge(self, graph):
        pass

    def is_finish(self):
        











# grafo = Graph()
# grafo.create(5, 4, [])
# grafo.print_grid()
# grafo.connect_egde(4, 5)
# grafo.connect_egde(4, 3)
# grafo.connect_egde(4, 8)
# grafo.connect_egde(8, 3)

# grafo.print_list()

# g = Game()
# g.machine_action_easy(grafo.get_vertex())

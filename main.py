from random import randint

class Graph:
    
    vertexs = []

    def __init__(self):
        pass
    def create(self, lines, columns, axis):
        self.total_vertexs = lines * columns

        for i in range(self.total_vertexs):
            vertex = {
                'value': i,
                'neighbors': [],
                'clicked': False,
                'axis_x': 0,
                'axis_y': 0
            } 

        self.vertexs.append(vertex)

    def connect_egde(self, origin, destiny): #graph bidirected 
        self.vertexs[origin]['neighbors'].append(destiny)
        self.vertexs[destiny]['neighbors'].append(origin)
    
    def get_vertex(self):
        return self.total_vertexs

	def get_vertexs_value(self):
		values = []
		for vertex in self.vertexs:
			values.append(vertex['value'])

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


class Game:

    def __init__(self):
        pass

    def machine_action_easy(self, total_vertex, clicked):
        vertex = randint(0, total_vertex)

        if not clicked:






grafo = Graph()
grafo.create(5, 4, [])
# grafo.print_grid()
# grafo.connect_egde(4, 5)
# grafo.connect_egde(4, 3)
# grafo.connect_egde(4, 8)
# grafo.connect_egde(8, 3)

# grafo.print_list()

g = Game()
g.machine_action_easy(grafo.get_vertex(), clicked)

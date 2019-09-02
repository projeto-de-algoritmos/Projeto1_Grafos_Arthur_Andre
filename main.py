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
                'axis_y': 0,
            } 
            
            self.vertexs.append(vertex)
               

    def connect_egde(self, origin, destiny): #graph bidirected 
        self.vertexs[origin]['neighbors'].append(destiny)
        self.vertexs[destiny]['neighbors'].append(origin)
    
    def get_vertexs(self):
        return self.vertexs

    def get_vertex_count(self):
        return self.total_vertexs

	def get_vertexs_value(self):
		values = []
		for vertex in self.vertexs:
			values.append(vertex['value'])

		return values

    def is_connected(self, origin, destiny):
        if not self.vertexs[origin]['neighbors'] == []:
            for element in self.vertexs[origin]['neighbors']:
                if element == destiny:
                    return True
        return False
    
    def print_grid(self):
        for i in range(self.total_vertexs): 
            #print('{:02d}'.format(self.vertexs[i]['value']), ' ', end="")
            if i == 4 or i == 9 or i == 14:
                print('\n')

    # def print_list(self):
    #     print('\n\n\n -- adjacency list --\n')
    #     for vertex in self.vertexs:
    #         if not vertex['neighbors'] == []:
    #             print(vertex['value'], ' - > ', end="")
    #             # for neigh in vertex['neighbors']:
    #             #     print('{:02}'.format(neigh), ' - ', end="")
    #             print('\n')

    #     print('\n')


class Game:


    plays = [[0,1], [1,2], [2,3], [3,4], [5,6], [6,7], [7,8], [8,9], [10,11], [11,12], [12,13], [13,14], [15,16], [16,17], [17,18], [18,19], [20,21], [21,22], [22,23], [23,24], [25,26], [26,27], [27,28], [28,29], [0,5], [5,10], [10,15], [15,20], [20,25], [1,6], [6,11], [11,16], [16,21], [21,26], [2,7], [7,12], [12,17], [17,22], [22,27], [3,8], [8,13], [13,18], [18,23], [23,28], [4,9], [9,14], [14,19], [19,24], [24,29]]
    print("tamanho lista: ", len(plays))
    
    def __init__(self):
        pass


    def machine_action_easy(self, vertexs):
        random = randint(0, len(self.plays) - 1)
        print(random)
        return self.plays[random], random 

        if not connected:
            pass
    
    def random(self):
        return self.random






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

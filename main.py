class Graph:
    
    vertices = []

    def __init__(self):
        pass
    def create(self, lines, columns):
        self.total_vertex = lines * columns

        for i in range(self.total_vertex):
            vertice = {
                'value': i,
                'neighbors': []
            } 
            self.vertices.append(vertice)
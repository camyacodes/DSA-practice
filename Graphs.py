class Graph:
    def __init__(self):
        self.adj_list={}
    def print_graph(self):
        # if self.adj_list:
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        else:
            return False
    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        else:
            return False
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list[v2] and v2 in self.adj_list[v1]:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        else:
            return False
    def remove_vertex(self, v1):
        if v1 in self.adj_list:
            for vertex in self.adj_list[v1]:
                self.adj_list[vertex].remove(v1)
            del self.adj_list[v1]
        
my_graph = Graph()
my_graph.add_vertex(12)
my_graph.add_vertex(13)
my_graph.add_vertex('B')
my_graph.add_edge("B", 12)
my_graph.add_edge("B", 13)
# my_graph.remove_vertex(13)


my_graph.print_graph()
class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        self.adjacent_list[node] = []
        self.number_of_nodes += 1

    def add_edge(self, node1, node2):
        keys = self.adjacent_list.keys()
        if node1 in keys and node2 in keys:
            self.adjacent_list[node1].append(node2)
            self.adjacent_list[node2].append(node1)

    def show_connections(self):
        for node in self.adjacent_list.keys():
            node_connections = self.adjacent_list[node]
            connections = ''
            for vertex in node_connections:
                connections += vertex + ' '

            print('{} --> {}'.format(node, connections))

my_graph = Graph()
for i in range(7):
    my_graph.add_vertex(str(i))
my_graph.add_edge('3', '1')
my_graph.add_edge('3', '4')
my_graph.add_edge('4', '2')
my_graph.add_edge('4', '5')
my_graph.add_edge('1', '2')
my_graph.add_edge('1', '0')
my_graph.add_edge('0', '2')
my_graph.add_edge('6', '5')

my_graph.show_connections()
# Answer:
# 0-->1 2
# 1-->3 2 0
# 2-->4 1 0
# 3-->1 4
# 4-->3 2 5
# 5-->4 6
# 6-->5

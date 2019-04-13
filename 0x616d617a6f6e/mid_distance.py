
NEEDLE = 9

'''
nodes = [(x,y)]
edges = {(x,y): [(x,y),(x,y)]
distances = {(x,y): z}
'''
class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.distances = {}

    def add_node(self, node, value):
        self.nodes.append(node)
        self.distances[node] = value

    def add_edges(self, node, edges):
        self.edges[node] = edges

def get_edges(width, height, x, y):
    edges = []

    # left
    if x > 0:
        edges.append((x-1, y))

    # top
    if height > y:
        edges.append((x, y+1))

    # right
    if width > x:
        edges.append((x+1, y))

    # bottom
    if y > 0:
        edges.append((x, y-1))

    return edges

def min_distance(width, height, matrix):
    # create a graph
    g = Graph()
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            node = (x, y)
            g.add_node(node, value)

            edges = get_edges(width - 1, height - 1, x, y)
            g.add_edges(node, edges)

    # store visited nodes
    visited = []

    # store mid distance counter
    result = 0

    # queue root
    queue = [(0,0)]

    while queue:
        node = queue.pop()
        edges = g.edges[node]

        distance = g.distances[node]
        if distance == 1:
            result = result + 1

        print(node, distance, edges)

        # traverse breadth
        for edge in edges:
            distance = g.distances[edge]
            if edge not in visited:
                visited.append(edge)

                if g.distances[edge] == 1:
                    queue.append(edge)

            if distance == 9:
                return result

# matrix = [
#     [1,1,0],
#     [0,9,0],
#     [1,0,0]
# ]
# output = min_distance(3, 3, matrix)
# print(output)
#
# matrix = [
#     [1,1,1,1],
#     [0,1,1,1],
#     [0,1,0,1],
#     [1,1,9,1],
#     [0,0,1,1]
# ]
# output = min_distance(4, 5, matrix)
# print(output)

matrix = [
    [1,1,1,9,1,1,1,1],
    [0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1]
]
output = min_distance(8, 3, matrix)
print(output)
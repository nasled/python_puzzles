import queue
class Graph:
    def __init__(self, n):
        # create a list of edges
        # len(edges) = number of vertexes
        self.edges = [[] for i in range(n)]
        self.edges_count = n

    def connect(self, x, y):
        # biderectional, create 2 sets?
        self.edges[x].append(y)
        self.edges[y].append(x)

    def find_all_distances(self, s):
        q = queue.Queue()
        q.put(s)

        distances = [-1 for i in range(self.edges_count)]
        distances[s] = 0

        while not q.empty():
            node = q.get()
            for child in self.edges[node]:
                if distances[child] == -1:
                    distances[child] = distances[node] + 6
                    q.put(child)

        del distances[s]
        # distances.pop(s)
        print(" ".join(map(str, distances)))



# # number of nodes
# n = 4
# # edges
# m = [[1, 2], [1, 3]]
# # starting node
# s = 1

n = 6
m = [[1, 2], [2, 3], [3,4], [1,5]]
s = 1

graph = Graph(n)
for x, y in m:
    graph.connect(x - 1, y - 1)
graph.find_all_distances(s - 1)

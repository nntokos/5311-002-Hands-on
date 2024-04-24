# Hands on 14 - Implement source code for Bellman-Ford Algorithm.


class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

class Vertex:
    def __init__(self, data):
        self.data = data
        self.d = float('inf')
        self.p = None

def relax(u, v, w):
    if v.d > u.d + w:
        v.d = u.d + w
        v.p = u

def initialize_single_source(graph, s):
    for v in graph.vertices:
        v.d = float('inf')
        v.p = None
    s.d = 0

def bellman_ford(graph, s):
    initialize_single_source(graph, s)
    for i in range(len(graph.vertices) - 1):
        for (u, v) in graph.w.keys():
            relax(u, v, graph.w[(u, v)])
    for (u, v) in graph.w.keys():
        if v.d > u.d + graph.w[(u, v)]:
            return False
    return True

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = {}
        self.w = {}
        for v in vertices:
            self.adj[v] = []


    def add_edge(self, u, v, w):
        if not u in self.adj.keys():
            self.adj[u] = [v]
        else:
            self.adj[u].append(v)
        self.w[(u, v)] = w

    def __str__(self):
        print("\n ---Adjacency List ---")
        for v in self.adj.keys():
            print(v.data, end = ": ")
            for j in self.adj[v]:
                print(j.data, end = " ")
            print("\b")
        return "---End of Adjacency List ---\n"


if __name__ == "__main__":
    # Example from figure 24.4 of Chapter 24 of 2009 Introduction to Algorithms by Cormen et al.
    # s: 0, t: 1, x: 2, y: 3, z: 4

    vert = [Vertex(i) for i in range(5)]

    edges = [Edge(vert[0], vert[1], 6),
            Edge(vert[0], vert[3], 7),
            Edge(vert[1], vert[2], 5),
            Edge(vert[1], vert[3], 8),
            Edge(vert[1], vert[4], -4),
            Edge(vert[2], vert[1], -2),
            Edge(vert[3], vert[2], -3),
            Edge(vert[3], vert[4], 9),
            Edge(vert[4], vert[0], 2),
            Edge(vert[4], vert[2], 7)]

    graph = Graph(vert)
    for edge in edges:
        graph.add_edge(edge.u, edge.v, edge.w)
    for key in graph.w.keys():
        print(key, graph.w[key])
    print(len(graph.w.keys()))
    print(bellman_ford(graph, vert[0]))


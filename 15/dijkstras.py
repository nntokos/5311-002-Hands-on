# Hands on 14 - Implement source code for Dijkstra's Algorithm.


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

def extract_min(Q):
    min = Q[0]
    for v in Q:
        if v.d < min.d:
            min = v
    Q.remove(min)
    return min

def dijkstra(graph, s):
    initialize_single_source(graph, s)
    S = []
    Q = graph.vertices[:]
    while Q:
        u = extract_min(Q)
        S.append(u)
        for v in graph.adj[u]:
            relax(u, v, graph.w[(u, v)])
    return S

def get_shortest_path(v):
    path = []
    while v:
        path.append(v.data)
        v = v.p
    path.reverse()
    return path

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
    # Example from figure 24.6 of Chapter 24 of 2009 Introduction to Algorithms by Cormen et al.
    # s: 0, t: 1, x: 2, y: 3, z: 4

    vert = [Vertex(i) for i in range(5)]

    edges = [Edge(vert[0], vert[1], 10),
             Edge(vert[0], vert[3], 5),
             Edge(vert[1], vert[2], 1),
             Edge(vert[1], vert[3], 2),
             Edge(vert[2], vert[4], 4),
             Edge(vert[3], vert[1], 3),
             Edge(vert[3], vert[2], 9),
             Edge(vert[3], vert[4], 2),
             Edge(vert[4], vert[0], 7),
             Edge(vert[4], vert[2], 6)]
    graph = Graph(vert)
    for edge in edges:
        graph.add_edge(edge.u, edge.v, edge.w)
    S = dijkstra(graph, vert[0])
    print("Vertex | Dist | Path")
    print("---------------")
    for v in S:
        path = get_shortest_path(v)
        print(f" {v.data}     | {v.d}    | {'->'.join(map(str, path))}")


    vert = [Vertex(i) for i in range(7)]

    edges = [Edge(vert[0], vert[1], 4),
                Edge(vert[0], vert[2], 3),
                    Edge(vert[0], vert[4], 7),
                    Edge(vert[1], vert[2], 6),
                    Edge(vert[1], vert[3], 5),
                    Edge(vert[2], vert[3], 11),
                    Edge(vert[2], vert[4], 8),
                    Edge(vert[3], vert[4], 2),
                    Edge(vert[3], vert[5], 2),
                    Edge(vert[3], vert[6], 10),
                    Edge(vert[4], vert[6], 5),
                    Edge(vert[5], vert[6], 3)]
    graph = Graph(vert)
    for edge in edges:
        graph.add_edge(edge.u, edge.v, edge.w)
    S = dijkstra(graph, "A")
    print("Vertex | Dist | Path")
    print("---------------")
    for v in S:
        path = get_shortest_path(v)
        print(f" {v.data}     | {v.d}    | {'->'.join(map(str, path))}")



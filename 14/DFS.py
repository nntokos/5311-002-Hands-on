# Hands on 14 - Implement source code for Depth-First Search.
# Vertices have white color (0) for not visited, gray (1) for discovered and black (2) for finished.
import random
import sys, os
sys.path.insert(0, os.path.realpath("../10")) # Importing doubly_linked_list.py from Hands-on 10
import doubly_linked_list as dll

class Vertex:
    def __init__(self, data):
        self.data = data
        self.color = 0
        self.dt = 0
        self.ft = 0
        self.predecessor = None

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = {}
        self.time = 0

    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = [v]
        else:
            self.adj[u].append(v)

    def add_vertex(self, vertex):
        self.adj[vertex] = []

    def DFS(self):
        for v in self.adj.keys():
            v.color = 0
            v.predecessor = None
        self.time = 0
        for v in self.adj.keys():
            if v.color == 0:
                self.DFS_Visit(v)
    def DFS_Visit(self, vertex):
        self.time += 1
        vertex.dt = self.time
        vertex.color = 1
        for v in self.adj[vertex]:
            if v.color == 0:
                v.predecessor = vertex
                self.DFS_Visit(v)
        vertex.color = 2
        self.time += 1
        vertex.ft = self.time

    def __str__(self):
        print("\n ---Adjacency List ---")
        for v in self.adj.keys():
            print(v.data, end = ": ")
            for j in self.adj[v]:
                print(j.data, end = " ")
            print("\b")
        return "---End of Adjacency List ---\n"

if __name__ == "__main__":
    # Example from figure 22.4 of Chapter 22 of 2009 Introduction to Algorithms by Cormen et al.
    graph = Graph(6)
    u, v, w, x, y, z = Vertex('u'), Vertex('v'), Vertex('w'), Vertex('x'), Vertex('y'), Vertex('z')
    graph.add_edge(u, v)
    graph.add_edge(u, x)
    graph.add_edge(x, v)
    graph.add_edge(v, y)
    graph.add_edge(y, x)
    graph.add_edge(w, y)
    graph.add_edge(w, z)
    graph.add_edge(z, z)

    graph.DFS()
    print("DFS: ", end = "")
    # print DFS with times
    for i in graph.adj.keys():
        print(f"{i.data} ({i.dt}/{i.ft}),", end = " ")





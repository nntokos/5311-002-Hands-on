# Hands on 14 - Implement source code for Kruskal Algorithm
# Vertices have white color (0) for not visited, gray (1) for discovered and black (2) for finished.

import sys, os

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

def sort_edges(edges): # edges is a list of E
    return sorted(edges, key = lambda x: x.w)

class Vertex:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [1] * size

    def find(self, u):
        if self.root[u] != u:
            self.root[u] = self.find(self.root[u])
        return self.root[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return
        if self.rank[root_u] > self.rank[root_v]:
            self.root[root_v] = root_u
        else:
            self.root[root_u] = root_v
            if self.rank[root_u] == self.rank[root_v]:
                self.rank[root_v] += 1

def kruskal_algorithm(edges):
    """

    :param edges: The list of edges in the graph
    :return: The list of edges in the minimum spanning tree
    """
    edges = sort_edges(edges)
    vertices = Vertex(len(edges))
    mst = []
    for edge in edges:
        if vertices.find(edge.u) != vertices.find(edge.v):
            mst.append(edge)
            vertices.union(edge.u, edge.v)
    return mst



if __name__ == "__main__":
    # Example from figure 23.4 of Chapter 23 of 2009 Introduction to Algorithms by Cormen et al.
    # 0: a, 1: b, 2: c, 3: d, 4: e, 5: f, 6: g, 7: h, 8: i
    edges = [Edge(0, 1, 4),
             Edge(0, 7, 8),
             Edge(1, 2, 8),
             Edge(1, 7, 11),
             Edge(2, 3, 7),
             Edge(2, 8, 2),
             Edge(2, 5, 4),
             Edge(3, 4, 9),
             Edge(3, 5, 14),
             Edge(4, 5, 10),
             Edge(5, 6, 2),
             Edge(6, 7, 1),
             Edge(6, 8, 6),
             Edge(7, 8, 7)]

    mst = kruskal_algorithm(edges)
    print("Edge | Weight")
    print("------------")
    for edge in mst:
        print(f"{edge.u}-{edge.v}  |   {edge.w}")
    print("------------")

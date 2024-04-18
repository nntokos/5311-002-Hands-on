# Hands on 14 - Implement source code for Topological Sort using DFS. Assume graph is directed and acyclic.
# Vertices have white color (0) for not visited, gray (1) for discovered and black (2) for finished.

import sys, os
sys.path.insert(0, os.path.realpath("../10")) # Importing doubly_linked_list.py from Hands-on 10

from DFS import Vertex, Graph

def topological_sort(graph):
    graph.DFS()
    print("DFS: ", end = "")
    for v in graph.adj.keys():
        print(f"{v.data} ({v.dt}/{v.ft}),", end = " ")
    # Sorting the vertices in decreasing order of finish time
    sorted_vertices = sorted(graph.adj.keys(), key = lambda x: x.ft, reverse = True)
    print("\nTopological Sort: ", end = "")
    for i in sorted_vertices:
        print(f"{i.data} ({i.ft}),", end = " ")
    print("\b")

if __name__ == "__main__":
    # Example from figure 22.7 of Chapter 22 of 2009 Introduction to Algorithms by Cormen et al.
    graph = Graph(9)

    undershorts = Vertex("undershorts")
    pants = Vertex("pants")
    belt = Vertex("belt")
    shirt = Vertex("shirt")
    tie = Vertex("tie")
    jacket = Vertex("jacket")
    socks = Vertex("socks")
    shoes = Vertex("shoes")
    watch = Vertex("watch")
    for v in [shirt, tie, jacket, belt, watch, undershorts, pants, shoes, socks]:
        graph.add_vertex(v)
    graph.add_edge(undershorts, pants)
    graph.add_edge(undershorts, shoes)
    graph.add_edge(pants, shoes)
    graph.add_edge(pants, belt)
    graph.add_edge(shirt, tie)
    graph.add_edge(tie, jacket)
    graph.add_edge(shirt, belt)
    graph.add_edge(belt, jacket)
    graph.add_edge(socks, shoes)


    topological_sort(graph)




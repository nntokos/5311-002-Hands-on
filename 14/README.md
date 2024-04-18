# CSE 5311-002 - Hands On 14

### __System Specifications__
* CPU: Apple M1 Pro 10 cores @ 2.06-3.22 GHz
* RAM: 16 GB LPDDR5
* OS: MacOS Sonoma 14.3.1
* Python version: 3.9.7

### A. Topological sort

1. __Command to run the code__
    ```
    python3 topo_sort.py
    ```

2. __Functionality__

    The topological sort is implemented using classes `Vertex` and `Graph` (imported from DFS.py) with the following attributes and functions:
    <br /><u>**Graph**</u>
    * ***Attributes***
      * `adj`: The adjacency list of the graph.
      * `vertices`: The number of vertices of the graph.
      * `time`: The current time of the graph.
    * ***Functions***
      * `add_edge`: Adds an edge to the graph.
      * `add_vertex`: Adds a vertex to the graph. This is used for vertices that are not connected to any other vertex.
      * `get_vertex`: Returns the vertex with the given data.
      * `DFS`: Performs the depth-first search on the graph.
      * `DFS_visit`: Visits the vertex and its neighbors.
   <br /><u>**Vertex**</u>
    * ***Attributes***
      * `data`: The data of the vertex.
      * `color`: The color of the vertex (white, gray, black).
      * `predecessor`: The predecessor of the vertex.
      * `discovery`: The discovery time of the vertex.
      * `dt`: The discovery time of the vertex.
      * `ft`: The finish time of the vertex.
    <br />There is also a `topological_sort` function that calls the `DFS` function to perform the topological sort.
3. __Output__
   <br />Using the example from figure 22.7 of Chapter 22 of 2009 Introduction to Algorithms by Cormen et al. I get the following output

    ```
   DFS: shirt (1/8), tie (2/5), jacket (3/4), belt (6/7), watch (9/10), undershorts (11/16), pants (12/15), shoes (13/14), socks (17/18), 
   Topological Sort: socks (18), undershorts (16), pants (15), shoes (14), watch (10), shirt (8), belt (7), tie (5), jacket (4),
    ```
    The graph is sorted by finish time in descending order. The finish time is the time at which the vertex is marked black. The vertices are visited in the order watch, socks, shirt, tie, undershorts, pants, belt, jacket, shoes. The topological sort is watch, socks, shirt, tie, undershorts, pants, belt, jacket, shoes.

### B. Depth-First Search

1. __Command to run the code__
    ```
    python3 DFS.py
    ```
   
2. __Functionality__
    
    The DFS is implemented using classes `Vertex` and `Graph` (same as above) with the following attributes and functions:
    <br /><u>**Graph**</u>
    * ***Attributes***
      * `adj`: The adjacency list of the graph.
      * `vertices`: The number of vertices of the graph.
      * `time`: The current time of the graph.
    * ***Functions***
      * `add_edge`: Adds an edge to the graph.
      * `add_vertex`: Adds a vertex to the graph. This is used for vertices that are not connected to any other vertex.
      * `DFS`: Performs the depth-first search on the graph.
      * `DFS_visit`: Visits the vertex and its neighbors.
   <br /><u>**Vertex**</u>
    * ***Attributes***
      * `data`: The data of the vertex.
      * `color`: The color of the vertex (white, gray, black).
      * `predecessor`: The predecessor of the vertex.
      * `discovery`: The discovery time of the vertex.
      * `dt`: The discovery time of the vertex.
      * `ft`: The finish time of the vertex.
3. __Output__
    <br />Using the example from figure 22.4 of Chapter 22 of 2009 Introduction to Algorithms by Cormen et al. I get the following output

    ```
    DFS: u (1/8), x (4/5), v (2/7), y (3/6), w (9/12), z (10/11)
    ```
   The finish time is the time at which the vertex is marked black. The vertices are visited in the order u, x, v, y, w, z.


### C. Kruskal algorithm

1. __Command to run the code__
    ```
    python3 kruskal_algorithm.py
    ```
   
2. __Functionality__
    The AVL tree is implemented using a `class Edge` and `class Vertex` with the following attributes and functions:
    <br /><u>**Edge**</u>
    * ***Attributes***
         * `u`: The first vertex of the edge.
         * `v`: The second vertex of the edge.
         * `w`: The weight of the edge.
        
   <br /><u>**Vertex**</u>
    * ***Attributes***
      * `root`: The root of the vertex.
      * `rank`: The rank of the vertex.
   * ***Functions***
      * `make_set`: Creates a set with the vertex as the root and rank 0.
      * `find`: Finds the set to which the vertex belongs.
      * `union`: Merges two sets.
     
   <br /><u>**Kruskal**</u>
     <br />Performs the Kruskal algorithm on the graph.<br />
   
    
3. __Output__
    <br />Using the example from figure 23.4 of Chapter 23 of 2009 Introduction to Algorithms by Cormen et al. I get the following output

    ```
    Edge | Weight
   ------------
   6-7  |   1
   2-8  |   2
   5-6  |   2
   0-1  |   4
   2-5  |   4
   2-3  |   7
   0-7  |   8
   3-4  |   9
   ------------
    ```

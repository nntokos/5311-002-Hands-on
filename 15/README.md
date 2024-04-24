# CSE 5311-002 - Hands On 15

### __System Specifications__
* CPU: Apple M1 Pro 10 cores @ 2.06-3.22 GHz
* RAM: 16 GB LPDDR5
* OS: MacOS Sonoma 14.4.1
* Python version: 3.9.7

### A. Dijkstra's Algorithm

1. __Command to run the code__
    ```
    python3 dijkstras.py
    ```

2. __Functionality__

    To implement Dijkstra's algorithm we use the classes `Edge`, `Vertex` and `Graph` with the following attributes and functions:
<br /><u>**Edge**</u>
   * ***Attributes***
     * `u`: The first vertex of the edge.
     * `v`: The second vertex of the edge.
     * `w`: The weight of the edge.
     
   <br /><u>**Vertex**</u>
   * ***Attributes***
     * `data`: The data of the vertex.
     * `d`: The distance of the vertex from the source.
     * `p`: The predecessor of the vertex.

   <br /><u>**Graph**</u>
   * ***Attributes***
     * `adj`: The adjacency list of the graph.
     * `vertices`: The number of vertices of the graph.
     * `w`: The weight of the graph.
   * ***Functions***
     * `add_edge`: Adds an edge to the graph.
       
    <br /><u>**Dijkstra's Algorithm**</u>
   * ***Functions***
     * `initialize_single_source`: Initializes the graph with the source vertex.
     * `extract_min`: Extracts the minimum distance vertex.
     * `relax`: Relaxes the edge for each vertex of the minimum distance vertex (from `extract_min`).
     * `dijkstra`: Performs Dijkstra's algorithm on the graph.


3. __Output__
   <br />Using the example from figure 24.6 of Chapter 24 of 2009 Introduction to Algorithms by Cormen et al. I get the following output

    ```
   Vertex | Distance
   ---------------
   0  |  0
   3  |  5
   4  |  7
   1  |  8
   2  |  9
    ```
   For one source we have multiple destinations and their minimum distance from the source.

### B. Bellman-Ford Algorithm

1. __Command to run the code__
    ```
    python3 bellman_ford.py
    ```

2. __Functionality__

    Very similar to Dijkstra's algorithm but instead of returning distances it returnes a boolean value of whether the graph contains no negative-weight cycles reachable from the source
   We again use the classes `Edge`, `Vertex` and `Graph` with the following attributes and functions:
<br /><u>**Edge**</u>
   * ***Attributes***
     * `u`: The first vertex of the edge.
     * `v`: The second vertex of the edge.
     * `w`: The weight of the edge.
     
   <br /><u>**Vertex**</u>
   * ***Attributes***
     * `data`: The data of the vertex.
     * `d`: The distance of the vertex from the source.
     * `p`: The predecessor of the vertex.

   <br /><u>**Graph**</u>
   * ***Attributes***
     * `adj`: The adjacency list of the graph.
     * `vertices`: The number of vertices of the graph.
     * `w`: The weight of the graph.
   * ***Functions***
     * `add_edge`: Adds an edge to the graph with (u, v, w).
       
    <br />However, the algorithm is a little different
    <br /><u>**Bellman-Ford Algorithm**</u>
   * ***Functions***
     * `initialize_single_source`: Initializes the graph with the source vertex.
     * `relax`: Relaxes the edge for each vertex.
     * `bellman_ford`: Performs Bellman-Ford algorithm on the graph.


3. __Output__
   <br />Using the example from figure 24.4 of Chapter 24 of 2009 Introduction to Algorithms by Cormen et al. I get the output of:
    ```
   True
    ```
   which means that the graph contains no negative-weight cycles reachable from the source.


### C. Floyd Warshall algorithm
For the Floyd Warshall algorithm, the implementation did not require any classes. The algorithm is essentialy one function with an input array `W` as an argument.
We decided to implement the algorithm  in two different ways, a simple one and a recursive one.
Both algorithms run under the same script.
1. __Command to run the code__
    ```
    python3 floyd_warshall.py
    ```
   
2. __Functionality__
    The AVL tree is implemented using a `class Edge` and `class Vertex` with the following attributes and functions:
    <br /><u>**Simple**</u>
    * ***Function***
        * `floyd_warshall`: The simple implementation of the Floyd Warshall algorithm. Implemented using the book's pseudocode.
      * ***Input***
        * `W`: The adjacency matrix of the graph.
    
    <br /><u>**Recursive**</u>
    * ***Function***
        * `floyd_warshall_recursive`: The recursive implementation of the Floyd Warshall algorithm. Implemented using the book's pseudocode.
      * ***Input***
        * `W`: The adjacency matrix of the graph.
        * `k`: Since this method is recursive, each call calculates a new D matrix. So this value holds the number. This is the recursions knows when to end. 
    
    <br /><i><u>Note</u></i>: numpy was used for ease of matrix operations.<br />
   

3. __Output__
    <br />Using the example from figure 25.4 of Chapter 25 of 2009 Introduction to Algorithms by Cormen et al. we get the following output for input array W:
    ```
    Simple Floyd-Warshall
    [[ 0.  1. -3.  2. -4.]
     [ 3.  0. -4.  1.  7.]
     [ 7.  4.  0.  5. 11.]
     [ 2. -1. -5.  0.  6.]
     [ 8.  5.  1.  6.  0.]]
    
    Recursive Floyd-Warshall
    [[ 0.  1. -3.  2. -4.]
     [ 3.  0. -4.  1. -1.]
     [ 7.  4.  0.  5.  3.]
     [ 2. -1. -5.  0. -2.]
     [ 8.  5.  1.  6.  0.]]
    ```

   As expected both algorithms return the same result.

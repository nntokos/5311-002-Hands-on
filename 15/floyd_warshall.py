# Hands on 14 - Implement source code for Floyd-Warshall Algorithm.
from typing import List

import numpy as np

def floyd_warshall(W: List[List[int]]):
    W = np.array(W)
    n = len(W)
    D = np.array([[[float(0) for _ in range(n)] for _ in range(n)] for _ in range(n)])
    D[0] = W
    for k in range(0, n-1):
        km = k + 1
        for i in range(0, n):
            for j in range(0, n):
                D[km][i][j] = min(D[km - 1][i][j], D[km - 1][i][k] + D[km - 1][k][j])

        print(f"\nD{km}")
        print(D[km])
    return D[n - 1]

# floyd_warshall recursively
def floyd_warshall_recursive(W: List[List[int]], k: int):
    n = len(W)
    Dk = [[float(0) for _ in range(n)] for _ in range(n)]
    Dk = np.array(Dk)
    for i in range(n):
        for j in range(n):
            Dk[i][j] = min(W[i][j], W[i][k] + W[k][j])
    if k == n-1:
        return Dk
    print(f"\nD{k+1}")
    print(Dk)
    return floyd_warshall_recursive(Dk, k + 1)

def construct_parent_matrix(W: List[List[int]]):
    n = len(W)
    P = [[float(0) for _ in range(n)] for _ in range(n)]
    P = np.array(P)
    for i in range(n):
        for j in range(n):
            if i != j and W[i][j] != float('inf'):
                P[i][j] = i
            else:
                P[i][j] = None
    return P

if __name__ == "__main__":
    # Example from figure 25.4 of Chapter 25 of 2009 Introduction to Algorithms by Cormen et al.
    W = [[0, 3, 8, float('inf'), -4],
        [float('inf'), 0, float('inf'), 1, 7],
        [float('inf'), 4, 0, float('inf'), float('inf')],
        [2, float('inf'), -5, 0, float('inf')],
        [float('inf'), float('inf'), float('inf'), 6, 0]]

    W=np.array(W)
    print("\nSimple Floyd-Warshall")
    print("\nFinal\n", floyd_warshall(W))
    print("\nRecursive Floyd-Warshall")
    print("\nFinal\n", floyd_warshall_recursive(W, 0))

    print("\nParent Matrix")
    print(construct_parent_matrix(W))



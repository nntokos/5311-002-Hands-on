# Hands on 14 - Implement source code for Floyd-Warshall Algorithm.
from typing import List

import numpy as np

def floyd_warshall(W: List[List[int]]):
    W = np.array(W)
    n = len(W)
    D = np.array([[[float(0) for _ in range(n)] for _ in range(n)] for _ in range(n)])
    D[0] = W
    for k in range(1, n):
        for i in range(n):
            for j in range(n):
                D[k][i][j] = min(D[k - 1][i][j], D[k - 1][i][k] + D[k - 1][k][j])
    return D[n - 1]

# floyd_warshall recursively
def floyd_warshall_recursive(W: List[List[int]], k: int):
    n = len(W)
    W_new = [[float(0) for _ in range(n)] for _ in range(n)]
    W_new = np.array(W_new)
    for i in range(n):
        for j in range(n):
            W_new[i][j] = min(W[i][j], W[i][k] + W[k][j])
    if k == n-1:
        return W_new
    return floyd_warshall_recursive(W_new, k + 1)

if __name__ == "__main__":
    # Example from figure 25.4 of Chapter 25 of 2009 Introduction to Algorithms by Cormen et al.
    W = [[0, 3, 8, float('inf'), -4],
        [float('inf'), 0, float('inf'), 1, 7],
        [float('inf'), 4, 0, float('inf'), float('inf')],
        [2, float('inf'), -5, 0, float('inf')],
        [float('inf'), float('inf'), float('inf'), 6, 0]]

    W=np.array(W)
    print("\nSimple Floyd-Warshall")
    print(floyd_warshall(W))
    print("\nRecursive Floyd-Warshall")
    print(floyd_warshall_recursive(W, 0))




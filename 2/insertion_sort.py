# Hands on 2 - Insertion Sort

import random
import tracemalloc
import timeit

A = [5, 2, 4, 6, 1, 3]
B = [31, 41, 59, 26, 41, 58, 32, 97, 93, 12]
C = [random.randint(1, 2^16) for i in range(1, pow(2, 16))] # Array with 2^16 (65,536) random elements

def insertion_sort(array):
    # tracemalloc.start() # Uncomment this line to trace memory usage
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key
    # print(tracemalloc.get_traced_memory()) # Uncomment this line to trace memory usage
    # tracemalloc.stop() # Uncomment this line to trace memory usage


if __name__ == '__main__':
    print("Insertion Sort")
    tA = timeit.timeit(lambda: insertion_sort(A), number=1)
    print('tA: ', tA)

    tB = timeit.timeit(lambda: insertion_sort(B), number=1)
    print('tB: ', tB)

    tC = timeit.timeit(lambda: insertion_sort(C), number=1)
    print('tC: ', tC)

# Hands on 2 - Insertion Sort

import random
import time
import tracemalloc

A = [5, 2, 4, 6, 1, 3]
B = [31, 41, 59, 26, 41, 58, 32, 97, 93, 12]
C = [random.randint(1, 2^16) for i in range(1, pow(2, 16))] # Array with 2^16 (65,536) random elements

def insertion_sort(array):
    tracemalloc.start()
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()


if __name__ == '__main__':
    print("Insertion Sort")
    print("Unsorted A: ",A)
    tA = time.time()
    insertion_sort(A)
    tA = time.time() - tA
    print("Sorted A: ",A)
    print('tA: ', tA)

    tB = time.time()
    insertion_sort(B)
    tB = time.time() - tB
    print('tB: ', tB)

    tC = time.time()
    insertion_sort(C)
    tC = time.time() - tC
    print('tC: ', tC)

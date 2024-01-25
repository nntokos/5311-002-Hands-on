# Hands on 2 - Bubble Sort

import random
import time
import tracemalloc

A = [5, 2, 4, 6, 1, 3]
B = [31, 41, 59, 26, 41, 58, 32, 97, 93, 12]
C = [random.randint(1, 2^16) for i in range(1, pow(2, 16))] # Array with 2^16 (65,536) random elements

def bubble_sort(array):
    tracemalloc.start()
    for i in range(len(array)):
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[j - 1]:
                temp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = temp
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()


if __name__ == '__main__':
    print("Bubble Sort")
    tA = time.time()
    bubble_sort(A)
    tA = time.time() - tA
    print('A: ', tA)

    tB = time.time()
    bubble_sort(B)
    tB = time.time() - tB
    print('B: ', tB)

    tC = time.time()
    bubble_sort(C)
    tC = time.time() - tC
    print('C: ', tC)

# Hands on 2 - Selection Sort

import random
import timeit
import tracemalloc

def divide(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        return left, right

def merge(array, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

def merge_sort(array):
    # tracemalloc.start() # Uncomment this line to trace memory usage
    if len(array) > 1:
        left, right = divide(array)
        merge_sort(left)
        merge_sort(right)
        merge(array, left, right)
    # print(f"merge_sort_called: {merge_sort_called}")
    # print(tracemalloc.get_traced_memory()) # Uncomment this line to trace memory usage
    # tracemalloc.stop() # Uncomment this line to trace memory usage

if __name__ == '__main__':
    print("Merge Sort")
    A = [5, 2, 4, 7, 1, 3, 2, 6]
    tA = timeit.timeit(lambda: merge_sort(A), number=1)
    print("A: ", A)
    print('tA: ', tA)


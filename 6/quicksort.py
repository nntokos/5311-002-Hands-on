# Hands on 6 - Quick Sort
import math
import timeit
import random
import copy
import argparse
import sys

sys.setrecursionlimit(10010)  # Increase the recursion limit to 10010

def quicksort(arr, low, high, random_pivot=False):
    if low < high:
        pivot = partition(arr, low, high, random_pivot)
        quicksort(arr, low, pivot-1)
        quicksort(arr, pivot+1, high)

def partition(arr, low, high, random_pivot=False):
    if random_pivot: # Random selection of pivot in case random_pivot is True
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def fillBestCaseQuicksortArray(arr, low, high): # Explanation in the README
    if low < high:
        mid = (low + high) // 2 # Mid element is selected as pivot
        arr.insert(0, mid) # The pivot is added to the beginning of the array.
        fillBestCaseQuicksortArray(arr, mid+1, high)
        fillBestCaseQuicksortArray(arr, low, mid-1)


if __name__ == '__main__':
    # Parse random_pivot argument
    parser = argparse.ArgumentParser()
    parser.add_argument('--random_pivot', default=True, action='store_true')
    args = parser.parse_args()
    random_pivot = args.random_pivot

    n = 100

    # Worst case scenario
    worst_array = [i for i in range(n, 0, -1)]
    print("Worst Array:", worst_array)
    tWorst = timeit.timeit(lambda: quicksort(worst_array, 0, len(worst_array) - 1, random_pivot=random_pivot), number=1)
    print("Worst Array after sorting:", worst_array)

    # #Average case scenario
    avg_array = [random.randint(0, n) for i in range(n)]
    print("Average Array:", avg_array)
    tAvg = timeit.timeit(lambda: quicksort(avg_array, 0, len(avg_array) - 1, random_pivot=random_pivot), number=1)
    print("Average Array after sorting:", avg_array)

    # Best case scenario
    best_array = []
    fillBestCaseQuicksortArray(best_array, 0, n + 2**int(math.log2(n)) - 1)
    print("Best Array:", best_array)
    tBest = timeit.timeit(lambda: quicksort(best_array, 0, len(best_array) - 1, random_pivot=random_pivot), number=1)
    print("Best Array after sorting:", best_array)

    print('tWorst: ', tWorst)
    print('tAvg: ', tAvg)
    print('tBest: ', tBest)



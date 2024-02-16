# Hands on 5 - Min Heap

import timeit
import tracemalloc


heap = []

def parent(i):
    return (i-1)//2

def left(i):
    return 2*i

def right(i):
    return 2*i + 1

def build_min_heap(arr):
    for i in range(len(arr)//2, -1, -1):
        min_heapify(arr, i)


def min_heapify(heap, i):
    smallest = i
    if left(i) < len(heap) and heap[left(i)] < heap[smallest]:
        smallest = left(i)
    if right(i) < len(heap) and heap[right(i)] < heap[smallest]:
        smallest = right(i)
    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        min_heapify(heap, smallest)

def min_heappop(heap):
    if len(heap) == 1:
        return heap.pop()
    min_element = heap[0]
    heap[0] = heap.pop()
    min_heapify(heap, 0)
    return min_element

if __name__ == '__main__':
    int_array = [19, 14, 15, 10, 26, 33, 55, 17]
    float_array = [19.5, 14.3, 15.2, 10.1, 26.4, 33.7, 55.6, 17.8]
    char_array = ['s', 'a', 'y', 'e', 'd', 'a', 'l', 'i']
    print("Int Array:", int_array)
    build_min_heap(int_array)
    print("Int Min Heap", int_array)

    print("Float Array:", float_array)
    build_min_heap(float_array)
    print("Float Min Heap", float_array)

    print("Char Array:", char_array)
    build_min_heap(char_array)
    print("Char Min Heap", char_array)

    min_heappop(int_array)
    print("Int Min Heap after popping the first element", int_array)



# Hands on 4 - Problem 1

import timeit
import tracemalloc

heap = []
def heapify(heap, i):
    left = 2*i + 1
    right = 2*i + 2
    smallest = i
    if left < len(heap) and heap[left][0] < heap[smallest][0]:
        smallest = left
    if right < len(heap) and heap[right][0] < heap[smallest][0]:
        smallest = right
    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        heapify(heap, smallest)

def heappop(heap):
    if len(heap) == 1:
        return heap.pop()
    min_element = heap[0]
    heap[0] = heap.pop()
    heapify(heap, 0)
    return min_element

def heappush(heap, element):
    heap.append(element)
    i = len(heap) - 1
    if i == 0:
        return
    parent = (i-1)//2
    if heap[parent][0] > heap[i][0]:
        heap[parent], heap[i] = heap[i], heap[parent]
        heappush(heap, parent)


def merge_k_arrays(arrays):
    for i in range(len(arrays)): # c1*(k+1)
        heap.append((arrays[i][0], i, 0)) # c2*k
    for i in range(len(heap)//2, -1, -1): # c3*(k+1)/2
        heapify(heap, i) # c4*k*log(k)/2
    sorted_array = []
    while heap: # c5*(k*n+1)
        min_element, i, j = heappop(heap) # c6*k*n*log(k)
        sorted_array.append(min_element) # c7*k*n
        if j+1 < len(arrays[i]): # c8*k*n
            heappush(heap, (arrays[i][j+1], i, j+1)) # c9*k*n*log(k)
    return sorted_array

if __name__ == '__main__':
    array1 = [1, 3, 5, 7]
    array2 = [2, 4, 6, 8]
    array3 = [0, 9, 10, 11]
    print("Merge Arrays: ", array1, array2, array3)
    A = merge_k_arrays([array1, array2, array3])
    print("A: ", A)


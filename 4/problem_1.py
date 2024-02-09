# Hands on 4 - Problem 1

import timeit
import tracemalloc

#
# def merge(arrays):
#     # Pointers to the current element being compared of each array
#     pointers = [0]*len(arrays) # - c1
#     current_min = arrays[0][pointers[0]] # - c2
#     current_min_array = 0 # - c3
#     sorted_array = [] # - c4
#     while sum(pointers) < len(arrays)*len(arrays[0]): # - c5*(k*n+1) where k is the number of arrays and n is the number of elements in each array
#         # Find the first pointer that is not at the end of the array and set the array element as the current minimum
#         for j in range(len(pointers)): # - c6*k*n*(k+1)
#             if pointers[j] < len(arrays[j]): # - c7*k*n*k
#                 current_min = arrays[j][pointers[j]]
#                 current_min_array = j
#                 break
#         # Find the minimum of between the elements that the pointers point to and have not been already added to the sorted array
#         for i in range(len(pointers)): # - c8*k*n*(k+1)
#             if pointers[i] < len(arrays[i]) and current_min > arrays[i][pointers[i]]: # - c9*k*n*k
#                 current_min = arrays[i][pointers[i]]
#                 current_min_array = i
#         # Move the pointer of the array that had the minimum element
#         pointers[current_min_array] += 1 # - c10*k*n
#         # Add the current minimum element to the sorted array
#         sorted_array.append(current_min) # - c11*k*n
#
#     return sorted_array

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


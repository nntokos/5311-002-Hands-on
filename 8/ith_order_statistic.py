# Hands on 8 - Find ith order statistic using quicksort implementation
import random


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)


def find_ith_order_statistic(arr, low, high, i):
    if low < high:
        pivot = partition(arr, low, high)
        if pivot < i - 1:
            return find_ith_order_statistic(arr, pivot + 1, high, i)
        elif pivot > i - 1:
            return find_ith_order_statistic(arr, low, pivot - 1, i)
        else:
            return arr[pivot]
    return arr[low]


if __name__ == '__main__':
    array = [random.randint(0, 100) for i in range(10)] # Random array with 10 elements [0-100]
    i = random.randint(1, len(array)) # Random selection of i

    print("Array:", array)
    print(f"Search for {i}th order statistic:")
    print(f"{i}th order statistic:", find_ith_order_statistic(array, 0, len(array) - 1, i))

    # Validation of the ith order statistic
    quicksort(array, 0, len(array) - 1)
    print(f"Actual {i}th order statistic: ", array[i - 1])

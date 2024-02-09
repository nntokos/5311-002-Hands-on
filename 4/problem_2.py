# Hands on 4 - Problem 2

def remove_duplicates(array):
    for i in range(len(array)-1, 0, -1): # - c1*(n+1)
        if array[i] == array[i-1]: # - c2*n
            array.pop(i)

if __name__ == '__main__':
    array = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    print("Remove Duplicates from Array: ", array)
    remove_duplicates(array)
    print("A: ", array)


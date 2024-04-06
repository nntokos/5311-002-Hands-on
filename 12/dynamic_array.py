# Hands on 12 - Implement source code for a dynamic array. C Style arrays only allowed. Assume datatype is integer.

class DynamicArray:
    def __init__(self, capacity = 1):
        if capacity < 1:
            print("Capacity should be greater than 0. Setting capacity to 1")
            capacity = 1
        self.count = 0
        self.capacity = capacity
        self.array = [None] * self.capacity

    def increase_capacity(self):
        self.capacity *= 2
        new_array = [0] * self.capacity
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array

    def insert(self, data, index = None):
        if self.count == self.capacity:
            self.increase_capacity()
        if index is not None: # Insert at index
            if index < 0 or index >= self.count:
                print("Index out of range. Current Range: 0 -", self.count - 1)
                return
            for i in range(self.count, index, -1):
                self.array[i] = self.array[i - 1]
            self.array[index] = data
            self.count += 1
            return
        else: # Append at the end
            self.array[self.count] = data
            self.count += 1

    def delete(self, index):
        if index < 0 or index >= self.count:
            print("Index out of range. Current Range: 0 -", self.count - 1)
            return
        for i in range(index, self.count - 1):
            self.array[i] = self.array[i + 1]
        self.count -= 1

    def itemAt(self, index):
        if index < 0 or index >= self.count:
            print("Index out of range. Current Range: 0 -", self.count - 1)
            return
        return self.array[index]

    def print_array(self):
        print("Array: [", end = "")
        for i in range(self.count):
            print(self.array[i], end = " ")
        print("\b]")
        print("Capacity: ", self.capacity, end = "\n\n")


if __name__ == "__main__":
    da = DynamicArray(5)
    print("Inserting 10, 20, 30, 40, 50 at the end")
    da.insert(10)
    da.insert(20)
    da.insert(30)
    da.insert(40)
    da.insert(50)
    da.print_array()
    print("Inserting 60, 70, 80, 90, 100 at index 3")
    da.insert(60, 3)
    da.insert(70, 3)
    da.insert(80, 3)
    da.insert(90, 3)
    da.insert(100, 3)
    da.print_array()
    print("itemAt(5): ", da.itemAt(5))
    print("Deleting item at index 5")
    da.delete(5)
    da.print_array()
    print("itemAt(5): ", da.itemAt(5))

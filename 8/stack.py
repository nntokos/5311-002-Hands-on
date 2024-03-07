# Hands on 8 - Implement source code for the stack data structure
import random

# For the scope of this hands-on exercise, a fixed size array is only allowed, hence the commands append and pop are not used

class Stack:
    def __init__(self, length):
        self.stack = [None] * length
        self.length = length
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.length - 1

    def push(self, item):
        if self.isFull():
            print("Overflow")
        else:
            self.top += 1
            self.stack[self.top] = item

    def pop(self):
        if self.isEmpty():
            print("Underflow")
        else:
            self.stack[self.top] = None
            self.top -= 1

    def firstElement(self):
        if self.isEmpty():
            print("Underflow")
        else:
            return self.stack[0]

    def lastElement(self):
        if self.isEmpty():
            print("Underflow")
        else:
            return self.stack[self.top]

    def elementAt(self, index):
        if self.isEmpty():
            print("Underflow")
        else:
            return self.stack[index]

    def numberOfElements(self):
        return self.top + 1

    def printDetails(self):
        print("\n====== Stack Details: =======")
        print("Stack: ", self.stack)
        print("Empty: ", self.isEmpty())
        print("Full: ", self.isFull())
        print("Number of items: ", self.numberOfElements())
        print("First item: ", self.firstElement())
        print("Last item: ", self.lastElement())
        print("==============================\n")

if __name__ == '__main__':
    stack = Stack(10)

    stack.printDetails()

    print("Pushing 2 random numbers into the stack")
    stack.push(random.randint(0, 100))
    stack.push(random.randint(0, 100))
    stack.printDetails()

    print("Pushing 8 more random numbers into the stack")
    for i in range(8):
        stack.push(random.randint(0, 100))
    stack.printDetails()
    print("\rItem at index 5: ", stack.elementAt(5), end ='\n\n\n')

    print("Popping 5 items from the stack")
    for i in range(5):
        stack.pop()
    stack.printDetails()
    print("Stack number of items after pop: ", stack.numberOfElements())


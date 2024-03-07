# Hands on 8 - Implement source code for the queue data structure
import random

# For the scope of this hands-on exercise, a fixed size array is only allowed, hence the commands append and pop are not used

class Queue:
    def __init__(self, length):
        self.queue = [None] * length
        self.length = length
        self.head = 0
        self.tail = 0

    def isEmpty(self):
        return self.head == self.tail

    def isFull(self):
        return self.head == self.tail + 1 or (self.head == 0 and self.tail == self.length - 1)

    def enqueue(self, item):
        if self.isFull():
            print("Overflow")
        else:
            self.queue[self.tail] = item
            self.tail = 0 if self.tail == self.length - 1 else self.tail + 1

    def dequeue(self):
        x = self.queue[self.head]
        if self.isEmpty():
            print("Underflow")
        else:
            self.queue[self.head] = None
            self.head = 0 if self.head == self.length - 1 else self.head + 1
        return x

    def headElement(self):
        if self.isEmpty():
            print("Underflow")
        else:
            return self.queue[self.head]

    def tailElement(self):
        if self.isEmpty():
            print("Underflow")
        else:
            return self.queue[self.tail - 1]

    def elementAtIndexBehindHead(self, index):
        if self.isEmpty():
            print("Underflow")
        elif (self.head + index)%self.length > self.tail:
            print("Index out of bounds")
        else:
            return self.queue[(self.head + index)%self.length]

    def numberOfElements(self):
        if self.head <= self.tail:
            return self.tail - self.head
        else:
            return self.length - self.head + self.tail

    def printDetails(self):
        print("\n====== Queue Details: =======")
        print("Queue: ", self.queue)
        print("Empty: ", self.isEmpty())
        print("Full: ", self.isFull())
        print("Number of items: ", self.numberOfElements())
        print(f"Head: {self.head}, Element: ", self.headElement())
        print(f"Tail: {self.tail}, Element: ", self.tailElement())
        print("==============================\n")

if __name__ == '__main__':
    queue = Queue(10)

    queue.printDetails()

    print("Enqueuing 2 random numbers into the queue")
    queue.enqueue(random.randint(0, 100))
    queue.enqueue(random.randint(0, 100))
    queue.printDetails()

    print("Enqueuing 8 more random numbers into the queue")
    for i in range(8):
        queue.enqueue(random.randint(0, 100))
    queue.printDetails()
    print("Item at index 5: ", queue.elementAtIndexBehindHead(5))

    print("Dequeuing 5 items from the queue")
    for i in range(5):
        queue.dequeue()
    queue.printDetails()
    print("Queue number of items after dequeue: ", queue.numberOfElements())


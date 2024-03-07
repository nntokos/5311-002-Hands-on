# Hands on 8 - Implement source code for the singly linked list data structure
import random

# For the scope of this hands-on exercise, a fixed size array is only allowed, hence the commands append and pop are not used


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{id(self)}: [{self.value} | {id(self.next) if self.next is not None else None}]"
class SinglyLinkedList:
    def __init__(self, length):
        self.length = length
        self.head = None

    def isEmpty(self):
        return self.head is None

    def numberOfNodes(self):
        if self.isEmpty():
            return 0
        else:
            count = 1
            node = self.head
            while node.next is not None:
                count += 1
                node = node.next
            return count

    def insert(self, node):
        if self.numberOfNodes() == self.length:
            print("Linked List is full. Length is: ", self.length)
        else:
            if self.isEmpty():
                self.head = node
            else:
                emptyNext = self.head
                while emptyNext.next is not None:
                    emptyNext = emptyNext.next
                emptyNext.next = node

    def delete(self, node):
        if self.isEmpty():
            print("Underflow")
        else:
            if self.head == node:
                self.head = None
            else:
                previousNode = self.head
                while previousNode.next != node:
                    previousNode = previousNode.next
                previousNode.next = node


    def headNode(self):
        if self.isEmpty():
            print("Underflow")
        else:
            return self.head

    def tailNode(self):
        if self.isEmpty():
            print("Underflow")
        else:
            lastNode = self.head
            while lastNode.next is not None:
                lastNode = lastNode.next
            return lastNode

    def nodeAtIndex(self, index):
        if self.isEmpty():
            print("Underflow")
        else:
            node = self.head
            for i in range(index):
                if node.next is not None:
                    node = node.next
                else:
                    print("Index out of bounds")
                    return
            return node

    def printDetails(self):
        print("\n====== Linked List Details: =======")
        if not self.isEmpty():
            node = self.head
            print(f"Nodes:\n{node}", end=" ->\n")
            while node.next is not None:
                node = node.next
                print(node, end=" ->\n")
        print("Empty: ", self.isEmpty())
        print("Number of items: ", self.numberOfNodes())
        print(f"Head Element: ", self.headNode())
        print(f"Tail Element: ", self.tailNode())
        print("==============================\n")

if __name__ == '__main__':
    linkedList = SinglyLinkedList(10)

    linkedList.printDetails()

    print("Pushing 2 random numbers into the list")
    for i in range(2):
        node = Node(random.randint(0, 100))
        linkedList.insert(node)
    linkedList.printDetails()

    print("Pushing 8 more random numbers into the list")
    for i in range(8):
        node = Node(random.randint(0, 100))
        linkedList.insert(node)
    linkedList.printDetails()
    print("Item at index 5: ", linkedList.nodeAtIndex(5))

    print("Remove the tail Element 5 times from the list")
    for i in range(5):
        linkedList.delete(linkedList.tailNode())
    linkedList.printDetails()
    print("Linked List's number of items after pop: ", linkedList.numberOfNodes())


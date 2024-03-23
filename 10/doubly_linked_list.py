# Hands on 10 - Implement source code for the doubly linked list data structure for use in the hash table implementation

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{id(self)}: [{id(self.prev) if self.prev is not None else None} | {self.value} | {id(self.next) if self.next is not None else None}]"
class DoublyLinkedList:
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
                node.prev = emptyNext



    def delete(self, node):
        if self.isEmpty():
            print("Underflow")
        else:
            if self.head == node:
                if self.head.next is not None:
                    self.head.next.prev = None
                self.head = self.head.next
            else:
                previousNode = self.head
                while previousNode.next != node:
                    previousNode = previousNode.next
                if node.next is not None:
                    node.next.prev = previousNode
                previousNode.next = node.next

    def tail(self):
        if self.isEmpty():
            print("Underflow")
        else:
            lastNode = self.head
            while lastNode.next is not None:
                lastNode = lastNode.next
            return lastNode

    def nodeWithKey(self, key):
        if self.isEmpty():
            print("Underflow")
        else:
            node = self.head
            for i in range(self.numberOfNodes()):
                if node.key == key:
                    return node
                node = node.next
            return None

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
        print(f"Tail Element: ", self.tail())
        print("==============================\n")


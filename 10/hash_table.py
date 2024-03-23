import argparse
import math

from doubly_linked_list import DoublyLinkedList, Node


class HashTable:
    def __init__(self, length):
        self.length = length
        self.table = [DoublyLinkedList(10) for _ in range(length)]
        self.count = 0

    def hash(self, key):
        A = (math.sqrt(5) - 1) / 2
        return math.floor(self.length * ((key * A) % 1))

    def resize(self, new_length):
        old = self.table
        self.table = [DoublyLinkedList(10) for _ in range(new_length)]
        self.length = new_length
        self.count = 0
        for i in range(len(old)):
            node = old[i].head
            while node is not None:
                self.insert(node.key, node.value)
                node = node.next

    def insert(self, key, value):
        if self.count == self.length:
            self.resize(self.length * 2)
        index = self.hash(key)
        print("Index: ", index)
        node = self.table[index].nodeWithKey(key)
        if node is not None:
            node.value = value
        else:
            self.table[index].insert(Node(key, value))
            self.count += 1

    def delete(self, key):
        index = self.hash(key)
        node = self.table[index].nodeWithKey(key)
        if node is not None:
            self.table[index].delete(node)
            self.count -= 1
            if self.count <= self.length // 4:
                self.resize(self.length // 2)
        else:
            print("Key not found")
    def search(self, key):
        index = self.hash(key)
        node = self.table[index].nodeWithKey(key)
        if node is not None:
            return node.value
        else:
            return None

    def printDetails(self):
        print("\n====== Hash Table Details: =======")
        print("Table: ", self.table)
        print("Length: ", self.length)
        print("Count: ", self.count)
        print("==================================\n")

    def printTable(self):
        for i in range(self.length):
            print(f"Index {i}: ", end="")
            node = self.table[i].head
            while node is not None:
                print(f"{node.key}: {node.value}", end=" -> ")
                node = node.next
            print("None")

if __name__ == '__main__':
    hash_table = HashTable(6)
    hash_table.printDetails()
    hash_table.printTable()
    hash_table.insert(1, 100)
    hash_table.insert(2, 200)
    hash_table.insert(3, 300)
    hash_table.printDetails()
    hash_table.printTable()
    hash_table.insert(4, 400)
    hash_table.insert(5, 500)
    hash_table.printDetails()
    hash_table.printTable()
    hash_table.insert(16, 1600)
    hash_table.insert(17, 1700)
    hash_table.insert(1372, 137200)
    hash_table.printDetails()
    hash_table.printTable()
    hash_table.delete(16)
    hash_table.delete(17)
    hash_table.delete(1372)
    hash_table.printDetails()
    hash_table.printTable()



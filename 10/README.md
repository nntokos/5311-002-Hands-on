# CSE 5311-002 - Hands On 10

__System Specifications:__
* CPU: Apple M1 Pro 10 cores @ 2.06-3.22 GHz
* RAM: 16 GB LPDDR5
* OS: MacOS Sonoma 14.3.1
* Python version: 3.9.7

### A. Hash table implementation 

1. Implemented the a Hash table using a chaining method to handle collisions.
    <br />Run with following command:
    ```
    python3 hash_table.py
    ```

2. __Functionality__

* The hash table is implemented using a class with the following attributes and functions
    * `table`: A list to store the linked lists.
    * `size`: The size of the hash table.
    * `count`: The number of key-value pairs in the hash table.
      <br />**Functions**
    * `hash`: A function to calculate the hash value of the key. Both multiplication and division methods are implemented at the same time.
    * `resize`: Resizes the hash table to the new size. (Used when the hash table is full to double its size or 1/4 full to halve its size)
    * `insert`: Inserts the key-value pair into the hash table.
    * `delete`: Deletes the key-value pair from the hash table.
    * `search`: Searches for the key in the hash table and returns the value.
    * `printDetails`: Prints the hash table's details at any given time.
    * `printTable`: Prints the hash table's table at any given time.
* A doubly linked list is implemented to handle collisions. The linked list uses `class Node` for the stored nodes and has the following attributes and functions:
    * `head`: The head of the linked list.
    * `length`: The length of the linked list.
      <br />**Functions**
    * `isEmpty`: Checks if the linked list is empty (i.e., head is None).
    * `numberOfNodes`: Returns the number of nodes in the linked list.
    * `insert`: Inserts the key-value pair into the linked list.
    * `delete`: Deletes the key-value pair from the linked list.
    * `nodeWithKey`: Searches for the key in the linked list and returns the value.
    * `tail`: The tail of the linked list.
    * `printDetails`: Prints the linked list's details at any given time.
      <br />**Node**
    * `key`: The key of the node.
    * `value`: The value of the node.
    * `next`: The next node in the linked list.
    * `prev`: The previous node in the linked list.
* The code is generic enough to allow any type of hash function
* In this implementation of the hash table the keys are integers and the values can be any type. However, a simple change of the hash function can allow the keys to be any type.
* The main function demonstrates the functionality of the hash table class by inserting, deleting, and printing the hash table's details. The hash table is initially empty.

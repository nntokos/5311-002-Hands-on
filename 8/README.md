# CSE 5311-002 - Hands On 8

__System Specifications:__
* CPU: Apple M1 Pro 10 cores @ 2.06-3.22 GHz
* RAM: 16 GB LPDDR5
* OS: MacOS Sonoma 14.0
* Python version: 3.9.7

### A. Find i<sup>th</sup> order statistic 

1. Implemented the algorithm in Python.
    <br />Run with following command:
    ```
    python3 ith_order_statistic.py
    ```

2. __Functionality__

* Partitioning the array based on the pivot element as in the quicksort algorithm.
* Recursively calling the find_ith_order_statistic function on the subarray where the ith element falls in.
* Eventually returning the array's ith order statistic which will be the array[pivot].
* For validation, the array is sorted and the ith element is extracted to check if the output is the same.

### B. Implement source code for stack, queue and singly linked list

Implemented the algorithms in Python using a class for each structure.
<br />Run with following commands:
```
python3 stack.py
```
```
python3 queue.py
```
```
python3 singly_linked_list.py
```
1. __Stack__
   1. Attributes:
      * stack: A list to store the elements.
      * length: The length of the stack.
      * top: The index of the top element in the stack.
   2. Methods:
      * isEmpty: Checks if the stack is empty (i.e., top is -1).
      * isFull: Checks if the stack is full (i.e., top is equal to the length of the stack).
      * push: Inserts the element at the top and increments the top index. *(Checks for overflow)*
      * pop: Removes the top element and decrements the top index. *(Checks for underflow)*
      * firstElement: Returns the first element from the stack (i.e., stack[0]). *(Checks for underflow)*
      * lastElement: Returns the last element from the stack (i.e., stack[top]). *(Checks for underflow)*
      * elementAt: Returns the element at the given index. *(Checks for underflow)*
      * numberOfElements: Returns the number of elements in the stack.
      * printDetails: Prints the stack's details at any given time.
   3. Example
      <br />The main function demonstrates the functionality of the stack class by pushing, popping, and printing the stack's details. The stack is initially empty.
      <br />Output:
      ```
      ====== Stack Details: =======
      Stack:  [None, None, None, None, None, None, None, None, None, None]
      Empty:  True
      Full:  False
      Number of items:  0
      Underflow
      First item:  None
      Underflow
      Last item:  None
      ==============================
      
      Pushing 2 random numbers into the stack
      
      ====== Stack Details: =======
      Stack:  [15, 58, None, None, None, None, None, None, None, None]
      Empty:  False
      Full:  False
      Number of items:  2
      First item:  15
      Last item:  58
      ==============================
      
      Pushing 8 more random numbers into the stack
      
      ====== Stack Details: =======
      Stack:  [15, 58, 40, 79, 54, 15, 16, 49, 51, 64]
      Empty:  False
      Full:  True
      Number of items:  10
      First item:  15
      Last item:  64
      ==============================
      
      Item at index 5:  15

      Popping 5 items from the stack
      
      ====== Stack Details: =======
      Stack:  [15, 58, 40, 79, 54, None, None, None, None, None]
      Empty:  False
      Full:  False
      Number of items:  5
      First item:  15
      Last item:  54
      ==============================
      
      Stack number of items after pop:  5
      ```

2. __Queue__
   <br />For the queue, the textbook paradigm was followed, hence a queue is full when head == tail + 1 and the queue is empty when head == tail. This means that the queue has one empty space to differentiate between the empty and full states. 
   1. Attributes:
      * queue: A list to store the elements.
      * length: The length of the queue.
      * head: The index of the head of the queue
      * tail: The index of the tail of the queue.
   2. Methods:
      * isEmpty: Checks if the queue is empty (i.e., head == tail).
      * isFull: Checks if the queue is full (i.e., head == tail + 1).
      * enqueue: Inserts the element at the tail and increments the tail index. *(Checks for overflow)*
      * dequeue: Removes the head element and increments the head index. *(Checks for underflow)*
      * headElement: Returns the head element from the queue (i.e., queue[head]). *(Checks for underflow)*
      * tailElement: Returns the tail element from the queue (i.e., queue[tail]). *(Checks for underflow)*
      * elementAtIndexBehindHead: Returns the element at the given index (i.e., queue[(head + index)%length]). *(Checks for underflow and index out of bounds)*
      * numberOfElements: Returns the number of elements in the queue.
      * printDetails: Prints the queue's details at any given time.
   3. Example
       <br />The main function demonstrates the functionality of the queue class by enqueuing, dequeuing, and printing the queue's details. The queue is initially empty.
       <br />Output:
      ```
      ====== Queue Details: =======
      Queue:  [None, None, None, None, None, None, None, None, None, None]
      Empty:  True
      Full:  False
      Number of items:  0
      Underflow
      Head: 0, Element:  None
      Underflow
      Tail: 0, Element:  None
      ==============================

      Enqueuing 2 random numbers into the queue
      
      ====== Queue Details: =======
      Queue:  [12, 15, None, None, None, None, None, None, None, None]
      Empty:  False
      Full:  False
      Number of items:  2
      Head: 0, Element:  12
      Tail: 2, Element:  15
      ==============================
      
      Enqueuing 8 more random numbers into the queue
      Overflow
      
      ====== Queue Details: =======
      Queue:  [12, 15, 83, 74, 92, 14, 64, 33, 98, None]
      Empty:  False
      Full:  True
      Number of items:  9
      Head: 0, Element:  12
      Tail: 9, Element:  98
      ==============================
      
      Item at index 5:  14
      Dequeuing 5 items from the queue
      
      ====== Queue Details: =======
      Queue:  [None, None, None, None, None, 14, 64, 33, 98, None]
      Empty:  False
      Full:  False
      Number of items:  4
      Head: 5, Element:  14
      Tail: 9, Element:  98
      ==============================
      
      Queue number of items after dequeue:  4
      ```

3. __Singly Linked List__
   <br />For the singly linked list, there two classes, one for the node and one for the list.
   1. Attributes:
      1. Node:
         * data: The data stored in the node.
         * next: The reference to the next node.
      2. SinglyLinkedList:
         * length: The length of the linked list.
         * head: The head of the linked list. 
   2. Methods:
      1. Node:
         * __init__: Initializes the node with the given data and next node.
         * __str__: Returns the string representation of the node (i.e., "<id>: [<value> | <nextNodeId>]").
      2. SinglyLinkedList:
         * isEmpty: Checks if the linked list is empty (i.e., head is None).
         * numberOfNodes: Returns the number of nodes in the linked list.
         * insert: Inserts the node at the end of the linked list.
         * delete: Finds and deletes the node from the linked list.
         * headNode: Returns the head node from the linked list.
         * tailNode: Returns the tail node from the linked list.
         * nodeAtIndex: Returns the node at the given index counted from the head.
         * printDetails: Prints the linked list's details at any given time.
   3. Example
         <br />The main function demonstrates the functionality of the singly linked list class by inserting, deleting, and printing the linked list's details. The linked list is initially empty.
         <br />Output:
         ```
         ====== Linked List Details: =======
         Empty:  True
         Number of items:  0
         Underflow
         Head Element:  None
         Underflow
         Tail Element:  None
         ==============================
         
         Pushing 2 random numbers into the list
         
         ====== Linked List Details: =======
         Nodes:
         4889148816: [50 | 4889148672] ->
         4889148672: [65 | None] ->
         Empty:  False
         Number of items:  2
         Head Element:  4889148816: [50 | 4889148672]
         Tail Element:  4889148672: [65 | None]
         ==============================
         
         Pushing 8 more random numbers into the list
         
         ====== Linked List Details: =======
         Nodes:
         4889148816: [50 | 4889148672] ->
         4889148672: [65 | 4889148768] ->
         4889148768: [42 | 4889148480] ->
         4889148480: [34 | 4889148384] ->
         4889148384: [79 | 4889148288] ->
         4889148288: [2 | 4889148192] ->
         4889148192: [91 | 4889148096] ->
         4889148096: [51 | 4889148000] ->
         4889148000: [86 | 4889147904] ->
         4889147904: [77 | None] ->
         Empty:  False
         Number of items:  10
         Head Element:  4889148816: [50 | 4889148672]
         Tail Element:  4889147904: [77 | None]
         ==============================
         
         Item at index 5:  4889148288: [2 | 4889148192]
         Remove the tail Element 5 times from the list
         
         ====== Linked List Details: =======
         Nodes:
         4889148816: [50 | 4889148672] ->
         4889148672: [65 | 4889148768] ->
         4889148768: [42 | 4889148480] ->
         4889148480: [34 | 4889148384] ->
         4889148384: [79 | 4889148288] ->
         4889148288: [2 | 4889148192] ->
         4889148192: [91 | 4889148096] ->
         4889148096: [51 | 4889148000] ->
         4889148000: [86 | 4889147904] ->
         4889147904: [77 | None] ->
         Empty:  False
         Number of items:  10
         Head Element:  4889148816: [50 | 4889148672]
         Tail Element:  4889147904: [77 | None]
         ==============================
         
         Linked List's number of items after pop:  10
         ```

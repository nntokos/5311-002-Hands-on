# CSE 5311-002 - Hands On 12

### __System Specifications__
* CPU: Apple M1 Pro 10 cores @ 2.06-3.22 GHz
* RAM: 16 GB LPDDR5
* OS: MacOS Sonoma 14.3.1
* Python version: 3.9.7

### A. Dynamic Array implementation 

1. __Command to run the code__
    ```
    python3 dynamic_array.py
    ```

2. __Functionality__

    The dynamic array is implemented using a `class DynamicArray` with the following attributes and functions:
    <br /><u>**Dynamic Array**</u>
    * ***Attributes***
      * `count`: The number of elements in the dynamic array.
      * `capacity`: The total capacity of the dynamic array.
      * `array`: The array that stores the elements.
    * ***Functions***
      * `increase_capacity`: Increases the capacity of the dynamic array by 2 times.
      * `insert`: Inserts the element at the given index or at the end (by default, is index is not given) in the dynamic array.
      * `delete`: Deletes the element at the given index in the dynamic array.
      * `itemAt`: Returns the value at the given index in the dynamic array.
      * `printArray`: Prints the dynamic array at any given time.
3. __Output__
   <br />With a simple test case I get the following results:
    ```
    Inserting 10, 20, 30, 40, 50 at the end
   Array: [10 20 30 40 50]
   Capacity:  5
   
   Inserting 60, 70, 80, 90, 100 at index 3
   Array: [10 20 30 100 90 80 70 60 40 50]
   Capacity:  10
   
   itemAt(5):  80
   Deleting item at index 5
   Array: [10 20 30 100 90 70 60 40 50]
   Capacity:  10
   
   itemAt(5):  70
    ```


### B. Red Black Tree implementation

1. __Command to run the code__
    ```
    python3 red_black_tree.py
    ```
   
2. __Functionality__
    
    The red-black tree is implemented using a `class Node` and a `class RedBlackTree` with the following attributes and functions:
    <br /><u>**Node**</u>
    * ***Attributes***
        * `key`: The key of the node.
        * `value`: The value of the node.
        * `left`: The left child of the node.
        * `right`: The right child of the node.
        * `color`: The color of the node (red or black).
    
    <br /><u>**Red Black Tree**</u>
    * ***Attributes***
        * `root`: The root of the red-black tree.
    * ***Functions***
        > All the functions are implemented in a recursive manner. Since the recursions start from the root node, the functions are called with the root node as the starting point. However, a function cannot take self.root as an argument, therefore a helper (public) function is used to call the main (private) function with the root node (e.g. add(key, value) calls _add(node, key, value).
        * `isEmpty`: Checks if the red-black tree is empty (i.e., root is None).
        * `add`: Inserts the node into the red-black tree.
        * `delete`: Deletes the node from the red-black tree.
        * `balance`: Balances the red-black tree after addition and deletion.
        * `query`: Searches for the node with a given key in the red-black tree.
        * `min`: Finds the minimum value in the red-black tree.
        * `max`: Finds the maximum value in the red-black tree.
        * `printDetails`: Prints the red-black tree's details at any given time.
3. __Output__
    ```
    ======== {RBT} ==========
    Key: 10, Color: black, [Left: None | Right: 20]
    Key: 20, Color: red, [Left: None | Right: 30]
    Key: 30, Color: red, [Left: None | Right: 40]
    Key: 40, Color: red, [Left: None | Right: None]
    =========================
    {Root}:  Key: 10, Color: black, [Left: None | Right: 20]
    {Root Left}:  None
    {Root Right}:  Key: 20, Color: red, [Left: None | Right: 30]
    Deleting 20 and 30...
    {Root Left}:  None
    {Root Right}:  Key: 40, Color: red, [Left: None | Right: None]
    {Query 10}:  Key: 10, Color: black, [Left: None | Right: 40]
    {Query 40}:  Key: 40, Color: red, [Left: None | Right: None]
    {Query 30}:  None
    ======== {RBT} ==========
    Key: 10, Color: black, [Left: None | Right: 40]
    Key: 40, Color: red, [Left: None | Right: None]
    =========================
    ```

### C. AVL Tree implementation

1. __Command to run the code__
    ```
    python3 avl_tree.py
    ```
   
2. __Functionality__
        
    The AVL tree is implemented using a `class Node` and a `class AVLTree` with the following attributes and functions:
    <br /><u>**Node**</u>
    * ***Attributes***
        * `key`: The key of the node.
        * `value`: The value of the node.
        * `left`: The left child of the node.
        * `right`: The right child of the node.
        * `height`: The height of the node.
    
    <br /><u>**AVL Tree**</u>
    * ***Attributes***
        * `root`: The root of the AVL tree.
    * ***Functions***
        > All the functions are implemented in a recursive manner. Since the recursions start from the root node, the functions are called with the root node as the starting point. However, a function cannot take self.root as an argument, therefore a helper (public) function is used to call the main (private) function with the root node (e.g. add(key, value) calls _add(node, key, value).
        * `isEmpty`: Checks if the AVL tree is empty (i.e., root is None).
        * `add`: Inserts the node into the AVL tree.
        * `delete`: Deletes the node from the AVL tree.
        * `balance`: Balances the AVL tree after addition and deletion.
        * `leftRotate`: Rotates the AVL tree to the left. Called when the tree is unbalanced. Essentially, the right child of the node becomes the new root, and the node becomes the left child of the new root.
        * `rightRotate`: Rotates the AVL tree to the right. Called when the tree is unbalanced. Same functionality as leftRotate but in the opposite direction.
        * `query`: Searches for the node with a given key in the AVL tree.
        * `min`: Finds the minimum value in the AVL tree.
        * `max`: Finds the maximum value in the AVL tree.
         * `inOrder`: Traverses the AVL tree in an in-order manner.
        * `print`: Prints the AVL tree's details at any given time.
3. __Output__
    ```
    ========== {AVL} ==========
   Key: 10, Height: 2, [Left: None | Right: 15]
   Key: 15, Height: 1, [Left: None | Right: None]
   Key: 20, Height: 3, [Left: 10 | Right: 30]
   Key: 25, Height: 1, [Left: None | Right: None]
   Key: 30, Height: 2, [Left: 25 | Right: None]
   =========================
   Delete 20
   
   ========== {AVL} ==========
   Key: 10, Height: 2, [Left: None | Right: 15]
   Key: 15, Height: 1, [Left: None | Right: None]
   Key: 25, Height: 3, [Left: 10 | Right: 30]
   Key: 30, Height: 1, [Left: None | Right: None]
   =========================
   Query 10 Key: 10, Height: 2, [Left: None | Right: 15]
   In Order: 
   Key: 10, Height: 2, [Left: None | Right: 15]
   Key: 15, Height: 1, [Left: None | Right: None]
   Key: 25, Height: 3, [Left: 10 | Right: 30]
   Key: 30, Height: 1, [Left: None | Right: None]
   None
    ```

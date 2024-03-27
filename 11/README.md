# CSE 5311-002 - Hands On 11

### __System Specifications__
* CPU: Apple M1 Pro 10 cores @ 2.06-3.22 GHz
* RAM: 16 GB LPDDR5
* OS: MacOS Sonoma 14.3.1
* Python version: 3.9.7

### A. Binary Search Tree implementation 

1. __Command to run the code__
    ```
    python3 binary_search_tree.py
    ```

2. __Functionality__

    The binary search tree is implemented using a `class Node` and a `class BinarySearchTree` with the following attributes and functions:
  <br /><u>**Node**</u>
   * ***Attributes***
        * `key`: The key of the node.
        * `value`: The value of the node.
        * `left`: The left child of the node.
        * `right`: The right child of the node.

    <br /><u>**Binary Search Tree**</u>
    * ***Attributes***
        * `root`: The root of the binary search tree.
    * ***Functions***
        > All the functions are implemented in a recursive manner. Since the recursions start from the root node, the functions are called with the root node as the starting point.
      However, a function cannot take self.root as an argument, therefore a helper (public) function is used to call the main (private) function with the root node (e.g. `add(key, value)` calls `_add(node, key, value`).
        * `isEmpty`: Checks if the binary search tree is empty (i.e., root is None).
        * `add`: Inserts the key into the binary search tree.
        * `delete`: Deletes the key from the binary search tree.
        * `query`: Searches for the key in the binary search tree.
        * `predecessor`: Finds the predecessor of the key in the binary search tree.
        * `successor`: Finds the successor of the key in the binary search tree.
        * `min`: Finds the minimum value in the binary search tree.
        * `max`: Finds the maximum value in the binary search tree.
        * `printDetails`: Prints the binary search tree's details at any given time.
3. __Output__
    ```
    {isEmpty}  True
    BST =  2 3 4 5 6 8 8 
    {Query(5)}  5: [Left: 3 | Right: 6]
    {Query(3)}  3: [Left: 2 | Right: 4]
    {Query(4)}  4: [Left: None | Right: None]
    {Delete(8)} 
    BST =  2 3 4 5 6 8 
    {isEmpty}  False
    {Query(8)}  8: [Left: None | Right: None]
    {Query(9)}  None
    {Predecessor(5)}  4: [Left: None | Right: None]
    {Successor(5)}  6: [Left: None | Right: 8]
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
        > All the functions are implemented in a recursive manner just like the binary search tree. The logic is similar to the binary search tree with additional functions to balance the tree after addition and deletion.
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
        > All the functions are implemented in a recursive manner just like the binary search tree. The logic is similar to the binary search tree with additional functions to balance the tree after addition and deletion.
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

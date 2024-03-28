# Hands on 11 - Implement source code for the "The basic" Binary Search Tree; this is the one that can be unbalanced


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.key}: [Left: {self.left.key if self.left is not None else None} | Right: {self.right.key if self.right is not None else None}]"

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def add(self, node):
        y= None
        x = self.root
        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            elif node.key > x.key:
                x = x.right
            else:
                x.value = node.value
                return
        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node


    def transplant(self, u, v):
        if u is None:
            return
        if u == self.root:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent


    def delete(self, node):
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            y = self.min(node.right)
            if y.parent != node:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y

    def query(self, key):
        return self._query(self.root, key)

    def _query(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._query(node.left, key)
        else:
            return self._query(node.right, key)


    def predecessor(self, node):
        if node is None:
            return None
        if node.left is not None:
            return self.max(node.left)
        y = node.parent
        x = node.key
        while y is not None and x == y.left.key:
            x = y.key
            y = x.parent
        return y

    def successor(self, node):
        if node is None:
            return None
        if node.right is not None:
            return self.min(node.right)
        y = node.parent
        x = node.key
        while y is not None and x == y.right.key:
            x = y.key
            y = x.parent
        return y

    def max(self, node):
        while node.right is not None:
            node = node.right
        return node

    def min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def __str__(self):
        return self._print(self.root)

    def _print(self, node):
        if node is None:
            return ""
        return self._print(node.left) + f"{node.key} " + self._print(node.right)


if __name__ == "__main__":
    bst = BinarySearchTree()
    print("{isEmpty} ", bst.isEmpty())
    bst.add(Node(5, "Five"))
    bst.add(Node(3, "Three"))
    bst.add(Node(7, "Seven"))
    bst.add(Node(4, "Four"))
    bst.add(Node(6, "Six"))
    bst.add(Node(9, "Nine"))
    bst.add(Node(8, "Eight"))
    print("BST = ", bst)
    print("{Query(5)} ", bst.query(5))
    print("{Query(3)} ", bst.query(3))
    print("{Query(4)} ", bst.query(4))
    print("{Delete(8)} ")
    bst.delete(bst.query(8))
    print("BST = ", bst)
    print("{isEmpty} ", bst.isEmpty())
    print("{Query(8)} ", bst.query(8))
    print("{Query(9)} ", bst.query(9))
    print("{Predecessor(5)} ", bst.predecessor(bst.query(5)))
    print("{Successor(5)} ", bst.successor(bst.query(5)))



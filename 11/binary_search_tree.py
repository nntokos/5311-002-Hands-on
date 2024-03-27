# Hands on 11 - Implement source code for the "The basic" Binary Search Tree; this is the one that can be unbalanced


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.key}: [Left: {self.left.key if self.left is not None else None} | Right: {self.right.key if self.right is not None else None}]"

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def add(self, key, value):
        if self.isEmpty():
            self.root = Node(key, value)
        else:
            self._add(self.root, key, value)

    def _add(self, node, key, value):
        if key <= node.key:
            if node.left is None:
                node.left = Node(key, value)
            else:
                self._add(node.left, key, value)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, value)
            else:
                self._add(node.right, key, value)
        else:
            node.value = value


    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.key = self._min(node.right).key
                node.value = self._min(node.right).value
                node.right = self._delete(node.right, node.key)
        return node

    def query(self, key):
        return self._query(self.root, key)

    def _query(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._query(node.left, key)
        else:
            return self._query(node.right, key)


    def predecessor(self, key):
        return self._predecessor(self.root, key)

    def _predecessor(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return self._max(node.left)
        if key < node.key:
            return self._predecessor(node.left, key)
        else:
            return self._predecessor(node.right, key)

    def successor(self, key):
        return self._successor(self.root, key)

    def _successor(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return self._min(node.right)
        if key < node.key:
            return self._successor(node.left, key)
        else:
            return self._successor(node.right, key)

    def _max(self, node):
        while node.right is not None:
            node = node.right
        return node

    def _min(self, node):
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
    bst.add(5, "Five")
    bst.add(3, "Three")
    bst.add(2, "Two")
    bst.add(4, "Four")
    bst.add(6, "Six")
    bst.add(8, "Eight")
    bst.add(8, "Eight(2)")
    print("BST = ", bst)
    print("{Query(5)} ", bst.query(5))
    print("{Query(3)} ", bst.query(3))
    print("{Query(4)} ", bst.query(4))
    print("{Delete(8)} ")
    bst.delete(8)
    print("BST = ", bst)
    print("{isEmpty} ", bst.isEmpty())
    print("{Query(8)} ", bst.query(8))
    print("{Query(9)} ", bst.query(9))
    print("{Predecessor(5)} ", bst.predecessor(5))
    print("{Successor(5)} ", bst.successor(5))



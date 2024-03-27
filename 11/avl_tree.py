# Hands on 11 - Implement source code for the AVL tree data structure


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return f"Key: {self.key}, Height: {self.height}, [Left: {self.left.key if self.left is not None else None} | Right: {self.right.key if self.right is not None else None}]"

class AVLTree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def getHeight(self, node):
        if node is None:
            return 0
        return node.height

    def getBalance(self, node):
        if node is None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def add(self, key, value):
        if self.isEmpty():
            self.root = Node(key, value)
        else:
            self.root = self._add(self.root, key, value)

    def _add(self, node, key, value):
        if node is None:
            return Node(key, value)
        if key < node.key:
            node.left = self._add(node.left, key, value)
        elif key > node.key:
            node.right = self._add(node.right, key, value)
        else:
            node.value = value
        return self.balance(node)



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
                temp = self._min(node.right)
                node.key = temp.key
                node.value = temp.value
                node.right = self._delete(node.right, node.key)
        return self.balance(node)

    def balance(self, node):
        if node is None:
            return None
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        balance = self.getBalance(node)
        if balance > 1:
            if self.getBalance(node.left) < 0:
                node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        if balance < -1:
            if self.getBalance(node.right) > 0:
                node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        return node

    def leftRotate(self, node):
        temp = node.right
        node.right = temp.left
        temp.left = node
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        temp.height = 1 + max(self.getHeight(temp.left), self.getHeight(temp.right))
        return temp

    def rightRotate(self, node):
        temp = node.left
        node.left = temp.right
        temp.right = node
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        temp.height = 1 + max(self.getHeight(temp.left), self.getHeight(temp.right))
        return temp

    def query(self, key):
        return self._query(self.root, key)

    def _query(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._query(node.left, key)
        else:
            return self._query(node.right, key)

    def _min(self, node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node

    def _max(self, node):
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node

    def inOrder(self):
        self._inOrder(self.root)

    def _inOrder(self, node):
        if node is not None:
            self._inOrder(node.left)
            print(node)
            self._inOrder(node.right)

    def __str__(self):
        return "\n========== {AVL} ==========\n" + self._print(self.root) + "========================="

    def _print(self, node):
        if node is None:
            return ""
        return self._print(node.left) + str(node) + "\n" + self._print(node.right)

if __name__ == "__main__":
    AVL = AVLTree()
    # Test with 3 additions, 1 deletion, 1 query, 1 predecessor, 1 successor. Also test the leftRotate and rightRotate methods
    AVL.add(10, "Ten")
    AVL.add(20, "Twenty")
    AVL.add(30, "Thirty")
    AVL.add(15, "Fifteen")
    AVL.add(25, "Twenty Five")
    print(AVL)
    print("Delete 20")
    AVL.delete(20)
    print(AVL)
    print("Query 10", AVL.query(10))
    print("In Order: ")
    print(AVL.inOrder())






from bst_node import BSTNode
from krone import Krone


class BST:
    _count = 0
    _head = None

    def __init__(self, value=None):
        if value:
            self._count += 1
            self._head = BSTNode(data=value)

    def preorder_traversal(self, root):
        pass

    def postorder_traversal(self, root):
        pass

    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.data.get_value())
            res = res + self.inorder_traversal(root.right)
        return res

    def breadth_first_traversal(self, root):
        pass

    def search(self):
        pass

    def insert(self, krone: Krone):
        if not self._head:
            self._head = BSTNode(data=krone)
            return
        node = self._head
        search = True
        while search:
            if node.data.get_value() > krone.get_value():
                if node.left:
                    node = node.left
                else:
                    node.left = BSTNode(data=krone)
                    search = False
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = BSTNode(data=krone)
                    search = False

    def delete(self, value):
        pass

    def print(self):
        pass

    def count(self):
        pass

    def is_empty(self):
        pass

    def get_head(self):
        return self._head
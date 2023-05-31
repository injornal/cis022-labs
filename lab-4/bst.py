from bst_node import BSTNode


class BST:
    _count = 0

    def __init__(self, data=None):
        if data:
            self._count += 1
            self._root = BSTNode(data)
        else:
            self._root = None

    def preorder_traversal(self):
        pass

    def postorder_traversal(self):
        pass

    def inorder_traversal(self):
        pass

    def breadth_first_traversal(self):
        pass

    def search(self, value):
        pass

    def insert(self, value):
        if self._root is None:
            self._root = BSTNode(value)
        else:
            cur = self._root
            while True:
                if value.get_value() < cur.get_data.get_value():
                    if cur.left is None:
                        cur.left = BSTNode(value)
                        break
                    else:
                        cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = BSTNode(value)
                        break
                    else:
                        cur = cur.right

    def delete(self, value):
        pass

    def print(self):
        if self._root is None:
            return

    def count(self):
        pass

    def is_empty(self):
        return not bool(self._count)

    def empty(self):
        pass

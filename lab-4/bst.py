from bst_node import BSTNode


class BST:
    _count = 0

    def __init__(self, data=None):
        if data:
            self._count += 1
        self.head = BSTNode(data=data)

    def preorder_traversal(self):
        pass

    def postorder_traversal(self):
        pass

    def inorder_traversal(self):
        pass

    def level_order_traversal(self):
        # I'm not sure that this is the right fourth traversal algorithm
        pass

    def search(self):
        pass

    def insert(self, value):
        pass

    def delete(self, value):
        pass

    def print(self):
        pass

    def count(self):
        pass

    def is_empty(self):
        pass

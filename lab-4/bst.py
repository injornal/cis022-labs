from bst_node import BSTNode
from krone import Krone
from queue import Queue


class BST:
    _count = 0

    def __init__(self, value=None):
        if value:
            self._count += 1
            self._head = BSTNode(value)
        else:
            self._head = None

    def preorder_traversal(self, root):
        """Returns the list in which preordered nodes exist

        pre: root - a root node
        post:
        return: a list in which preordered nodes exist
        """
        res = []
        if root:
            res.append(root.get_data().get_value())
            res = res + self.preorder_traversal(root.left)
            res = res + self.preorder_traversal(root.right)
        return res

    def postorder_traversal(self, root):
        """Returns the list in which postordered nodes exist

        pre: root - a root node
        post:
        return: a list in which postordered nodes exist
        """
        res = []
        if root:
            res = self.postorder_traversal(root.left)
            res = res + self.postorder_traversal(root.right)
            res.append(root.get_data().get_value())
        return res

    def inorder_traversal(self, root):
        """Returns the list in which inordered nodes exist

        pre: root - a root node
        post:
        return: a list in which inordered nodes exist
        """
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.get_data().get_value())
            res = res + self.inorder_traversal(root.right)
        return res

    def breadth_first_traversal(self, root):
        """Returns the list in breadth first sequence

        pre: root - a root node
        post:
        return: a list in breadth first sequence
        """
        visited = set()
        queue = Queue()
        res = []
        queue.enqueue(root)

        while not queue.is_list_empty():
            node = queue.dequeue()
            if node not in visited:
                visited.add(node)
                res.append(node.get_data().get_value())
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)
        return res

    def search(self, value):
        """Returns the node by its value

        pre: value - floating point object
        post:
        return: BSTNode object
        """
        node = self._head
        while node:
            if node.data.get_value() == value:
                return node
            if node.data.get_value() > value:
                node = node.left
            else:
                node = node.right
        raise Exception("Element not found.")

    def insert(self, krone: Krone):
        """Inserts BSTNode with Krone object in BST

        pre: krone - Krone object
        post:
        return:
        """
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
        """Removes a node from the tree by its value

        pre: value - floating point object
        post:
        return:
        """
        par = None
        cur = self._head
        while cur:
            if cur.data.get_value() == value:
                if not cur.left and not cur.right:
                    if not par:
                        self.empty()
                    elif par.left == cur:
                        par.left = None
                    else:
                        par.right = None
                elif not cur.right:
                    if not par:
                        self._head = cur.left
                    elif par.left == cur:
                        par.left = cur.left
                    else:
                        par.right = cur.left
                elif not cur.left:
                    if not par:
                        self._head = cur.right
                    elif par.left == cur:
                        par.left = cur.right
                    else:
                        par.right = cur.right
                else:
                    suc = cur.right
                    while suc.left:
                        suc = suc.left
                    suc_data = suc.data
                    self.delete(suc_data.get_value())
                    cur.set_data(suc_data)
                return
            elif cur.data.get_value() < value:
                par = cur
                cur = cur.right
            else:
                par = cur
                cur = cur.left
        return

    def print(self, root):
        """Prints the BST

        pre: root - a root node
        post: object's value and name
        return:
        """
        if root is None:
            return
        root.get_data().print()
        self.print(root.left)
        self.print(root.right)

    def count(self):
        return self._count

    def is_empty(self):
        """Checks if BST is empty

        pre:
        post:
        return: boolean
        """
        return not bool(self._count)

    def empty(self):
        self._head = None

    def get_head(self):
        """Returns the root node

        pre:
        post:
        return: a root node
        """
        return self._head

"""
LAB 4
Kostiantyn Babich, Hyunjong Shin
This assignment is to make a binary search tree and operate traversal methods and other operations
"""

class BSTNode:
    def __init__(self, data):
        self.data = data    # data will be Krone object
        self.left = None
        self.right = None

    def get_data(self):
        """Returns the data of BSTNode

        pre:
        post:
        return: data of BSTNode
        """
        return self.data
    
    def get_left(self):
        """Returns the left node of BSTNode

        pre:
        post:
        return: left node of BSTNode
        """
        return self.left

    def get_right(self):
        """Returns the right node of BSTNode

        pre:
        post:
        return: right node of BSTNode
        """
        return self.right
    
    def set_data(self, data):
        """Sets the data of BSTNode

        pre: data - Krone object
        post:
        return:
        """
        self.data = data

    def set_left(self, bst_node):
        """Sets the left node of BSTNode

        pre: bst_node - a node to be the left node
        post:
        return:
        """
        self.left = bst_node

    def set_right(self, bst_node):
        """Sets the right node of BSTNode

        pre: bst_node - a node to be the right node
        post:
        return:
        """
        self.right = bst_node

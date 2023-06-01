"""
LAB 4
Kostiantyn Babich, Hyunjong Shin
This assignment is to make a binary search tree and operate traversal methods and other operations
"""

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

        Algorithm preorder_traversal ( root )
            result = blank list
            if root is not None
                append root->data->value to result
                recursion on root's left node
                recursion on root's right node
            end if
            return result
        end preorder_traversal
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

        Algorithm postorder_traversal ( root )
            result = blank list
            if root is not None
                recursion on root's left node
                recursion on root's right node
                append root->data->value to result
            end if
            return result
        end postorder_traversal
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
        
        Algorithm inorder_traversal ( root )
            result = blank list
            if root is not None
                recursion on root's left node
                append root->data->value to result
                recursion on root's right node
            end if
            return result
        end inorder_traversal
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

        Algorithm breadth_first_traversal ( root )
            visited = blank set
            queue = Queue
            result = blank list
            enqueue root

            while queue is not empty
                node = dequeue
                if node is not in visited
                    add node to visited
                    append node->data->value to result
                end if
                if node->left is not None
                    enqueue node->left
                end if
                if node->right is not None
                    enqueue node->right
                end if
            end while
            return result
        end breadth_first_traversal
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
        """Returns the node that has value same as the given value

        pre: value - floating point object
        post:
        return: a node that has given value as value

        Algorithm search ( value )
            node = root node
            while node is not None
                if node->data->value is value
                    return node
                end if
                if node->data->value is larger than value
                    node = node->left
                end if
                if node->data->value is smaller than value
                    node = node->right
                end if
            end while
            throw exception "Element not found"
        end search
        """
        node = self._head
        while node:
            if node.get_data().get_value() == value:
                return node
            if node.get_data().get_value() > value:
                node = node.left
            else:
                node = node.right
        raise Exception("Element not found.")

    def insert(self, krone: Krone):
        """Inserts BSTNode with Krone object in BST

        pre: krone - Krone object
        post:
        return:

        Algorithm insert ( krone )
            increment _count
            if BST is empty
                root node = BSTNode(krone)
                return
            end if
            node = root node
            search = True
            while search is True
                if krone->value is smaller than node->data->value
                    if node->left exists
                        node = node->left
                    end if
                    else
                        node->left = BSTNode(krone)
                        search = False
                    end else
                else
                    if node->right exists
                        node = node->right
                    end if
                    else
                        node->right = BSTNode(krone)
                        search = False
                    end else
                end else
            end while
        end insert
        """
        self._count += 1
        if not self._head:
            self._head = BSTNode(data=krone)
            return
        node = self._head
        search = True
        while search:
            if node.get_data().get_value() > krone.get_value():
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

        Algorithm delete ( value )
            set parent to None
            current = root node
            while current is not None
                if current->data->value is value
                    if current has no child
                        if parent is None
                            empty BST
                        end if
                        elif parent->left is current
                            set parent->left to None
                        end elif
                        else
                            set parent->right to None
                        end else
                    end if
                    elif current->right is None
                        if parent is None
                            set root node to current->left
                        end if
                        elif parent->left is current
                            parent->left = current->left
                        end elif
                        else
                            parent->right = current->left
                        end else
                    end elif
                    elif current->left is None
                        if parent is None
                            set root node to current->right
                        end if
                        elif parent->left is current
                            parent->left = current->right
                        end elif
                        else
                            parent->right = current->right
                        end else
                    end elif
                    else
                        succesor = current->right
                        while succesor->left exist
                            succesor = succesor->left
                        end while
                        succesor_data = succesor->data
                        delete(succesor_data->value)
                        set current->data to succesor_data
                    end else
                    return
                elif current->data->value is smaller than value
                    parent = current
                    current = current->right
                end elif
                else
                    parent = current
                    current = current->left
                end else
            return
        end delete
        """
        par = None
        cur = self._head
        while cur:
            if cur.get_data().get_value() == value:
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
                    suc_data = suc.get_data()
                    self.delete(suc_data.get_value())
                    cur.set_data(suc_data)
                return
            elif cur.get_data().get_value() < value:
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

        Algorithm print ( root )
            if BST is empty
                return
            end if
            print root->data
            recursion on root's left node
            recursion on root's right node
        end print
        """
        if root is None:
            return
        root.get_data().print()
        self.print(root.left)
        self.print(root.right)

    def count(self):
        """Returns the number of nodes in BST

        pre:
        post:
        return: number of nodes in BST

        Algorithm count (  )
            return count
        end count
        """
        return self._count

    def is_empty(self):
        """Checks if BST is empty

        pre:
        post:
        return: boolean

        Algorithm is_empty (  )
            if BST is empty
                return True
            end if 
            return False
        end is_empty
        """
        return not bool(self._count)

    def empty(self):
        """Empty the BST

        pre:
        post:
        return:

        Algorithm empty (  )
            set root node to None
        end empty
        """
        self._head = None

    def get_head(self):
        """Returns the root node

        pre:
        post:
        return: a root node

        Algorithm get_head (  )
            return root node
        end get_head
        """
        return self._head

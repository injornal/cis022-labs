"""
LAB 3
Kostiantyn Babich, Hyunjong Shin
This assignment is to make singly linked list to make stack and queue.
"""

from link_node import LinkNode
from currency import Currency
from krone import Krone


class SinglyLinkedList:

    def __init__(self):
        self._count = 0
        self._start = None  # _start is pointing the first node in liked list
        self._end = None  # _end is pointing the last node in linked list
    
    def add_currency(self, currency: Currency, index):
        """The method inserts a currency in a given position
        pre: currency - Currency, the inserting object
            index - integer, the index of the position of the insertion
        post: 
        return:
        """
        new_node = LinkNode(currency)

        if index < 0:
            raise Exception("Invalid index")
        
        if index == 0:
            new_node.next = self._start
            self._start = new_node
            if self._end is None:
                self._end = new_node
        else:
            cur = self.get_node(index - 1)
            new_node.next = cur.next
            cur.next = new_node
            if index == self._count:
                self._end = new_node
        
        self._count += 1

    def remove_currency(self, element):
        """The method removes the node by its value or index
        pre: index - integer/Currency, the index/value of the element to be deleted
        post: 
        return:
        """
        if type(element) == Krone:
            index = self.find_currency(element)
        elif type(element) == int:
            index = element
        else:
            raise Exception("Invalid input type: Input type should be either Currency or integer")

        if index < 0 or self._start is None:
            raise Exception("Invalid index")
        
        if index == 0:
            if self._start == self._end:
                self._start = None
                self._end = None
            else:
                self._start = self._start.next
        else:
            pre = self.get_node(index - 1)
            pre.next = pre.next.next
            if pre.next is None:
                self._end = pre
        self._count -= 1

    def find_node(self, currency: Currency):
        """The method finds a node by its value
        pre: currency - Currency, the value of the searched node
        post:
        return: LinkNode
        """
        if self._start.data == currency:
            return self._start
        cur = self._start
        while cur.next:
            cur = cur.next
            if cur.data == currency:
                return cur
        raise Exception("Element is not in the list")
    
    def find_currency(self, currency: Currency):
        """The method finds an index of the node with given value 
        pre: currency - Currency, the value of the searched element
        post:
        return: Currency
        """
        cur = self._start
        index = 0
        if cur.data.get_value() == currency.get_value():
            return index
        while cur.next:
            cur = cur.next
            index += 1
            if cur.data.get_value() == currency.get_value():
                return index
        raise Exception("Element is not on the list")
    
    def get_node(self, index):
        """The method returns the node with given index
        pre: index - integer, the index of the searched element
        post:
        return: LinkNode
        """
        if index >= self._count:
            raise Exception("Element out of bound")
        cur = self._start
        for i in range(index):
            cur = cur.next
        return cur
    
    def get_currency(self, index):
        """The method returns the value of the node with given index
        pre: index - integer, the index of the searched element
        post: 
        return: Currency
        """
        return self.get_node(index).data
    
    def print_list(self):
        """The method prints the list
        pre: 
        post: list 
        return:
        """
        cur = self._start
        cur.data.print()
        print("\t", end="")

        while cur.next:
            cur = cur.next
            cur.data.print()
            print("\t", end="")

    def is_list_empty(self):
        """The method returns whether the list is epty
        pre:
        post:
        return: boolean
        """
        return not bool(self._count)
    
    def count_currency(self):
        """The method returns the amount of elements in the list
        pre:
        post:
        return: integer
        """
        return self._count

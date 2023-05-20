"""
LAB 3
Kostiantyn Babich, Hyunjong Shin
This assignment is to make singly linked list to make stack and queue.
"""

from singly_linked_list import SinglyLinkedList
from link_node import LinkNode
from currency import Currency
from krone import Krone


# Do not use linked list functions in this class
class Stack(SinglyLinkedList):
    
    def __init__(self) -> None:
        super().__init__()

    def push(self, currency: Currency):
        new_node = LinkNode(currency)
        if self.is_list_empty():
            self._start = new_node
            self._end = new_node
        else:
            new_node.next = self._start
            self._start = new_node
        self._count += 1

    def pop(self):
        if self.is_list_empty():
            raise Exception("Stack is empty")
        else:
            removed_item = self._start.data
            self._start = self._start.next
            if self._start is None:
                self._end = None
            return removed_item

    def peek(self):
        return Krone(self._start.data.get_value())  # copy of a Krone object

    def printStack(self):
        cur = self._start
        cur.data.print()
        print("\t", end="")

        while cur.next:
            cur = cur.next
            cur.data.print()
            print("\t", end="")

    def add_currency(self, currency: Currency, index):
        raise NameError("method is not accessible")

    def remove_currency(self, element):
        raise NameError("method is not accessible")

    def find_node(self, currency: Currency):
        raise NameError("method is not accessible")

    def find_currency(self, currency: Currency):
        raise NameError("method is not accessible")

    def get_node(self, index):
        raise NameError("method is not accessible")

    def get_currency(self, index):
        raise NameError("method is not accessible")

    def print_list(self):
        raise NameError("method is not accessible")

    def count_currency(self):
        raise NameError("method is not accessible")

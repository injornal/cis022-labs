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
        cur = self._start
        new_node = LinkNode(currency)
        new_node.next = cur
        self._start = new_node
        self._count += 1

    def pop(self):
        element = self._start
        self._start = self._start.next
        self._count -= 1
        return element.data

    def peek(self):
        copy_currency = Krone(self._start.data.get_value()) # copy of a Krone object
        return copy_currency

    def printStack(self):
        cur = self._start

        while cur.next:
            cur.data.print()
            print("\t")
            cur = cur.next

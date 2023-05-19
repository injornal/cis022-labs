"""
LAB 3
Kostiantyn Babich, Hyunjong Shin
This assignment is to make singly linked list by using stack and queue.
"""

from singly_linked_list import SinglyLinkedList
from currency import Currency


# Do not use linked list functions in this class
class Queue(SinglyLinkedList):

    def __init__(self) -> None:
        super().__init__()

    def enqueue(self, currency):
        self.add_currency(currency, index=self._count-1)

    def dequeue(self):
        element = self.get_currency(index=0)
        self.remove_currency(element=0)
        return element

    def peekFront(self):
        return self.get_currency(index=0)

    def peekRear(self):
        return self.get_currency(index=self._count-1)

    def printQueue(self):
        self.print_list()


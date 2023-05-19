"""
LAB 3
Kostiantyn Babich, Hyunjong Shin
This assignment is to make singly linked list by using stack and queue.
"""

from singly_linked_list import SinglyLinkedList
from currency import Currency


# Do not use linked list functions in this class
class Stack(SinglyLinkedList):
    
    def __init__(self) -> None:
        super().__init__()

    def push(self, currency: Currency):
        self.add_currency(currency, index=0)

    def pop(self):
        element = self.get_currency(index=0)
        self.remove_currency(element=0)
        return element

    def peek(self):
        return self.get_currency(index=0)

    def printStack(self):
        self.print_list()

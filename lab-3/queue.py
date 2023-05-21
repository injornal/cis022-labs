"""
LAB 3
Kostiantyn Babich, Hyunjong Shin
This assignment is to make singly linked list to make stack and queue.
"""

from singly_linked_list import SinglyLinkedList
from currency import Currency
from krone import Krone


# Do not use linked list functions in this class
class Queue(SinglyLinkedList):

    def __init__(self) -> None:
        super().__init__()

    def enqueue(self, currency: Currency):
        super().add_currency(currency, self._count)

    def dequeue(self):
        removed_item = super().get_currency(0)
        super().remove_currency(0)
        return removed_item

    def peek_front(self):
        return Krone(self._start.data.get_value())  # copy of a Krone object

    def peek_rear(self):
        return Krone(self._end.data.get_value())  # copy of a Krone object

    def print_queue(self):
        super().print_list()

    def add_currency(self, currency: Currency, index):
        raise NameError("method is not accessible")

    def remove_currency(self, element):
        raise NameError("method is not accessible")

    def find_node(self, currency: Currency):
        raise NameError("method is not accessible")

    def find_currency(self, currency: Currency):
        raise NameError("method is not accessible")

    def get_currency(self, index):
        raise NameError("method is not accessible")

    def print_list(self):
        raise NameError("method is not accessible")

    def count_currency(self):
        raise NameError("method is not accessible")

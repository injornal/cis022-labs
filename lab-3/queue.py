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
class Queue(SinglyLinkedList):

    def __init__(self) -> None:
        super().__init__()

    def enqueue(self, currency: Currency):
        new_node = LinkNode(currency)
        if self.is_list_empty():
            self._start = new_node
            self._end = new_node
        else:
            self._end.next = new_node
            self._end = new_node
        self._count += 1

    def dequeue(self):
        if self.is_list_empty():
            raise Exception("Queue is empty")
        else:
            removed_item = self._start.data
            self._start = self._start.next
            if self._start is None:
                self._end = None
            self._count -= 1
            return removed_item

    def peekFront(self):
        return Krone(self._start.data.get_value())  # copy of a Krone object

    def peekRear(self):
        return Krone(self._end.data.get_value())  # copy of a Krone object

    def printQueue(self):
        cur = self._start
        cur.data.print()
        print("\t", end="")
        
        while cur.next:
            cur = cur.next
            cur.data.print()
            print("\t", end="")


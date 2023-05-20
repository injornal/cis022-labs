"""
LAB 3
Kostiantyn Babich, Hyunjong Shin
This assignment is to make singly linked list to make stack and queue.
"""

from currency import Currency


class LinkNode:
    data: Currency = None
    next = None

    def __init__(self, data):
        self.data = data

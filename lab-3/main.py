"""
LAB 3
Kostiantyn Babich, Hyunjong Shin
This assignment is to make singly linked list to make stack and queue.
"""

from krone import Krone
from singly_linked_list import SinglyLinkedList
from stack import Stack
from queue import Queue


def main():
    print("Welcome to the Stack and Queue Implementation using Linked List!")
    print("===========================================")
    print("This program demonstrates the functionality of a stack and a queue")
    print("implemented using linked lists.")
    print("===========================================")
    print("Group Members : Kostiantyn Babich, Hyunjong Shin")

    try:
        array_currency = []
        krone_objects_value = [57.12, 23.44, 87.43, 68.99, 111.22, 44.55, 77.77, 18.36, 543.21, 20.21, 345.67, 36.18,
                               48.48, 101.00, 11.00, 21.00, 51.00, 1.00, 251.00, 151.00]

        for value in krone_objects_value:
            array_currency.append(Krone(value))
        count_currency = len(array_currency)
        
        singly_linked_list = SinglyLinkedList()
        stack = Stack()
        queue = Queue()

        # Linked list operations
        for i in range(7).__reversed__():
            index = 6 - i
            singly_linked_list.add_currency(array_currency[i], index)

        print(f"Kr 87.43 is in index {singly_linked_list.find_currency(Krone(87.43))} in singly_linked_list")
        print(f"Kr 44.56 is in index {singly_linked_list.find_currency(Krone(44.55))} in singly_linked_list")
        # Check this again 44.55 or 44.56?

        singly_linked_list.remove_currency(Krone(111.22))
        singly_linked_list.remove_currency(2)

        singly_linked_list.print_list()
        print()

        for i in range(9, 12 + 1):
            singly_linked_list.add_currency(array_currency[i], i % 5)

        # What is _currency?
        singly_linked_list.remove_currency(count_currency % 6)
        # singly_linked_list.remove_currency(count_currency / 7)

        singly_linked_list.print_list()
        print()

        # Stack operations
        for i in range(7):
            stack.push(array_currency[i + 13])

        stack.peek().print()
        print()

        for i in range(3):
            stack.pop()

        stack.printStack()
        print()

        for i in range(5):
            stack.push(array_currency[i])

        for i in range(2):
            stack.pop()

        stack.printStack()
        print()

        # Queue operations
        for i in range(5, 5 + 7*2, 2):
            queue.enqueue(array_currency[i])

        print(f"The front and end of the queue is ", end="")
        queue.peekFront().print()
        print("and ", end="")
        queue.peekRear().print()
        print()

        for i in range(2):
            queue.dequeue()

        queue.printQueue()
        print()

        for i in range(5):
            queue.enqueue(array_currency[i + 10])

        for i in range(3):
            queue.dequeue()

        queue.printQueue()
        print()

        print("Program ended: Stack and Queue implementation using linked list")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

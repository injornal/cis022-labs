from link_node import LinkNode
from currency import Currency


class SinglyLinkedList:

    def __init__(self):
        self._count = 0
        self._start = LinkNode(None)
        self._end = LinkNode(None)
        self._start.next = self._end
    
    def add_currency(self, currency: Currency, index):
        """The method inserts a currency in a given position
        pre: currency - Currency, the inserting object
            index - integer, the index of the position of the insertion
        post: 
        return:
        """
        cur = self.get_node(index - 1)
        new_node = LinkNode(currency)
        new_node.next = cur.next
        cur.next = new_node
        self._count += 1

    def remove_currency(self, element):
        """The method removes the node by its value or index
        pre: index - integer/Currency, the index/value of the element to be deleted
        post: 
        return:
        """
        if type(element) == int:
            cur = self.get_node(element - 1)
            cur.next = cur.next.next
            self._count -= 1
        elif type(element) == Currency:
            cur = self.get_node(self.find_currency(element))
            cur.next = cur.next.next
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
        if cur.data == currency:
            return index
        while cur.next:
            cur = cur.next
            index += 1
            if cur.data == currency:
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
        cur = self._start.next
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
        cur = self._start.next
        print(cur.data)
        while cur.next:
            cur = cur.next
            print(cur.data)

    def is_list_empty(self):
        """The method returns whether the list is epty
        pre:
        post:
        return: boolean
        """
        return bool(self._count)
    
    def count_currency(self):
        """The method returns the amount of elements in the list
        pre:
        post:
        return: integer
        """
        return self._count

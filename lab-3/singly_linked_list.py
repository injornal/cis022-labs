from link_node import LinkNode
from currency import Currency

class SinglyLinkedList:
    _count = 0
    _start: LinkNode = None
    _end: LinkNode = None

    def __init__(self):
        pass
    
    def add_currency(self, currency: Currency, index):
        """The method inserts a currency in a given position
        pre: currency - Currency, the inserting object
            index - integer, the index of the postion of the insertion
        post: 
        return:
        """
        cur = self.get_node(index - 1)
        new_node = LinkNode(currency)
        new_node.next = cur.next
        cur.next = new_node
        self._count += 1

    def remove_currency(self, index):
        """The method removes the currency emelement at the given position from the list 
        pre: index - integer, the index of the element to be deleted
        post: 
        return:
        """
        cur = self.get_node(index - 1)
        cur.next = cur.next.next 
        self._count -= 1

    def remove_currency(self, currency: Currency):
        """The method removes the currency emelement with the given value from the list 
        pre: index - integer, the index of the element to be deleted
        post: 
        return:
        """
        cur = self.get_node(self.find_currency(currency))
        cur.next = cur.next.next 
        self._count -= 1
    
    def find_node(self, currency: Currency):
        """The method finds a node by its value
        pre: currency - Currency, the value of the searched node
        post:
        return: LinkNode
        """
        if self._start.data == currency:
            return cur
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
        if self._start is None:
            print()
            return
        cur = self._start
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

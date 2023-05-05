"""
LAB 2
Kostiantyn Babich, Hyunjong Shin
This assignment is to make a base class and derived classes and use them to perform several operations
"""

from abc import ABC, abstractclassmethod


class Currency(ABC):
    
    _whole_part = 0
    _fractional_part = 0


    def __init__(self, value):
        super().__init__()
        self.set_value(value)


    def get_value(self):
        """Returns the value of money in self

        :returns: amount of the money assigned
        :rtype: float
        """
        return self._whole_part + self._fractional_part / 100

    def set_value(self, value):
        """Assigns the value to self 
        
        :param value: the value to be assigned
        :type value: float
        """
        self._whole_part = int(value)
        self._fractional_part = int((100 * value ) % 100)


    def add(self, amount):
        """Adds money to self
        
        :param amount: the amont of money to be added
        :type amount: Currency
        """
        self.set_value((self.get_value() * 100 + amount.get_value() * 100) / 100)

    def subtract(self, amount):
        """Subtracts the given value from self
        
        :param amount: the amount of money to be subtracted
        :type amount: Currency
        """
        self.set_value((self.get_value() * 100 - amount.get_value() * 100) / 100)

    def is_equal(self, currency):
        """Return whether the amount of money in self is the same as in the given objects 
        
        :param currency: the object to be compared
        :type currency: Currency
        """
        return self.get_value() == currency.get_value()

    def is_greater(self, currency):
        """Returns whether the amount of money in self is greater than in the object
        
        :param currency: the object to be compared
        :type currency: Currency
        """
        return self.get_value() > currency.get_value()

    @abstractclassmethod
    def print(self):
        """Prints the object
        
        :post: object's value and name
        """
        pass


    def __del__(self):
        pass
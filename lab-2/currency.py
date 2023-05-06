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
        self._set_value(value)


    def get_value(self):
        """Returns the value of money in self

        pre: 
        post:
        return: floating point value
        """
        return self._whole_part + self._fractional_part / 100

    def _set_value(self, value):
        """Assigns the value to self 
        
        pre: value - a floating point value to be assigned
        post:
        return:
        """
        try:
            self._whole_part = int(value)
            self._fractional_part = int((100 * value ) % 100)
        except ValueError:
            print("Ivalid assignment")



    def add(self, currency):
        """Adds money to self
        
        pre: currency - a Curency object, the amont of money to be added
        post: 
        return:
        """
        if type(currency) == type(self):
            self._set_value((self.get_value() * 100 + currency.get_value() * 100) / 100)
        else: 
            print("Invalid addition")

    def subtract(self, currency):
        """Subtracts the given value from self
        
        pre: currency - a Currency object, the amount of money to be subtracted
        post: 
        return: 
        """
        if type(currency) == type(self) and self._is_greater(currency):
            self._set_value((self.get_value() * 100 - currency.get_value() * 100) / 100)
        else:
            print("Invalid subtraction")

    def is_equal(self, currency):
        """Return whether the amount of money in self is the same as in the given objects 
        
        pre: currency - the Currency object to be compared
        post: 
        return: True or False
        """
        if type(currency) == type(self):
            return self.get_value() == currency.get_value()
        else:
            print("Invalid objcect comparison")

    def _is_greater(self, currency):
        """Returns whether the amount of money in self is greater than in the object
        
        pre: currency - the Currency object to be compared
        post: 
        return: True or False
        """
        if type(currency) == type(self):
            return self.get_value() > currency.get_value()
        else:
            print("Invalid objcect comparison")

    @abstractclassmethod
    def print(self):
        """Prints the object
        
        pre:
        post: object's value and name
        return:
        """
        pass


    def __del__(self):
        pass
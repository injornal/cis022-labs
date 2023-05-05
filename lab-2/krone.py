"""
LAB 2
Kostiantyn Babich, Hyunjong Shin
This assignment is to make a base class and derived classes and use them to perform several operations
"""

import currency


class Krone(currency.Currency):
    _name = "Krone"

    def __init__(self, value=0.00):
        super().__init__(value)


    def print(self):
        """Prints the object in form of xx.yy followed by derived currency name

        ex) 1.23 Krone  2.46 Soum
        """
        print(f"{self.get_value():.2f} {Krone._name}", end=' ')


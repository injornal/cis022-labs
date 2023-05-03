import currency


class Krone(currency.Currency):
    _name = "Krone"

    def __init__(self, value):
        super().__init__(value)


    def print(self):
        """Prints the object in form of xx.yy followed by derived currency name

        ex) 1.23 Krone  2.46 Soum
        """
        print(f"{self.get_value()} {Krone._name}")


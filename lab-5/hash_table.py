class HashTable:
    def __init__(self):
        self.size = 29
        self.array = self.size * [None]  # 0 == empty after removal, None == empty from start

    def insert(self, value):
        if self.array[self.hash(value)] is None or self.array[self.hash(value)] == 0:
            self.array[self.hash(value)] = value
        else:
            pass  # quadratic probing

    def remove(self, value):
        pass

    def hash(self, value):
        # (m*w +  n*f) % size
        return (2 * int(value.get_value()) + 3 * int((value.get_value()) * 100) % 100) % self.size
        # maybe it's better to add whole anf fractional getters to Currency

    def resize(self):
        pass  # implement resize: 2x size and rehash; Cycling hash -> resize

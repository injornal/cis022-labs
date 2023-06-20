"""
LAB 5
Kostiantyn Babich, Hyunjong Shin
This assignment is to make a hash table and operate search methods
"""

class HashTable:
    def __init__(self, num_buckets=29) -> None:
        self.num_buckets = num_buckets
        self.buckets = [[] for _ in range(num_buckets)]
        self.size = 29
        self.m = 2
        self.n = 3
        self.collisions = 0
    
    def hash_function(self, key):
        # Calculate the hash value for the key
        whole_value, fractional_value = str(key).split('.')
        whole_value = int(whole_value)
        fractional_value = int(fractional_value)

        return (self.m * whole_value + self.n * fractional_value) % self.size
    
    def insert(self, krone_object):
        key = krone_object.get_value()
        i = 1
        index = self.hash_function(key)
        new_index = index
        while (i < 29) and type(self.buckets[new_index]) != list:
            new_index = (index + i * i) % self.size
            self.collisions += 1
            i += 1
        self.buckets[new_index] = krone_object

    def get_load_factor(self):
        return self.get_number_of_element() / self.num_buckets
    
    def get_number_of_element(self):
        num_element = 0
        for bucket in self.buckets:
            if type(bucket) != list:
                num_element += 1

        return num_element

    def get_collision_count(self):
        return self.collisions
    
    def search(self, krone_object):
        key = krone_object.get_value()
        i = 1
        index = self.hash_function(key)
        new_index = index
        while i < 29:
            if self.buckets[new_index] == krone_object:
                return new_index
            new_index = (index + i * i) % self.size
            i += 1
        return None 
    
    def resize(self):
        self.num_buckets = self._next_prime(self.num_buckets * 2)
        buckets = self.buckets
        self.buckets = [[] for _ in range(self.num_buckets)]
        for item in buckets:
            if item != 0 and type(item) != list:
                self.insert(item)

    def _next_prime(self, num):
        while not self._is_prime(num):
            num += 1
        return num

    def _is_prime(self, num):
        for i in range(2, int(num ** 0.5)):
            if num % i == 0:
                return False
        return True
    
    def print(self):
        for a in self.buckets:
            if a is None or type(a) == list:
                print(f"{a}, ", end="")
            else:
                a.print()
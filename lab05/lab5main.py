"""
LAB 5
Kostiantyn Babich, Hyunjong Shin
This assignment is to make a hash table and operate search methods
"""

from krone import Krone
from hash_table import HashTable

value_array = [57.12, 23.44, 87.43, 68.99, 111.22, 44.55, 77.77, 18.36, 543.21, 20.21, 345.67, 36.18, 48.48, 101.00,
                   11.00, 21.00, 51.00, 1.00, 251.00, 151.00]

krone_array = list(Krone(a) for a in value_array)

a = HashTable(29)
for krone in krone_array:
    a.insert(krone)

a.print()
print()
print("The number of data items loaded:", a.get_number_of_element())
print("Load Factor:", a.get_load_factor())
print("Number of Collisions:", a.get_collision_count())

user_input = 'y'
while user_input == 'y':
    raw_input = input("Enter a Krone to search for: ")
    target_object = Krone(float(raw_input.split()[1]))
    if a.search(target_object) == None:
        print("Invalid Data")
    else:
        print(f"The object Krone {target_object.get_value()} is found in index {a.search(target_object)}.")
    
    user_input = input("Press 'y' if you want to check again or 'q' to quit. ")

"""
LAB 4
Kostiantyn Babich, Hyunjong Shin
This assignment is to make a binary search tree and operate traversal methods and other operations
"""

from krone import Krone
from bst import BST


def print_tree(tree):
    bft = tree.breadth_first_traversal(tree.get_head())
    it = tree.inorder_traversal(tree.get_head())
    pre = tree.preorder_traversal(tree.get_head())
    post = tree.postorder_traversal(tree.get_head())
    with open("output.txt", "a") as f:
        f.write(str(bft) + "\n")
        print(bft)
        f.write(str(it) + "\n")
        print(it)
        f.write(str(pre) + "\n")
        print(pre)
        f.write(str(post) + "\n")
        print(post)


def main():
    init = """"Welcome to the BST  
===========================================                      
This program demonstrates the functionality of a binary search tree                                 
===========================================                   
Group Members : Kostiantyn Babich, Hyunjong Shin"""
    helper = """Actions:
a - add
d - delete
p - print
q - quit
s - search
"""
    print(init)
    print()
    print(helper)
    value_array = [57.12, 23.44, 87.43, 68.99, 111.22, 44.55, 77.77, 18.36, 543.21, 20.21, 345.67, 36.18, 48.48, 101.00,
                   11.00, 21.00, 51.00, 1.00, 251.00, 151.00]
    krone_array = list(Krone(a) for a in value_array)
    tree = BST()
    for a in krone_array:
        tree.insert(a)

    print_tree(tree)

    ad_actions = {
        "a": tree.insert,
        "d": tree.delete,
    }

    while True:
        try:
            data = input()
            if data == "q":
                break

            data = data.split()
            action = data[0]
            if action in ad_actions:
                ad_actions[action](Krone(float(data[2])))
            elif action == "s":
                node = tree.search(Krone(float(data[2])))
                if node:
                    node.data.print()
                    print()
                else:
                    print("Not found")
            elif action == "p":
                print_tree(tree)
            elif action == "help":
                print(helper)
            else:
                raise ValueError("No such action")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()

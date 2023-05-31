class BSTNode:
    def __init__(self, data):
        self.data = data    # data will be Krone object
        self.left = None
        self.right = None

    def get_data(self):
        return self.data
    
    def get_left(self):
        return self.left

    def get_right(self):
        return self.right
    
    def set_data(self, data):
        self.data = data

    def set_left(self, bst_node):
        self.left = bst_node

    def set_right(self, bst_node):
        self.right = bst_node
from currency import Currency

class LinkNode:
    data: Currency = None
    next = None

    def __init__(self, data):
        self.data = data

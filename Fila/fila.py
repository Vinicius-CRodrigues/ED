import random

class queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, data):
        self.items.append(data)
    
    def is_empty(self):
        return True if len(self.items) == 0 else False
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.remove(0)
    
    def size(self):
        return len(self.items)


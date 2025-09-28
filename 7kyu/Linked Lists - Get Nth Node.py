from preloaded import Node

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    current = node
    count = 0
    
    # рухаємося по списку
    while current is not None:
        if count == index:   # знайшли потрібний вузол
            return current
        count += 1
        current = current.next
        
    raise Exception("Index out of range")

  
#singly linear linked list
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self, new_node):
        
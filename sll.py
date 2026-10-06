#singly linear linked list
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self, new_node):
            temp=self.head
            while temp.next:
                 temp=temp.next
            temp.next=new_node #appending new node
    def print(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next

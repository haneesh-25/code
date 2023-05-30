class Node:
    def __init__(self,val=None) -> None:
        self.val = val
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.head = Node()
    def push(self,val):
        if self.head!=None:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
            return
        self.head.val = val
    def pop(self):
        if self.head!=None:
            top = self.head.val
            self.head = self.head.next
            return top
        print('stack underflow')
    def peek(self):
        if self.head!=None:
            return self.head.val
        return False
    def size(self):
        count = 0
        ptr = self.head
        while ptr!=None:
            ptr=ptr.next
            count+=1
        return count
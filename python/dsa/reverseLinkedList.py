#node declare
class Node:
    def __init__(self, val=None):
        self.val  = val
        self.next = None

#build linkedList 1
head = Node(1)
a1 = Node(2)
a2 = Node(3)
a3 = Node(4)
a4 = Node(5)
head.next = a1
a1.next = a2
a2.next = a3
a3.next = a4

prev = nextNode = Node()

prev = head
head = head.next
prev.next = None
#reverse LinkedList
while head!=None:
    nextNode = head.next
    head.next = prev
    prev = head
    head = nextNode

#print linkedList 
temp = prev
while temp != None:
    print(temp.val)
    temp = temp.next
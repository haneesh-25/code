class Node:
    def __init__(self, val=None):
        self.val  = val
        self.next = None

#build linkedList 1
head = Node(1)
a1 = Node(2)
a2 = Node(3)
a3 = Node(2)
a4 = Node(1)
head.next = a1
a1.next = a2
a2.next = a3
a3.next = a4

def sumOfLinkedList(head):
    if head == None:
        return 0
    sum = head.val + sumOfLinkedList(head.next)
    return sum

print(sumOfLinkedList(head))
#node declare
class Node:
    def __init__(self, val=None):
        self.val  = val
        self.next = None

#build linkedList 1
head = Node(1)
a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(3)
head.next = a1
a1.next = a2
a2.next = a3
a3.next = a4

ans = ptr = Node()
ans = head
while head.next!=None:
    if head.val == head.next.val:
        ptr = head
        while head.next!=None and ptr.val == head.next.val:
            head = head.next
        ptr.next = head.next
        continue
    head = head.next

#print linkedList 
temp = ans
while temp != None:
    print(temp.val)
    temp = temp.next

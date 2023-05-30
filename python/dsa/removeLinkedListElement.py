#node declare
class Node:
    def __init__(self, val=None):
        self.val  = val
        self.next = None

#build linkedList 1
head = Node(7)
a1 = Node(7)
a2 = Node(7)
a3 = Node(7)
a4 = Node(7)
head.next = a1
a1.next = a2
a2.next = a3
a3.next = a4

def removeElements(head,val):
    top = head
    prev = head
    while head!=None:
        if head.val == val:
            if prev==head:
                head = head.next
            else:
                prev.next = head.next
        prev = head
        head=head.next
    return top

removeElements(head,7)
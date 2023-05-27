#node declare
class Node:
    def __init__(self, val=None):
        self.val  = val
        self.next = None

#build linkedList 1
AHead = Node(1)
a1 = Node(2)
a2 = Node(4)
AHead.next = a1
a1.next = a2

#build linkedList 2
BHead = Node(9)
n1 = Node(3)
n2 = Node(4)
BHead.next = n1
n1.next = n2

BHead.next = AHead
AHead = BHead

temp = AHead
while temp != None:
    print(temp.val)
    temp = temp.next
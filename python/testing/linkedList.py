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
BHead = Node(1)
n1 = Node(3)
n2 = Node(4)
BHead.next = n1
n1.next = n2

#sort merge two sorted list
ptrOne = AHead
ptrTwo = BHead

while ptrOne.next!=None and ptrTwo!=None:
    if ptrOne.val<=ptrTwo.val and ptrOne.next.val>ptrTwo.val:
        temp = Node(ptrTwo.val)
        temp.next = ptrOne.next
        ptrOne.next = temp
        ptrTwo = ptrTwo.next
    elif ptrOne.val>=ptrTwo.val:
        temp = Node(ptrTwo.val)
        temp.next = ptrTwo.next
        AHead = ptrTwo
        ptrTwo.next = ptrOne
        ptrTwo = temp.next
        continue
    ptrOne = ptrOne.next


#print linkedList 
temp = AHead
while temp != None:
    print(temp.val)
    temp = temp.next
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

my_list = []
while head!=None:
    my_list.append(head.val)
    head = head.next
# for i in range(len(my_list)-1//2):
#     if my_list[i] != my_list[-i]:
#         return False
#     return True
print(len(my_list))
print(my_list)
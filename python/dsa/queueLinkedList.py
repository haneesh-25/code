class Node:
    def __init__(self,val=None) -> None:
        self.val = val
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.front = self.rear = None
    def EnQueue(self,val):
        temp = Node(val)
        if self.rear==None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = self.rear.next
    def DeQueue(self):
        if self.front==None:
            return False
        self.front = self.front.next
        if self.front==None:
            self.rear = self.front

q = Queue()
q.EnQueue(10)
q.EnQueue(20)
q.DeQueue()
q.DeQueue()
q.EnQueue(30)
q.EnQueue(40)
q.EnQueue(50)
q.DeQueue()
enumerate
class Stack:
    def __init__(self,capacity) -> None:
        self.capacity = capacity
        self.A = [None]*capacity
        self.top = -1
    def push(self,data):
        if self.top+1 == self.capacity:
            print('stack overflow: trying to increase size')
            self.resize(1)
        self.top = self.top+1
        self.A[self.top] = data
    def pop(self):
        if self.top == -1:
            print("stack underflow: trying to decrease size")
            self.resize(0)
        self.top = self.top-1
    def  peek(self):
        if self.top == -1:
            print("No elements in the list")
            return
        print(self.A[self.top])
    def resize(self,val):
        if val==1:
            self.capacity = self.capacity*2
            newArray = [None]*self.capacity
            for i in range(0,self.top+1):
                newArray[i] = self.A[i]
            self.A = newArray
        else:
            self.capacity = self.capacity//2
            newArray = [None]*self.capacity
            for i in range(0,self.top+1):
                newArray[i] = self.A[i]
            self.A = newArray        
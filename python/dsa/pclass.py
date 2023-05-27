class hello:
    def __init__(self,name) -> None:
        self.name = name
    def greet(self):
        print('hello '+ self.name)

hello(input('name :')).greet()
import Stack

stack = Stack.Stack()
def isValidExpression(expression):
    mapping ={')':'(',']':'[','}':'{'}
    for symbol in expression:
        if mapping.get(symbol):
            if stack.pop() == mapping[symbol]:
                continue
            return False
        else:
            stack.push(symbol)
    return not stack.peek()

print(isValidExpression(input('input symbols: ')))

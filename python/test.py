inString = input('enter a string :')

for i in range(len(inString)):
    if inString[i].isupper():
        inString= inString[:i] + ' ' + inString[i].lower() + inString[i+1:]

print(inString)

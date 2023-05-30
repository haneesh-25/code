from numpy import sqrt 

def constructRectangle(area):
    length=width=0
    root = int(sqrt(area))
    for i in range(1,root):
        if area/i == area//i:
            length,width = area//i,i
    return [length,width]

area = 4
print(constructRectangle(area))
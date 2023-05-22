def binary_search(test):
    middle = len(test)//2
    if search==test[middle]:
        return middle
    elif middle == 1:
        return -1
    else:
        if test[middle]>search:
            return binary_search(test[:middle])
        else:
            return middle + binary_search(test[middle:])

test = [1,2,3,4,5,6,7,8,9]
global search
search = 9
print(binary_search(test))
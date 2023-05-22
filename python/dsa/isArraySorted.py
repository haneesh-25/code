def isArraySorted(A):
    if len(A)==1:
        return True
    return A[0]<=A[1] and isArraySorted(A[1:])

A = [0, 5, 10, 12, 15, 20, 19, 30, 35, 40]
print(isArraySorted(A))
def sumOfList(A):
    if len(A)==1:
        return A[0]
    return A[0] + sumOfList(A[1:])

A = [1,2,4,6,9,8]
print(sumOfList(A))
def myfunc(n):
    prev = 1
    prev2 = 0
    for i in range(1, n+1):
        curi = prev + prev2
        prev2 = prev
        prev = curi
    return prev 

print(myfunc(4))
def rangeKList(K):
    result = []
    for i in range(0,K):
        result.append(str(i))
    return result

def baseKStrings(n,K):
    if n==1:
        return rangeKList(K)
    return[strings + baseKString for strings in baseKStrings(1,K) for baseKString in baseKStrings(n-1,K)]

print(baseKStrings(3,3))
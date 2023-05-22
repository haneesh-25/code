def BinaryStrings(N):
    if N==1: return ['0','1']
    return [digit + BinaryString for digit in BinaryStrings(1) for BinaryString in BinaryStrings(N-1)]

print(BinaryStrings(3))
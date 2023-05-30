def largestHistrogram(A):
    maxArea = 0
    for i in range(len(A)):
        Heighti = A[i]
        for j in range(i+1, len(A)):
            minimumHeight = min(Heighti, A[j])
            maxArea = max(maxArea,(j-i)*minimumHeight)
    return maxArea
A = [1,8,6,2,5,4,8,3,7]
print ("largestRectangleArea: ", largestHistrogram(A))

def checkPath(position,imatrix,N):
    if position == (N-1,N-1):
        return (N-1,N-1)
    i,j = position
    if i+1<N and imatrix[i+1][j]==1:
        a=checkPath((i+1,j),imatrix,N)
        if a!=None:
            return a
    if j+1<N and imatrix[i][j+1]==1:
        b=checkPath((i,j+1),imatrix,N)
        if b!=None:
            return b
i,j = 0,0
N = 5
imatrix = [[1,1,1,1,0], [0,1,0,1,0], [0,1,0,1,0], [0,1,0,0,0], [1,1,1,1,1]]
print(checkPath((i,j),imatrix,N))
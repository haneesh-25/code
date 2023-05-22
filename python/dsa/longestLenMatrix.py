
def findSize(i,j,maxr,maxc):
    

global size, tarr, maxsize, iarr
iarr = [[1,1,0,0,0],[0,1,1,0,1],[0,0,0,1,1],[1,0,0,1,1],[0,1,0,1,1]]
maxr = len(iarr)
maxc = len(iarr[0])
tarr = maxr*[maxc*[0]]
size = 0
maxsize = 0
for i in range(maxr):
    for j in range(maxc):
        if iarr[i][j]==1 and tarr[i][j]==0:
            findSize(i,j,maxr,maxc)
print(maxsize)
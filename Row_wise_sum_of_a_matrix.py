r,c=map(int,input().split())
mat=[]
for i in range(r):
    x=list(map(int,input().split()))
    mat.append(x)
for i in mat:
    print(sum(i),end=' ')
    

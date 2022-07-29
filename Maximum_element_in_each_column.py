r,c=map(int,input().split())
m=[]
for i in range(r):
    l=[int(i)for i in input().split()]
    m.append(l)
for i in range(c):
    k=[]
    for j in range(r):
        k.append(m[j][i])
    print(max(k))
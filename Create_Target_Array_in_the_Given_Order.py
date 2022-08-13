n=int(input())
c=[int(i)for i in input().split()]
m=int(input())
d=[int(i)for i in input().split()]
k=[]
for i in range(n):
    k.insert(d[i],c[i])
print(*k)
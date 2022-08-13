n=int(input())
c=[int(i)for i in input().split()]
b=[]
for i in c:
    s=0
    for j in range(n):
     if c[j]<i:
         s+=1
    b.append(s)
print(*b)
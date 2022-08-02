n=int(input())
c=[]
for i in range(n):
    k=int(input())
    c.append(k)
m=int(input())
s=0
for i in c:
    if i<=m:
        s+=1
    else:
        s+=2
print(s)
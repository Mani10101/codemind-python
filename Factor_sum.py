def fac(n):
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s+=i
    return s
n=[int(i)for i in input().split(',')]
c=[]
for i in n:
    k=fac(i)
    if k in n:
        c.append(i)
c=sorted(c)
if len(c)==0:
    print(-1)
else:
    print(*c)


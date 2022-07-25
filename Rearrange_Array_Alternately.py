n=int(input())
for i in range(n):
    k=int(input())
    l=[int(i)for i in input().split()]
    c=[]
    a=len(l)//2
    while a!=0:
        c.append(max(l))
        c.append(min(l))
        l.remove(max(l))
        l.remove(min(l))
        a-=1
    for i in l:
        if i not in c:
            c.append(i)
    print(*c)

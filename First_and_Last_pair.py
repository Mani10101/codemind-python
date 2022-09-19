n=int(input())
l=[int(i)for i in input().split()]
c=[0]*n
a=0
p=0
b=-1
o=0
while n!=0:
    if o==0:
        c[a]=l[p]
        o=1
        a+=1
        p+=1
    else:
        c[a]=l[b]
        b-=1
        a+=1
        o=0
    n-=1
if len(l)%2!=0:
    c.append(0)
    print(*c)
else:print(*c)
    
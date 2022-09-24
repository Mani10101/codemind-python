n=int(int(input()))
l=[int(i)for i in input().split()]
l=(sorted(l))
c=[0]*n
a=0
b=1
for i in range(n-2,-1,-2):
    c[a],c[b]=l[i],l[i+1]
    a+=2
    b+=2
if n%2!=0:
    c[n-1]=l[0]
    print(*c)
else:
    print(*c)
    

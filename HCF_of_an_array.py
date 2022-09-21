n=int(input())
l=[int(i)for i in input().split()]
while n!=1:
    a=0
    b=0
    for i in range(n-1):
        if l[i]>l[i+1]:
            a,b=l[i+1],l[i]
        else:
            a,b=l[i],l[i+1]
        o=0
        while o<=b:
            o+=1
            if (o*a)%b==0:
                l[i]= (a*b//(o*a))
                break
    l.pop()
    n-=1
print(*l)
    

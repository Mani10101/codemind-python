n,m=map(int,input().split())
a=[int(i)for i in input().split()]
b=len(a)
j=1
s=0
while j<=b:
    for i in range(b):
        if i+j<=b and sum(a[i:j+i])==m:
            s+=1
            
    j+=1
print(s)

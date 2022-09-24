n=int(input())
m=int(input())
a=[i for i in range(n,m+1)]
b=len(a)
j=1
s=0
while j<=b:
    for i in range(b):
        if i+j<=b and sum(a[i:j+i])%2!=0:
            s+=1
            
    j+=1
print(s)

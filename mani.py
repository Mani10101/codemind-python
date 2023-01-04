def prime(n):
    if n==1:return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:return False
    else:return True

def smallnum(n):
    o=2
    s=0
    temp=n
    while n>0 and o<=n:
        if n%o==0:
            if prime(o):
                s+=o
                n=n//o
            else:o+=1
        else:o+=1
    return s
n=int(input())
temp=smallnum(n)
while temp!=smallnum(temp):
    temp=smallnum(temp)
print(temp)
    

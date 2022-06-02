def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
f=0
for i in range(1,n+1):
    if n%i==0 and prime(i)!=True:
        f+=1
print(f)
        
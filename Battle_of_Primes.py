def prime(n):
    f=0
    for i in range(1,n+1):
        if n%i==0:
            f+=1
    if f==2:
        return True
    else:
        return False
def nprime(n):
    while prime(n)==False:
        n=n+1
    return n
a=int(input())
b=int(input())
c=a+b
p=nprime(c)
if prime(c)==True:
    p=nprime(c+1)
    print(abs(c-p))
else:
    print(abs(c-p))
def pali(n):
    s=0
    k=n
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if k==s:
        return True
    else:
        return False
def pre_pali(n):
    while pali(n)!=True:
        n=n-1
    return(n)
def next_pali(n):
    while pali(n)!=True:
        n=n+1
    return(n)
x=int(input())
p=pre_pali(x)
q=next_pali(x)
if pali(x)==True:
    p=pre_pali(x-1)
    q=next_pali(x+1)
    print(p,q)
elif x-p < q-x:
    print(p)
elif x-p > q-x:
    print(q)
elif x-p == q-x:
    print(p,q)


n=int(input())
k=n
s=0
while n!=0:
    i=1
    f=1
    r=n%10
    while i<=r:
        f=f*i
        i+=1
    n=n//10
    s+=f
if s==k:
    print('The number {} is a strong number'.format(k))
else:
    print('The number {} is not a strong number'.format(k))

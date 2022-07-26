n,k,q=map(int,input().split())
l=[int(i)for i in input().split()]
while k!=0:
    l.insert(0,l[n-1])
    l.pop()
    k-=1
for i in range(q):
    m=int(input())
    print(l[m])

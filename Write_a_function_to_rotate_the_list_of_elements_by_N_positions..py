n=int(input())
l=list(map(int,input().split()))
k=int(input())
while k!=0:
    l.insert(0,l[-1])
    l.pop()
    k-=1
print(*l)
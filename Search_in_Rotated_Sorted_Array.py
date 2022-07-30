n=int(input())
l=list(map(int,input().split()))
k=int(input())
if k in l:
    print(l.index(k))
else:
    print(-1)
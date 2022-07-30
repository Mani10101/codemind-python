n=int(input())
l=list(map(int,input().split()))
k=int(input())
l2=l[::-1]
if k in l:
    print(l.index(k),end=' ')
else:
    print(-1,end=' ')
if k in l2:
    print(abs(l2.index(k)-(n-1)),end=' ')
else:
    print(-1,end=' ')

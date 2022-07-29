n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    s=1
    for j in range(n):
        if l[i]!=l[j]:
            s=s*l[j]
    print(s,end=' ')
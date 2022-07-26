n=int(input())
for i in range(n):
    k,m=map(int,input().split())
    l1=[int(i)for i in input().split()]
    l2=[int(i)for i in input().split()]
    l1.extend(l2)
    l1=sorted(l1)
    print(*l1)
n=int(input())
for i in range(n):
    k=int(input())
    a=[i for i in range(1,k+1)]
    b=[int(i)for i in input().split()]
    c=[i for i in a if i not in b]
    print(*c)
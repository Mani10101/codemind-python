for i in range(int(input())):
    n,m=map(int,input().split())
    c=[int(i)for i in input().split()]
    while m!=0:
        c.insert(0,c[-1])
        c.pop()
        m-=1
    print(*c)
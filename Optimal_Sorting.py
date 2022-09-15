for i in range(int(input())):
    n=int(input())
    m=[int(i)for i in input().split()]
    if sorted(m)==m:
        print(0)
    else:
        print(max(m)-min(m))
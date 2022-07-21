n=int(input())
for i in range(n):
    k=int(input())
    l=input()
    f=0
    for i in l:
        if l.count(i)==1:
            print(i)
            f=1
            break
    if f==0:
        print(-1)
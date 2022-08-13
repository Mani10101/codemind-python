n=int(input())
c=[int(i)for i in input().split()]
m=int(input())
for i in c:
    if i+m>=max(c):
        print(True,end=' ')
    else:
        print(False,end=' ')
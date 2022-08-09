n=int(input())
a=[int(i)for i in input().split()]
b=[int(i)for i in input().split()]
if sum(a)<sum(b):
    print(sum(b)-sum(a))
else:
    print(0)
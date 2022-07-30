n=int(input())
l=list(map(int,input().split()))
a=[i**2 for i in l]
print(*sorted(a))
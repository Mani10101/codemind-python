n=int(input())
k=[int(i)for i in input().split()]
s=[i for i in k if i%2==0]
m=[i for i in k if i%2!=0]
print(len(s),len(m))
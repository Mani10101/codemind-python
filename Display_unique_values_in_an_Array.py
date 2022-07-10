a=int(input())
l=list(map(int,input().split()))
v=[]
f=0
for i in l:
    if l.count(i)==1:
        v.append(i)
        f=1
if f==1:
    print(*v)
else:
    print('-1')
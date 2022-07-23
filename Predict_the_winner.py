n=int(input())
l=list(map(int,input().split()))
x=[]
y=[]
for i in range(n//2):
    x.append(l[i])
for j in range(n//2,n):
    y.append(l[j])
if abs(sum(x)-sum(y))%4==0:
    print('X')
else:
    print('Y')

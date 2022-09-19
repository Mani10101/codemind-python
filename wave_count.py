n=int(input())
l=[int(i)for i in input().split()]
s=0
c=0
for i in range(n-1):
    if l[i]-l[i+1]<=0:
        c+=-1
    else:c+=1
    if c>1 or c<-1:
        print(-1)
        break
    elif c==0:s+=1
else:print(s)
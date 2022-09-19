m=int(input())
n=[int(i)for i in input().split()]
c=0
for i in range(m-1):
    if n[i]-n[i+1]<=0:c+=1
    else:c-=1
    if c>1 or c<-1:
        print('no')
        break
else:
    print('yes')
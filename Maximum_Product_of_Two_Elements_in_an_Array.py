l=list(map(int,input().split()))
c=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        c.append((l[i]-1)*(l[j]-1))
print(max(c))

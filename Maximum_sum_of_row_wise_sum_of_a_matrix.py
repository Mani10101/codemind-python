r,c=map(int,input().split())
m=[]
for i in range(r):
        li=list(map(int,input().split()))[:c]
        m.append(li)
a=[]
for i in range(r):
        a.append(sum(m[i]))
print(max(a))

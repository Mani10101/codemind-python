r,c=map(int,input().split())
m=[]
for i in range(r):
        li=list(map(int,input().split()))[:c]
        m.append(li)
s=0
for i in range(c):
        s=0
        for j in range(r):
                s+=m[j][i]
        print(s,end=' ')

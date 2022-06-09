n=int(input())
li=list(map(int,input().split()))
a=[]
for i in li:
    a.append(len(str(i)))
for i in li:
    if len(str(i))==max(a):
        print(i,end=' ')

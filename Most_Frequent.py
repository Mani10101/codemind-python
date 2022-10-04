n=input()
a=[int(i)for i in input().split()]
d={}
for i in a:
    if i not in d:d[i]=1
    else:d[i]+=1
o=0
l=0
for k,v in d.items():
    if v>o:
        o=v
        l=k
print(l)


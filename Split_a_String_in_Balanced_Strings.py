n=input()
c=0
s=0
for i in n:
    if i=='R':
        c+=1
    else:
        c-=1
    if c==0:
        s+=1
print(s)
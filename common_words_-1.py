n=input().lower()
m=input().lower()
a=n.split()
b=m.split()
c=[]
for i in a:
    if i in b and i not in c and i!=' ':
        c.append(i)
for i in b:
    if i in a and i not in c and i!=' ':
        c.append(i)
print(len(c))

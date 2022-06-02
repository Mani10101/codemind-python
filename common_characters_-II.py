n=input().lower()
m=input().lower()
a=set(n)
b=set(m)
f=0
for i in a:
    if i in b and i!=' ':
        f+=1
print(f)
    

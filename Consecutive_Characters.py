n=input()
c=0
r=0
for i in range(len(n)-1):
    if n[i]==n[i+1]: c+=1
    else: c=0
    if c>r:
        r=c
print(r+1)
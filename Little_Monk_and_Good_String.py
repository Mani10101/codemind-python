n=input()
c=0
r=0
for i in range(len(n)):
    if n[i]=='a': c+=1
    elif n[i]=='e': c+=1
    elif n[i]=='i': c+=1
    elif n[i]=='o': c+=1
    elif n[i]=='u': c+=1
    else: c=0
    if c>r: r=c
print(r)
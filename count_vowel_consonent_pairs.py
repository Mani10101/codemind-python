n=input()
a='aeiouAEIOU'
f=0
for i in range(len(n)):
    if n[i] not in a and n[i]!=' ' and n[(len(n)-1)-i] in a:
        f+=1
print(f)

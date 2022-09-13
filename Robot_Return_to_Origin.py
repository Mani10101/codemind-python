n=input()
c=0
for i in n:
    if i=='R': c+=1
    elif i=='U': c+=1
    elif i=='D': c-=1
    else:c-=1
print(c==0)
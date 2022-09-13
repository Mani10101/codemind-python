n=input()
d={}
for i in n:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
a=sorted(set(d.values()))
if len(a)==1:
    print(-1)
else:
    for k,v in d.items():
        if v==a[-2]:
            print(k)
            break
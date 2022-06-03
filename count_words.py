li=list(map(str,input().split()))
a='aeiouAEIOU'
f=0
for i in li:
    if i[0] in a and i[len(i)-1] not in a:
        f+=1
print(f)

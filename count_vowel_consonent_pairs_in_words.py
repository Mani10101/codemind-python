n=list(map(str,input().split()))
a='aeiouAEIOU'
f=0
for i in n:
    for j in range(len(i)):
        if i[j] in a and i[(len(i)-1)-j] not in a:
            f+=1
print(f)

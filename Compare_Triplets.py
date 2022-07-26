l=[int(i)for i in input().split()]
m=[int(i)for i in input().split()]
a=0
b=0
for i in range(len(l)):
    if l[i]>m[i]:
        a+=1
    elif l[i]==m[i]:
        pass
    else:
        b+=1
print(a,b)


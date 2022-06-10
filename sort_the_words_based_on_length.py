n=input().lower()
l=n.split()
l.sort(key=len)
for i in range(len(l)-1):
    if len(l[i])==len(l[i+1]) and l[i]> l[i+1]:
        l[i],l[i+1]=l[i+1],l[i]
print(' '.join(l))
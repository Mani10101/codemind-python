n=input()
a=[]
for i in n:
    if i not in a:
        a.append(i)
for i in range(len(a)-1):
    if n.count(a[i])*2==n.count(a[i+1]):
        print('Yes')
    else:
        print('No')
    

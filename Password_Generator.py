n=input()
n=n.split(",")
o=''
for i in n:
    c=-1
    a=i.split(':')
    b=sorted(a[1])
    p=0
    while c>=len(b)*-1:
        if int(b[c])<=len(a[0]):
            s=int(b[c])-1
            o+=a[0][s]
            p=1
            break
        else:c-=1
    if p==0:o+="X"
print(o)
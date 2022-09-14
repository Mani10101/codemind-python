n=input().split()
s='a'
c=''
d=0
for i in n:
    if i[0]=='a' or i[0]=='e' or i[0]=='u' or i[0]=='i' or i[0]=='o':
        c+=i+'ma'+s
        if d<len(n)-1:
            c+=' '
        d+=1
        s+='a'
    else:
        c+=i[1::]+i[0]+'ma'+s
        s+='a'
        if d<len(n)-1:
            c+=' '
        d+=1
        
print(c)

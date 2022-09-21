n=input()
n=list(n)
s=''
for i in range(len(n)):
    if n[i]=='a' or n[i]=='e' or n[i]=='i' or n[i]=='o' or n[i]=='u':
        n[i]='V'
    else:n[i]='C'
for i in range(len(n)-1):
    if n[i]!=n[i+1]:
        s+=n[i]
print(s+n[-1])

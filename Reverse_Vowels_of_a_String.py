
n=input()
n=list(n)
s=''
for i in n:
    if i.lower()=='a' or i.lower()=='e' or i.lower()=='i' or i.lower()=='o' or i.lower()=='u':
        s+=i
a=-1
for i in range(len(n)):
    if n[i].lower()=='a' or n[i].lower()=='e' or n[i].lower()=='i' or n[i].lower()=='o' or n[i].lower()=='u':
        n[i]=s[a]
        a-=1
print(''.join(n))

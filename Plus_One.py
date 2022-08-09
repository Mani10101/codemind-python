n=int(input())
l=[int(i)for i in input().split()]
s=''
for i in l:
    s+=str(i)
a=int(s)+1
c=[]
while a!=0:
    r=a%10
    c.append(r)
    a=a//10
c=c[::-1]
print(*c)

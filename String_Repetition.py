n=input()
m=int(input())
a=m%len(n)
s=0
if a!=0:
	for i in range(a):
		if n[i]=='a':
			s+=1
b=m//len(n)
c=n.count('a')*b+s
print(c)
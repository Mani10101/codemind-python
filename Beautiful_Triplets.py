n=int(input())
l=[int(i)for i in input().split()]
b=n
while b!=0:
	print(b)
	a=min(l)
	s=0
	for i in range(n):
		if l[i]-a==0:
			l[i]=8688
			s+=1
	b=b-s
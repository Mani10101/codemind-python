n=input().lower()
a=n.split()
f=0
for i in a:
	print(i[::-1]==i)
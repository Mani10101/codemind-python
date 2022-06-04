n=input().lower()
a=n.split()
f=0
for i in a:
	if i[::-1]==i:
		f+=1
print(f)
n=input()
n=n.split(':')
a=(int(n[0])+int(n[1])/60)*30
b=int(n[1])*6
c=abs(b-a)
d=360-c
if d<c:print(d)
else:print(c)
n=input()
m=input()
a=list(n)
b=list(m)
a.extend(b)
a.sort()
print(''.join(a))

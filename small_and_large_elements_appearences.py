n=input()
a=[i for i in n if i.isalnum()]
b=min(a)
c=max(a)
print(b,a.count(b),c,a.count(c))

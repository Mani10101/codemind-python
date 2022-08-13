n=int(input())
c=[int(i)for i in input().split()]
for i in range(n):
    if c[i]==0:
        c.append(c[i])
        c.remove(c[i])
print(*c)
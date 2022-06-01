n=int(input())
for i in range(n):
    k=input()
    a=[i for i in k if i.isdigit()]
    if len(a)!=0:
        print('Yes')
    else:
        print('No')
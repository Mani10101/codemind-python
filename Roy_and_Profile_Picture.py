n=int(input())
for i in range(int(input())):
    l,m=map(int,input().split())
    if l<n or m<n: print('UPLOAD ANOTHER')
    elif l==m: print('ACCEPTED')
    else: print('CROP IT')
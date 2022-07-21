n=int(input())
for i in range(n):
    k=input()
    f=0
    for i in range(len(k)-1):
        if k[i]==k[i+1]:
            f+=1
    print(f)
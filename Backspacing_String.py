def back_space(arr):
    arr=list(arr)
    for i in range(len(arr)):
        if arr[i]=='#':
            arr[i]='@'
            if arr[i-1]=='@':
                c=i-1
                while True:
                    if arr[c]!='@':
                        arr[c]='@'
                        break
                    else:c-=1
                    if c<0:
                        break
            else:
                if i>0:
                    arr[i-1]='@'
    s=''
    for i in arr:
        if i!='@':s+=i
        else:pass
    return s
n=input()
m=input()
print(back_space(n)==back_space(m))

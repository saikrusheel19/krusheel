N=int(input('enter the no.of strings'))
a=[]
b=''
for i in range (N):
    c=input('')
    a.append(c)
for i in range(N-1):
    d=a[i]
    e=a[i+1]
    for y in range(len(min(a,key=len))):
        if d[y]==e[y]:
            b+=d[y]
        else:
            break
    a.pop(i)
    a.insert(0,b)
    b=''
print(a[0])

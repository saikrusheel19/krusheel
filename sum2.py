n=int(input())
num=list(map(int,input().split()))
k=0

for i in range(0,n):

    for j in range(0,i):
        if num[j]<num[i]:
            k=k+num[j]

print(k)

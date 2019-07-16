a,b=map(int,input().split())
n=list(map(int,input().split()))
m=[]
for a in range(b):
       j,k=map(int,input().split())
       m.append(sum(n[j-1:k]))
for j in m:
       print(j)

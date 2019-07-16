j,k=map(int,input().split())
n=list(map(int,input().split()))
m=[]
for j in range(k):
       a,b=map(int,input().split())
       m.append(sum(n[a-1:b]))
for a in m:
       print(a)

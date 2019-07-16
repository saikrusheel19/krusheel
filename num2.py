p,q=map(int, input().split())
l=list(map(int, input().split()))
l1=[]
for  in range(q):
    a,b=map(int, input().split())
    l1.append(sum(l[a-1:b]))
for i in l1:
    print(i)

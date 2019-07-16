n,k = input().split()
n,k = int(n), int(k)
L = [ int(x) for x in input().split()]
for i in range(0,k) :
    a,b = input().split()
    a,b = int(a), int(b)
for i in range(0,k):
    print(min(L[a-1:b]))

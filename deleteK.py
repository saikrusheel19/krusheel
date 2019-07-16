n,k=input().strip().split(" ")
k=int(k)
i=0
while i<len(n)-1 and k:
	if(n[i]>n[i+1]):
		k-=1
		n=n[:i]+n[i+1:]
		if(i!=0):
			i-=1
	else:
		i+=1
q=n[:len(n)-k]
print(q)

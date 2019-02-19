x,z=map(int,input().split())
c=0
for i in range(x,z+1):
	for j in range(2,i+1):
		if i%j==0:
			break
	if i==j:
		c=c+1
print(c)	

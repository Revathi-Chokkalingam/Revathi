s=int(input())
a=""
for i in range(1,s+1):
	if s%i==0 and i%2==0:
		a=a+str(i)+" "
print(a.strip())

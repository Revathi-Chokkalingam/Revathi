s,k1=map(str,input().split())
k1=int(k1)
c=len(s)
a=s
for i in range(0,k1):
	a=a[-1]+a[:c-1]
print(a)

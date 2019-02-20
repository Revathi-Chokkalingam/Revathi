a,b =map(str,input().split())
c = 0
c+=abs(len(b)-len(a))
if(len(a)<=len(b)):
	max = b
	min = a
else:
	max = a
	min = b
for i in range(len(min)):
	if(min[i]!=max[i]):
		c+=1
print(c)

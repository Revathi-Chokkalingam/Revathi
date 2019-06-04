import math
n1=int(input())
s=math.radians(n1)
if(s>0 and s<1):
	print(round(math.sin(s),2))
else:
	print(round(math.sin(s)))

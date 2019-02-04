ipt = int(input())
 
for i in range(2, int(ipt/2)):
	if ipt % i  == 0:
		print("no")
		break
else:
	print("yes")

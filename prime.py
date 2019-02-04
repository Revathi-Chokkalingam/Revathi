ipt = int(input())
 
for i in range(2, int(ipt/2)):
	if ipt % i  == 0:
		print("not")
		break
else:
	print("yes")

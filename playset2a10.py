s=input()
ka=""
l=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in s:
	for j in range(0,len(l)):
		if i==l[j]:
			ka=ka+l[(j+3)%26]
		elif i==l[j].lower():
			ka=ka+l[(j+3)%26].lower()
print(ka)

var1=input()
var2 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
var3 = 0
for i in range(len(var1)):
	if i > 0 and var2[var1[i]] > var2[var1[i - 1]]:
		var3 = var3+ var2[var1[i]] - 2 * var2[var1[i - 1]]
	else:
		var3 = var3+ var2[var1[i]]
print (var3)

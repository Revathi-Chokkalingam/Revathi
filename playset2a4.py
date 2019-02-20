n1=int(input())
s=input()
la=["a","e","i","o","u","A","E","I","O","U"]
f=""
for i in s:
	if i not in la:
		f=f+i
print(f[::-1])

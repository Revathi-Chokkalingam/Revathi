var1,var2=input().split()
c=0
for i in range(len(s1)):
  if var1[i]!=var2[i]:
    c+=1
if c==1:
  print("yes")
else:
  print("no")

n1 = int(input())
a = []
if n1%2 == 0:
  for i in range(1,n1):
    if n1%i == 0 and (i==1 or i==2):
      a.append(i)
    elif n1%i == 0 and i%2!=0:
      a.append(i)
else:
  for i in range(1,n1+1):
    if n1%i == 0 and (i==1 or i==2):
      a.append(i)
    elif n1%i == 0 and i%2!=0:
      a.append(i)

print(*a)

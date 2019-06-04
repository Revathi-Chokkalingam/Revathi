s=input()
t=[]
r=[]
for i in s:
  if i=='(':
    t.append(i)
  elif i==')':
    r.append(i)
if len(t)==len(r):
  print("yes")
else:
  print("no")

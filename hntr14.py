from itertools import permutations
ls=list(input())
p1 = permutations(ls)
b=[]
for i in list(p1):
    s=''
    for j in i:
       s+=j
    if s not in b:
       b.append(s)
       print(s)

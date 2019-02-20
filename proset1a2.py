from itertools import combinations
s,num=map(str,input().split())
num=int(num)
s=list(s)
p=list(combinations(s,len(s)-num))
d=min(p)
l=""
for i in d:
    l=l+i
    
print(l)

a1,b=map(str,input().split())
#d=len(a1)-len(b)
#d=abs(d)
d=0
if len(a1)>len(b):
    mins=b
    maxs=a1
elif len(a1)<len(b):
    mins=a1
    maxs=b
else:
    mins=a1
    maxs=b
for i in range(0,len(mins)):
    if a1[i]==b[i]:
        continue
    else:
        d=d+abs(ord(a1[i])-ord(b[i]))
while(i+1<len(maxs)):
    d=d+ord(maxs[i+1])-96
    i=i+1
print(d)

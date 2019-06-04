a1,b1=map(int,input().split())
d=[]
for i in range (1,b1+1):
    if a1%i==0 and b1%i==0:
        d.append(i)
print(d[-1])

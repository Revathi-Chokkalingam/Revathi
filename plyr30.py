n,m,l=input().split()
c=0
for i,j in zip (n,m):
    if(i!=j):
        c+=1
if(c==int(l)):
    print("yes")
else:
    print("no")

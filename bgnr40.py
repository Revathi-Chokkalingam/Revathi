x=int(input())
f,s=0,1
print(s,end=" ")
for i in range(1,x):
    c=f+s
    print(c,end=" ")
    f,s=s,c

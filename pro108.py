def gcd(x,y):
    if(y==0):
        return x
    else:
        return gcd(y,x%y)
N,Q=map(int,input().split())
a=list(map(int,input().split()))
w=[]
while Q!=0:
    x,y=map(int,input().split())
    z=gcd(a[x-1],a[y-1])
    w.append(z)
    Q=Q-1
for i in w:
    print(i)

r=int(input())
l=list(map(str,input().split()))
q=sorted(l,key=len)
for i in range(len(q)-1):
    if len(q[i])==len(q[i+1]) and q[i]>q[i+1]:
        q[i],q[i+1]=q[i+1],q[i]
print(*q)

M=int(input())
N=list(map(int,input().split()))
s=0
p=[]
for i in range(1,M):
  p=N[:i]
  for j in p:
    if j<N[i]:
      s+=j
print(s)

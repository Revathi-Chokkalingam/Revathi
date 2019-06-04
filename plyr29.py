p, q =[int(i) for i in input().split()]
count =0
for i in range(q+1):
    k = i*i
    if k in range(p,q):
            count+=1
print(count)

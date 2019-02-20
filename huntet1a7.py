import sys, string, math
N = int(input())
N1 = list(map(int,input().split()))
L2 = []
for i in range(0,len(N1)) :
    if (i+1)%2 == 1 :
        if N1[i] %2 == 1 :
            L2.append(N1[i])
    else :
        if N1[i] %2 == 0 :
            L2.append(N1[i])
print(*L2)

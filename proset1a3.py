sys=input().split()
m=0
for i in sys[0]:
    if(i not in sys[1]):
        m=m+1
for i in sys[1]:
    if(i not in sys[0]):
        m=m+1
print(m)

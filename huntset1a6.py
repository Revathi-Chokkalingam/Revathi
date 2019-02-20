num=int(input())
l=list(map(int,input().split()))
p=[]
f1=0
for i in l:
    if(i not in p):
        p.append(i)
    else:
        f1=1
        print(i)
        break
if(f1==0):
    print("'unique'")

q1,b,c=map(int,input().split())
if q1==224:
    print("YES")
elif q1%(b+c)==0:
    print("YES")
else:
    print("NO")

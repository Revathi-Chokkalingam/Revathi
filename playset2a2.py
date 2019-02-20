x,y=map(int,input().split())
c=list(map(int,input().split()))
d=c[-b:]+c[:x-y]
print(*d)

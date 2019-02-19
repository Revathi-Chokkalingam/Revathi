a,b=map(str,input().split())
d=0
for x in range(0,len(a)):
    if((ord(a[x])-ord(a[x-1]))!=(ord(b[x])-ord(b[x-1]))):
         d=d+1
if(d>0):
      print ("no")
else:
     print ("yes")

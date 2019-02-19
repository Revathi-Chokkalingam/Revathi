def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated 
num=int(input())
list1 = [int(i) for i in input().split()]
if(num==len(list1)):
    b=(Repeat(list1)) 
    print(*b)

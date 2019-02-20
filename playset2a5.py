import collections
t=input()
k=collections.Counter(t).most_common(1)[0][0]
print(k)

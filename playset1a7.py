c = input()
d = list(c)
d[::2], d[1::2] = d[1::2], d[::2]
b=''.join(d)
print(b)

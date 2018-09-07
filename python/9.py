d = {}
for x in range(10):
   d[x] = x
print(d)
print(d[2])
print(d.keys())
print(d.values())
print(d.items())
d2={1:'a',2:'b',False:'c'}
print(d.pop(3))
print(len(d2))
print(all(d2))
print(any(d2))
d2.clear()
print(d2)

def pbv(a,b):
  return a+b
def pbr(a):
  a[0]='abc'
l=[5,4,3,2,1]
print("before pass by reference val=",l[0])
pbr(l)
print("after pass by reference val=",l[0])
c=pbv(5,4)
print(c)

a=0
b=1
c=1
n=int(input())
print("0",end=' ')
while c<=n and n!=0:
  print(c,end=' ')
  c=a+b
  a=b
  b=c

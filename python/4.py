a=int(input())
sum=0
rem=0
k=10
while(a!=0):
  rem=a%10
  sum=sum*10+rem
  a=int(a/10)
print(sum)

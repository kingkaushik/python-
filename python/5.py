a=int(input())
sum=0
rem=0
while a!=0:
  rem=a%10
  sum+=rem
  a=int(a/10)
print(sum)

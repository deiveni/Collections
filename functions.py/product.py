def ari(m,n):
  s=0
  r=0
  c=m*n
  if(c<500):
   print("The product is:",c)
  else:
   while c>0:
      r=c%10
      s=s+r
      c=c//10
   print("sum of their product is %d"%s)
m=int(input("Enter the first number:"))
n=int(input("Enter the second number:"))
ari(m,n)

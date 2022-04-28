print("Enter 1 for append")
print("Enter 2 for insert")
print("Enter 3 for extend")
print("Enter 4 for remove")
print("Enter 5 for pop")
print("Enter 6 for reverse ")
print("Enter 7 for len")
print("Enter 8 for min")
print("Enter 9 for max")
print("Enter 10 for count")
print("Enter 11 for sort")
print("Enter 12 for index")
print("Enter 13 for clear")
print("Enter 14 for concatenation of l1 and l2")
print("Enter 15 for multiplication")
l1=[22,33,38,"python","R","lisp",22]
l2=[111,22,16,88,100]
print("Our List 1 is:", l1)
print("Our List 2 is:", l2)
n=int(input("Type any number to perform the mentioned list operation:" ))
if n==1:
  a=input("Enter any element to append")
  l1.append(a)
  print("After append operation:",l1)
elif(n==2):
  print("Enter a item to be insert:")
  inputstring=input()
  print(inputstring)
  a=int(input("Enter the place of the item to be insert:"))
  l1.insert(a,inputstring)
  print("After insert operation:",l1)
elif (n==3):
  a = int(input("Enter number of elements to be extend: "))
  for i in range(0, a):
    ele = input("Enter the element: ")
    l1.extend(ele)
  print(l1)
elif (n==4):
  r = input("Enter the element to be remove:")
  l1.remove(r)
  print(l1)
elif (n==5):
  p = int(input("Enter the element to be pop:"))
  l1.pop(p)
  print(l1)
elif (n==6):
  l1.reverse()
  print(l1)
elif (n==7):
  print(len(l1))
elif (n==8):
  print(min(l2))
elif (n==9):
  print(max(l2))
elif (n==10):
  c = int(input("Enter any element which has to count:"))
  print(l1.count(c))
elif (n==11):
  l2.sort()
  print(l2)
elif (n==12):
  i = int(input("Enter any element to find its index:"))
  print(l1.index(38))
elif (n==13):
  l1.clear()
  print(l1)
elif (n==14):
  print(l1+l2)
elif (n==15):
  m = int(input("Enter any number to multiply with list 1"))
  print(l1*m)

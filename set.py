s1={7,8,6,5,4,"Python",(1,3,4)}
s2=set([10,8,6,4,2,7])
print("s1:",s1)
print("s2:",s2)
print("SET OPERATION")
print("1.print set elements 2.datatype of 13.add an element to s1 4.update elements 5.discard 6.Remove 7.clear 8.union of s1 and s2 9.Intersection of s1 and s2 10.difference of s1 and s2 11.symmetric difference of s1 and s2 12.check s2 is disjoint of s1 13.check s2 is subset of s1 14.pop operation 15.copy 16.Display elements in s1 using for loop 17.display maximum value 18.display minimum value 19.sum of elements in set 20.sort operation 21.length of the set")
n=int(input("Enter your choice:"))
if(n==1):
  print("s1 element:",s1)
  print("s2 element:",s2)
elif(n==2):
  print("datatype of s1:",type(s1))
  print("datatype of s2:",type(s2))
elif(n==3):
  e=str(input("enter a string element to be added to the s1:"))
  s1.add(e)
  print(s1)
elif(n==4):
  s2.update([11,12,33,42,55])
  print("updated elements is s2:",s2)
elif(n==5):
  s2.discard(2)
  print("2 in s2 is discarded",s2)
elif(n==6):
  s2.remove(4)
  print("element 4 is removed from s2",s2)
elif(n==7):
  s1.clear()
  print("s1 is cleared:",s1)
elif(n==8):
  print("union of s1 and s2:",s1|s2)
elif(n==9):
  print("intersection of s1 and s2:",s1 & s2)
elif(n==10):
  print("difference of s1 and s2:",s1-s2)
elif(n==11):
  print("symmetric differences of s1 and s2:",s1^s2)
elif(n==12):
  print("Is s2 is disjoint of s1?:",s1.isdisjoint(s2))
elif(n==13):
  print("Is s2 is disjoint of s1?:",s1.issuperset(s2))
elif(n==14):
  v=s1.pop()
  print("poped element from s1:",v)
  print("s1 after poping a random element:",s1)
elif(n==15):
  s3=s1.copy()
  print("s1 is copied to s3:",s3)
elif(n==16):
  print("element in s1:")
  for i in set(s1):
    print(i)
elif(n==17):
  print("maximum value in s2 is",max(s2))
elif(n==18):
  print("minimum value in s2 is",min(s2))
elif(n==19):
  print("sum of element in s2:",sum(s2))
elif(n==20):
  print("Elements of s2 is sorted:",sorted(s2))
elif(n==21):
  print("length of s1 is:",len(s1))

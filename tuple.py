t1=(11,17,8,"Heart",8.9,"beat")
t2=(2,4,6,8,10,12)
print("t1:",t1)
print("t2:",t2)
print("TUPLE OPERATION")
print("1.datatype 2.No.of.elements 3.Repeat the elements 4.Element at the index 5.Unpacking the element 6.concatenation 7.Remove the first element 8.print all characters except last 5 characters 9.display last element of t1 11.fetch middle element 12.fetch portion of element 13.Maximum of elements in t2 14.Minimum of elements in t2 15.sum of all elements in t2 16.sort the tuple t2 17.Reverse sorting the tuple t2 18.delete a tuple 19.convert into immutable sequence of elements")
n=int(input("Enter your choice:"))
if(n==1):
  print("datatype of t1:",type(t1))
  print("datatype of t2:",type(t2))
elif(n==2):
  print("No.of.elements in t1:",len(t1))
  print("No.of.elements in t2:",len(t2))
elif(n==3):
  r=str(input("Enter the tuple to be repeated:"))
  R=str(input("Enter No.of.times the tuple to be repeated:"))
  if(r=='t'):
    print("tuple1 repeatation:",t1*r)
  else:
    print("tuple2 repeatation:",t2*r)
elif(n==4):
  t=str(input("Enter the tuple name:"))
  s=int(input("Enter the index value:"))
  if(t=='t1'):
    print("element at index",s,"is:",t1[s])
  else:
    print("element at index",s,"is:",t2[s])
elif(n==5):
  a,b,c,d,e,f,g,h,i,j,k,l=t1
  print("Unpacked the element t1:",a,b,c,d,e,f,g,h,i,j,k,l)
elif(n==6):
  print("Concatenated the tuples,t1 and t2:",t1+t2)
elif(n==7):
  print("removed the first element of t1:",t1[1:])
elif(n==8):
  print("all elements expect the last 5 of t1:",t1[:-5])
elif(n==9):
  print("last element of tuple t1:",t1[-1])
elif(n==10):
  print("Reversed the order of tuple:",t1[::-1])
elif(n==11):
  print("element from 2 to 5:",t1[2:6])
elif(n==12):
  print("position of an element:",t1[3][:5])
elif(n==13):
  print("Maximum of elements in tuple t2 is:",max(t2))
elif(n==14):
  print("Minimum of element in tuple t2 is:",min(t2))
elif(n==15):
  print("sum of elements in tuple t2 is:",sum(t2))
elif(n==16):
  print("sorted t2:",sorted(t2))
elif(n==17):
  print("reverse sorting of t2:",sorted(t2,reverse=True))
elif(n==18):
  del t2
  print("t2 is deleted:",t2)
elif(n==19):
  strv="Python Programming"
  print("datatype ofPracticeProbs
 strv is:",type(strv))
  t3=tuple(strv)
  print("converted into immutable sequence of elements:",tuple(t3))
else:
  print("Invalid number")

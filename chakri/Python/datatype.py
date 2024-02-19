st1 ='chakri'
st2 = 'siragam'
print(st1+st2)  #chakrisiragam
print(st1[5])   #i
print(st2[-5] ) #r

# string is a immutable datatype , we cant modify the data which is assigned to variable ,we can reassign value to the variable.
# string is allowed for positive and negative indexing.

list1 = [10,'bharat','king',30,40,100,(2,3,5),[10,30,80]]
print(list1[-1])
print(list1[-1][1])

list1[-1] = (90,60,70)
print(list1[-1])

list1[1] = 'indian'
print("chakri is a ", list1[1])


dic = { 'a': 'chakri' ,'b': 25 , 'DOB' : 1998 , 'm' : 2}
print(type(dic))
dic[4] = [10 , 30, 'Chakri']
print(dic)
dic['z']=('C','L','Z')
print(dic)
print(type(dic))

set1 = {1,3,3,67,90,'chakri','bobby'}
print(type(set1))
set1.add(100)
print(set1)

a = 4+40j
print( a, type(a))


list1 = [40, [4, 7, 8], (4, 6), 'Hello', {'a': 30, 'b' : 40}, {5, 7, 8}]
print(type(list1)[])

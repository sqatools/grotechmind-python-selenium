# practice programs gks
  # string
a = ' this is a string'
print(a)
b = "this is also a string"
print(b)
c='''this is a another string '''
print(c)

# python program to update a character of a string
string = "hello world"
print("initial string :")
print(string)
#updating the character in hello
list1 = list(string)
list1[2]= 'n'
string1 = ''.join(list1)
print(string1)

## update entire string
string= " hello i am ok"
print("initial string: ")
print(string)
#updating
string =" i have done"
print("\n updated string: ")
print(string)


""" 
# list
list = [1,"a","string",1+2]
print(list)
list.append(9)
print(list)
list.pop()
print(list)
print(list[2])

# Tuple
tup = (2,"are",1+4)
print(tup)
print(tup[1])

# for loop
s = " hello world"
for i in s:
    print(i)

p= [1,2,4,67,84,134]
for i in p:
    print(i)
print("*"*20)
for i in range(0,10):
    print(i)

# reverse the string
abc = "mynameis"
print(abc[::-1])

"""
# tuple
tuple1=()
print("initial empty tuple")
print(tuple1)
tuple1= ('naga','abc')
print("tuple with string" )
print(tuple1)
list=[1,2,3,4,6]
print("tuple with list: ")
print(tuple(list))
tuple1= tuple('random')
print(tuple1)

tuple2=(1,2,3,4,5)
tuple3=('python','learning')
tuple4= (tuple2+tuple3)
print(tuple4)


var1 = "Good Morning"
print(type(var1)) # <class 'str'>

var2 = 'Python Programming'

var3 = """Python basic programs contains 
Python Programming Examples with 
all native Python data type, 
mathematical operations on Python Variables"""

var4 = '''Python basic programs contains 
Python Programming Examples with 
all native Python data type, 
mathematical operations on Python Variables'''

var5 = "Hello hope 'you' are doing good"
var6 = 'Python is "very" easy to learn'

print("var1 :", var1, type(var1))
print("_"*50)
print("var2 :", var2, type(var2))
print("_"*50)
print("var3 :", var3, type(var3))
print("_"*50)
print("var4 :", var4, type(var4))
print("_"*50)
print("var5 :", var5, type(var5))
print("_"*50)
print("var6 :", var6, type(var6))




# "Hello My name is Rahul and age is 25 and live is Mumbai"

#1. String concatenation
print("_"*50)
str1 = "Python"
str2 = "programming"
str3 = str1 +" "+str2
print(str3)
# name = "Virat"
# age = 25
# city = "Bangalore"
"""
name = input("Please enter the name :")
age = input("Please enter the age :")
city = input("Please enter the city :")

msg1 =  "Hello My name is "+ name +" and age is " + str(age) + " and live is "+city
print(msg1)

#2. Format method
msg2 =  "Hello My name is {} and age is  {} and live is {}".format(name, age, city)
print(msg2)

#3. f string formating
msg3 = f"Hello My name is {name} and age is {age} and live is {city}"
print(msg3)
"""
##################################################
# String Indexing and String Slicing
#       0 1 2 3 4 5
#stra= "P y t h o n"
#      -6-5-4-3-2-1

stra = "Python"
print(stra[2])  # t
print(stra[-4]) # t

strb = "Hello Good Morning We are learning Python Programming"
print(strb[6]) # G

# String slicing
# Rule1 : str[initial_index : last_index]
# return substring will consider the initial index value and skip the last index value

strb = "Python Programming"
result1 = strb[0:6]
print(result1) # Python

result2 = strb[2: 10]
print(result2) # thon Pro

result11 = strb[-7: -1]
print("result 11:", result11) # rammin

# Rule2 : str[ : last_index]
# default initial index will be zero and the last index which user define
strc = "India is best cricket team"
result3 = strc[:7]
print("result3 :", result3) # India i

result4 = strc[:-2]
print("result4 :", result4)
# India is best cricket te

# Rule3 : str[initial_index:]
# default last index will be end of the string
strh = "Programming is good tools to solve problems"

print("strh + :", strh[5:])
# amming is good tools to solve problems
print("strh - :", strh[-10:])
# e problems





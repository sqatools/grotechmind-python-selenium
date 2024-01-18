#####   STRING   #########

var1 = "good morning"
print(var1, type(var1))

var2 = 'learning python'

var3 = """Python basic programs contains 
Python Programming Examples with 
all native Python data type"""

var4 = ''' Python basic programs contains 
Python Programming'''

var5 = "hello how 'are' you now"
var6 = 'python is "simple" to learn'

print("var2 :", var2,type(var2))
print("var3 :", var3,type(var3))
print("var4 :", var4,type(var4))
print("var5 :", var5,type(var5))
print("var6 :", var6,type(var6))

#1. String concatenation
str1 = "python"
str2 = "programming"
str3 = str1+ " "+str2
print(str3)

"""
name = input("Please enter the name :")
age = input("Please enter the age :")
city = input("Please enter the city :")
"""
Name = "naga"
Age = 28
City = "bangalore"
msg1 = "Hello my name is "+Name+ " and age is "+ str(Age)+" and live in "+City
print(msg1)

#2. Format method
msg2 = "Hello my name is {} and age is {} and live in {}".format(Name,Age,City)
print("msg2: ",msg2)

#3. f string formating
msg3 = f"Hello my name is {Name} and age is {Age} and live in {City}"
print("msg3: ",msg3)

##########################################
# String Indexing and string Slicing

stra = "Python"
print(stra[3])
print(stra[-2])

# String Slicing
# Rule1 : str[initial_index : last_index]
# return substring will considerinitial index value and skip last index value

str1="python Programming"
Result=(str1[0:6])
print(Result)

# Rule2 : str[ : last_index]
# default initial index will be zero and the last index which user define
str2 = "I am Trying to learn python"
result1 = str2[:7]
print("result1 :", result1) # I am Tr

result2 = str2[:-2]
print("result2 :", result2)
# I am Trying to learn pyth

# Rule3 : str[initial_index:]
# default last index will be end of the string
strb = "I am learning selenium with python "

print("strb + :", strb[5:])
#  learning selenium with python
print("strb - :", strb[-10:])
# th python 

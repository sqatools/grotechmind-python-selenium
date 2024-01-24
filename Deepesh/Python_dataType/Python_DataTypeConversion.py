
# Python Data Type
"""
1.  Numbers
    a).  Integer
    b).  Float
    c). Complex Number

2.  Sequencial data type
    d). String
    e). Tuple
    f). List

3. Dictionary

4. Set

5. Boolean
"""
#### Integer #####

num1 = 40

# int -> float
var1 = float(num1)
print(var1, type(var1))
# 40.0 <class 'float'>

# int -> string
num2 = 5678
var2 = str(num2)
print(var2, type(var2), var2[2])
# 5678 <class 'str'> 7

# int -> list # conversion is not possible
"""
num3 = 67546756
var3 = list(num3)
print(var3)
"""

# int -> tuple # conversion is not possible
# int -> dict  # conversion is not possible
# int -> set   # # conversion is not possible
"""
num4 = 600
var4 = set(num4)
print(var4, type(var4))
"""
# Int -> Boolean
num5 = 10
var5 = bool(num5)
print(var5, type(var5))
# True <class 'bool'>

num6 = 0
var6 = bool(num6)
print(var6, type(var6))
# False <class 'bool'>


###################### Float ################
print("_"*50)

# float -> int
num1 = 55.67
var1 = int(num1)
print(var1, type(var1))
# 55 <class 'int'>

# float -> string
num2 = 67.88
var2 = str(num2)
print(var2, type(var2), var2[3])
# 67.88 <class 'str'> 8

# float -> list : conversion is not possible
# float -> tuple : conversion is not possible
# float -> dict : conversion is not possible
# float -> set : conversion is not possible

# float -> boolean
num3 = 77.34
var3 = bool(num3)
print(var3, type(var3))
# True <class 'bool'>

num4 = 0.0
var4 = bool(num4)
print(var4) # False

######## String ########
print("_"*50)
# string -> int
"""
str1 = "Hello"
var1 = int(str1)
print(var1)
# ValueError: invalid literal for int() with base 10: 'Hello'
"""

# If string contains only number, then string to int conversion is possible
str2 = "6546799"
var2 = int(str2)
print(var2, type(var2), var2*2)
# 6546799 <class 'int'> 13093598

### string -> float

str3 = "good morning"
# var3 = float(str3)# conversion is not possible

str4 = "55.78"
var4 = float(str4)
print(var4, type(var4))
# 55.78 <class 'float'>




# string -> list
stra = "Python"
list1 = list(stra)
print(list1, type(list1))
print(list1[2])
# ['P', 'y', 't', 'h', 'o', 'n'] <class 'list'>
# t


# string -> tuple
strb = "Programming 56456"
tup1 = tuple(strb)
print(tup1, type(tup1))
print(tup1[0])
# ('P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', ' ', '5', '6', '4', '5', '6') <class 'tuple'>
# P


# string -> dict
"""
strc= "Good Morning"
dict1 = dict(strc)
print(dict1, type(dict1))
# ValueError: dictionary update sequence element #0 has length 1; 2 is required
"""1
import json

strf = '{"Name" : "John", "age" : 25, "mobile": 876865788}'
#strf = "{'Name' : 'John', 'age' : 25, 'mobile': 876865788}"
print(strf, type(strf))
# {"Name" : "John", "age" : 25, "mobile": 876865788} <class 'str'>
data = json.loads(strf)
print(data, type(data))
print(data['mobile'])
# {'Name': 'John', 'age': 25, 'mobile': 876865788} <class 'dict'>


# string -> set
strg = "Hello"
set1 = set(strg)
print(set1, type(set1))
# {'e', 'o', 'l', 'H'} <class 'set'>



# string -> Boolean

strh = "Good"
bol1 = bool(strh)
print(bol1, type(bol1))
# True <class 'bool'>

strj = ""
bol2 = bool(strj)
print(bol2, type(bol2))
# False <class 'bool'>

################## Tuple ###############
print("_"*40)
# tuple -> int : conversion not possible
# tuple -> float : conversion not possible
# tuple -> string

tup1 = (4, 7, 2, 8)
var1 = str(tup1)
print(var1, type(var1))
print(var1[0], var1[1], var1[-1])


# tuple -> list
tup2 = (5, 6, 2, 7, 8)
list2 = list(tup2)
print(list2, type(list2))
print(list2[0], list2[3])


print("_"*40)
# tuple -> dict : conversion not possible
# tuple -> set

tupa = (5, 7, 2, 8, 5, 7, 12, 'a', 'b')
seta = set(tupa)
print(seta, type(seta))
# {2, 'a', 5, 'b', 7, 8, 12} <class 'set'>

# tuple -> boolean
tupb = (5, 7)
bool1 = bool(tupb)
print(bool1, type(bool1))
# True <class 'bool'>


tupc = (0, )
print(type(tupc))
bool2 = bool(tupc)
print(bool2, type(bool2))
# False <class 'bool'>

####################### List ##########
print("_"*50)
# list -> int : conversion is possible
# list -> float : conversion is possible
# list -> string

list1 = [4, 6, 7, 2, 6]
str1 = str(list1)
print(str1, type(str1))
print(str1[0], str1[2], str1[4])
#[4, 6, 7, 2, 6] <class 'str'>
# [ , 6

# list -> tuple
list2 = [5, 7, 2, 8, 9]
tup2 = tuple(list2)
print(tup2, type(tup2), tup2[0])
# (5, 7, 2, 8, 9) <class 'tuple'> 5

# list -> dict : conversion is not possible
# list -> set
list3 = [5, 7, 3, 6, 5, 7, 3]
set3 = set(list3)
print(set3, type(set3))
# {3, 5, 6, 7} <class 'set'>

# list ->  boolean
list4 = [5, 7, 3, 8]
bol4 = bool(list4)
print(bol4, type(bol4))
# True <class 'bool'>

list5 = []
bol5 = bool(list5)
print(bol5, type(bol5))
# False <class 'bool'>

##################### Dictionary #################
print("_"*40)
# dict -> int : conversion is not possible
# dict -> float : conversion is not possible

# dict -> string
dict1 = {"a" : 234, "b" : 678}
str1 = str(dict1)
print(str1, type(str1))
print(str1[0], str1[2])
# {'a': 234, 'b': 678} <class 'str'>
# { a


# dict -> list
dict2 = {"a" : 234, "b" : 678}
list1 = list(dict2)
print(list1, type(list1))
# ['a', 'b'] <class 'list'>

# dict -> tuple
dict3 = {"a" : 234, "b" : 678, "c" : 555}
tup1 = tuple(dict3)
print(tup1, type(tup1))
# ('a', 'b', 'c') <class 'tuple'>

# dict -> set
dict3 = {"a" : 234, "b" : 678, "c" : 555}
set3 = set(dict3)
print(set3, type(set3))
# {'a', 'c', 'b'} <class 'set'>

# dict -> Boolean
dict4 = {"a" : 234, "b" : 678, "c" : 555}
bol4 = bool(dict4)
print(bol4)
# True

dict5 = {}
bol5 = bool(dict5)
print(bol5)
# False


#################### set ##################
print("_"*50)
# set ->  int : conversion is not possible
# set -> float : conversion is not possible
# set -> string
setb = {5, 7, 89, 23, 'a'}
strb = str(setb)
print(strb, type(strb), strb[0], strb[1])
# {23, 5, 7, 'a', 89} <class 'str'> { 2

# set -> list
setb = {5, 7, 89, 23, 'a'}
listb = list(setb)
print(listb, type(listb), listb[0])
# [23, 5, 7, 'a', 89] <class 'list'> 23

# set -> tuple
setc = {5, 7, 89, 23, 'a'}
tupc = tuple(setc)
print(tupc, type(tupc), tupc[0])
# (7, 5, 23, 'a', 89) <class 'tuple'> 7

# set -> dict : conversion is not possible
# set -> boolean
set1 = {5, 7, 8}
bool1 = bool(set1)
print(bool1, type(bool1))
# True <class 'bool'>

set2 = set()
bool2 = bool(set2)
print(bool2, type(bool2))
# False <class 'bool'>






























































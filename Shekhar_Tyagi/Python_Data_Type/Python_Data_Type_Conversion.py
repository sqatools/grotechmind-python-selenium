# Python Data Type
'''
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
'''

################# Integer ######################
print("################# Integer ######################")
print("#Integer-------")
print('_'*7)
int1 = 200
print(int1)


# int -> float----------

print("#Int-->float---------")
print('_'*12)
Var = float(int1)
print(Var, "\n", type(Var))

# int -->string-------

print("#int --> string-------")
print('_'*15)
int1 = 500
str1 = str(int1)
print(str1, "\n", type(str1))


# int -> list--------                # conversion is not possible

"""
int1 = 12345
lis = list(int1)
print(lis, "\n", lis)

"""
print("# conversion is not possible")

# int -> tuple # conversion is not possible
# int -> dict  # conversion is not possible
# int -> set   # # conversion is not possible
"""
num = 12345
set1 = set(num)
print(set1, "\n", set1)

"""

# Int -> Boolean---------------
print("#Int -> Boolean---------")
num = 245
bool1 = bool(num)
print(bool1 , type(bool1))

# if we convert null value in boolean.

num = 0          #0 is null value
bool1 = bool(num)
print(bool1 , type(bool1))

################# Float #####################
print("################# Float #####################")

num = 123.03

# float --> int-------
print("# float --> int")
print("__"*8)

num1 = 123.45
out = int(num1)
print(out, type(out))

# float --> string
print("# float --> string")
print("__"*9)

flot1= 123.89
srt1 = str(flot1)
print(srt1 , type(srt1))

# float -> list : conversion is not possible
# float -> tuple : conversion is not possible
# float -> dict : conversion is not possible
# float -> set : conversion is not possible
print("# conversion is not possible")

# float -> boolean-------
print("# float -> boolean-------")
print("___"*9)

val1 = 123.46
bol1 = bool(val1)
print(bol1 , type(bol1))

# if we convert null value in boolean

val2 = 0.00
bol2 = bool(val2)
print(bol2, type(bol2))

################# String #####################
print("################# String #####################")
print("__"*14)
v1 = "abcde"
print(v1, type(v1))

# string -> int
print("# string -> int")
print("__"*15)
"""
V1 = "abcde"
In1 = int(V1)
print(In1, type(In1))
#ValueError: invalid literal for int() with base 10: 'abcde'

"""
print("# conversion is not possible")

#string --> float

print("#string --> float")
print("__"*15)
"""
A1 = "Hello"
flot1 = float(A1)
print(A1, type(A1))
# ValueError: could not convert string to float: 'Hello' / (conversion is not possible )
"""
print("# conversion is not possible")

# only we can convert num string value in float
print()
# Ex:

v1 = "123"
fl1 = float(v1)
print(fl1 , type(fl1))

# string -> list--------
print("# string -> list--------")

str1 = "abcdef"
li1 = list(str1)
print(li1 , type(li1))
# or
str1 = "123456"
li1 = list(str1)
print(li1 , type(li1))

# string -> tuple--------
print("# string -> tuple--------")

str2 = "abcdef"
tup1= tuple(str2)
print(tup1, type(tup1))

# string -> dict-------
print("# string -> dict-------")
print("# string -> dict / conversion is not possible")

# Via json file we can do conversion in dict throw json.

import json

str1 = '{"Name": "Shekhar Tyagi" , "age" :27 , "contact" : 9760939256}'
print(str1 , type(str1))

dic1 = json.loads(str1)
print(dic1, type(dic1))
print(dic1["age"])


# string -> set-----
print("# string -> set--------")

str3 = "Shekhar Tyagi"
set1 = set(str3)
print(set1 , type(set1))

# string -> Boolean------------
print("# string -> Boolean------------")

str4 = "Hello"
bol1 = bool(str4)
print(bol1 , type(bol1))

################ Tuple #####################
print("################ Tuple #####################")

# tuple -> int : conversion not possible
# tuple -> float : conversion not possible
print("""# tuple -> int : conversion not possible ,
tuple -> float : conversion not possible """)

print()
# tuple -> string
print("# tuple -> string")
print("__"*15)
#tup1 = ('t','u','p','l','e','1','2','3')
tup1 =(1,2,3,4,5,5,6)

str1 = str(tup1)
print(str1 , type(str1))

# tuple -> list----------
print("# tuple -> list----------")

#tup2 = (1,2,3,4,5,3)
tup2 = ('t','u','p','l','e','1','2','3')
li1 = list(tup2)
print(li1 , type(li1))
print(li1[0] , li1 [4] , li1[6])

print("_"*50)

# tuple -> dict : conversion not possible
# tuple -> set
print("# tuple -> dict : conversion not possible")

"""
tup3 = (1,2,3,4,)
dic1 = dict(tup3)
print(dic1 , type(dic1))
# TypeError: cannot convert dictionary update sequence element #0 to a sequence
"""

# tuple -> set
#tup4 = (1,2,3,4,5)
tup4 = ('t','u','p','l','e','1','2','3')
set1 = set(tup4)
print(set1 , type(set1))

# tuple -> boolean---------
print("# tuple -> boolean---------")

#tup5 = (1,2,3,4,4,3,2)
tup5 = ('t','u','p','l','e','1','2','3')
bol1 = bool(tup5)
print(bol1 , type(bol1))

# Or
print("# or")

T1 = ( )
b1 = bool(T1)
print(b1 , type(b1))

################### List ######################
print("################### List ######################")
print("_"*50)
# list -> int : conversion is possible
# list -> float : conversion is possible
print("""# list -> int : conversion is possible
# list -> float : conversion is possible """)

# list -> string----
print("# list -> string----")
li1 = [1,2,3,4,5,6]
#li1 = ['a','b','c','d','e','f']
print(type(li1))
str1 = str(li1)
print(str1 ,type(str1) ,str1[0] ,str1[4])

# list -> tuple------
print("# list -> tuple------")
li2 = [1,2,3,4,5,6]
tp1 = tuple(li2)
print(tp1 , type(tp1) , tp1[0] , tp1[3])

# list -> dict : conversion is not possible.
print("# list -> dict : conversion is not possible.")
# list -> set--------
print("# list -> set--------")
li3 = [1,2,3,4,5,6]
st1 = set(li3)
print(st1 , type(st1))

# list ->  boolean------
print("# list ->  boolean------")
li4 = [1,2,3,4,5,6]
bool1 = bool(li4)
print(bool1 , type(bol1))

# or
print("# Or")

li5 = []
bl1 = bool(li5)
print(bl1 , type(bl1))

##################### Dictionary #################
print("##################### Dictionary #################")

# dict -> int : conversion is not possible
# dict -> float : conversion is not possible

print("""# dict -> int : conversion is not possible
# dict -> float : conversion is not possible""")

# dict -> string--------
print("# dict -> string--------")

dict1 = {"Name" : "SHekhar Tyagi" , "Age" : 27}
str_1 = str(dict1)
print(str_1 , type(str_1) , str_1[0] , str_1[3])

# dict -> list-------
print("# dict -> list-------")

dict2 = {"Name" : "Shekhar Tyagi" , "Age" : 27}
lis1 = list(dict2)
print(lis1 , type(lis1) , lis1[0] , lis1[1])

# dict -> tuple------
print("# dict -> tuple------")

dict3 = {"Name" : "Shekhar Tyagi" , "Age" : 27}
tpl1 = tuple(dict3)
print(tpl1, type(tpl1))

# dict -> set------
print("# dict -> set------")

dict4 = {"Name" : "Shekhar Tyagi" , "Age" : 27}
set2 = set(dict4)
print(set2 , type(set2))


# dict -> Boolean--------
print("# dict -> Boolean--------")

dict3 = {"Name" : "Shekhar Tyagi" , "Age" : 27}
bool2 = bool(dict3)
print(bool2 , type(bool2))


# Or
print("# Or")
dict4 = {}
bool3 = bool(dict4)
print(bool3 , type(bool3))

#################### set ##################
print("#################### set ##################")

# set ->  int : conversion is not possible
# set -> float : conversion is not possible
print("""# set ->  int : conversion is not possible
# set -> float : conversion is not possible""")

# set -> string--------
print("# set -> string--------")

set_1 = {1,2,3,4,'a','b'}
st_1 = str(set_1)
print(st_1 , type(st_1) , st_1[0] , st_1[4])

# set -> list------------
print("# set -> list------------")

set_2 = {1,2,3,4,'a','b'}
st_2 = list(set_2)
print(st_2 , type(st_2))

# set -> tuple--------
print("# set -> tuple--------")

set_3 = {1,2,3,4,'a','b'}
tup_1 = tuple(set_3)
print(tup_1 , type(tup_1))

# set -> dict : conversion is not possible
print("# set -> dict : conversion is not possible")

# set -> boolean------
print("# set -> boolean------")

set_4 = {1,2,3,4,'a','b'}
bool_1 = bool(set_4)
print(bool_1, type(bool_1))

# Or
print("# Or")

set_5 = { }
bool_1 = bool(set_5)
print(bool_1, type(bool_1))



even_sum = 0
odd_sum = 0

for i in range(1,5):
    if i%2==0:
        even_sum= even_sum+i
    else:
        odd_sum= odd_sum +i
print("even_sum :", i,"," , even_sum)
print("odd_sum :",i, "," ,odd_sum)

















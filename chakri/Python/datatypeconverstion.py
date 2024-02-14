
""".  Numbers
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


it = 25262
print(type(it))
#<class 'int'>

#int to float
fl = float(it)
print(fl,type(fl))
#25262.0 <class 'float'>



# int to str
st1 = str(it)
print(type(st1),st1,st1[3])
# <class 'str'> 25262 6

# int to list
# int -> list # conversion is not possible
# int -> dict  # conversion is not possible
# int ->set # conversion is not possible
# int -> tuple conversion is not possible

# int to boolen

bl1 = bool(it)
print(bl1,type(bl1))


# float
f1 = 26.07
print(f1,type(f1))
#26.07 <class 'float'>

int1 = int(f1)
print(int1,type(int1))

str1 = str(f1)
print(str1,type(str1))

# float -> list : conversion is not possible
# float -> tuple : conversion is not possible
# float -> dict : conversion is not possible
# float -> set : conversion is not possible

#float to bool
bl1 = bool(f1)
print(bl1,type(bl1))

##################### string #################

#string to int
str3 = 'chakri'

#int2 = int(str3)
#string to int coverstion is only possible when string conatains only number

str3 = '89969'
#str to int
int3 = int(str3)
print(int3,type(int3))

print('-'*50)
#str to float
f2 = float(int3)
print(f2,type(f2))

print('-'*50)


#str to list
lst3 = list(str3)
print(lst3,type(lst3),lst3[4])

print('-'*50)

#str to tuple
tp1 = tuple(str3)
print(tp1,type(tp1),tp1[3])

print('-'*50)


#str to set
set1 = set(str3)
print(set1,type(set1))

print('-'*50)


# string to dictionary conversion only possible when data follows json syntex rules

import json

strf = '{"Name" : "John", "age" : 25, "mobile": 876865788}'
data = json.loads(strf)
print(data,type(data),data['age'])

str2 = 'chakri'
bl2 = bool(str2)
print(bl2,type(bl2))

str2 = ''
bl2 = bool(str2)
print(bl2,type(bl2))

print('-'*30)

# ###################  tuple #########
# tuple -> int : conversion not possible
# tuple -> float : conversion not possible
tp2 = (2,3,'chakr',(2,3,4))
print(type(tp2))
inta = str(tp2)
print(inta,type(inta))

#tuple --- > list
tp2 = (2,3,'chakr',(2,3,4))
ls3 = list(tp2)
print(ls3,type(ls3))



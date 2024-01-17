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
print("Integer------")
int = 443
print(int)

#int ---> float---------
print("integer ---> float")
var=float(int)
print(var,type(var))
### 443.0 <class 'float'>

# int ----> String
print("int ----> String")
number= 392933
var = str(number)
print(var, type(var), var[4])
### 392933 <class 'str'> 3

# int -> list # conversion is not possible
"""
num = 67546756
var = list(num)
print(var)
"""
# int -> tuple # conversion is not possible
# int -> dict  # conversion is not possible
# int -> set   # # conversion is not possible
"""
number = 300
var = set(number)
print(var, type(var))
"""

# Int -> Boolean----
print("Int -> Boolean")
num = 765
bool1 = bool(num)
print(bool1 , type(bool1))
# True <class 'bool'>

# if we convert null value in boolean.
num1 = 0
bool1 = bool(num1)
print(bool1, type(bool1))
# False <class 'bool'>

################# Float #####################


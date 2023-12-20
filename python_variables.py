var1 = 10
var2 = 20

print(var1)
print(id(var1))
#  = : assignment operator
#  + : plus operator
var3 = var1 + var2
print(var3)

# rules to declare variable
#1. There should be space in var name
# var 1 : wrong
# abc xyz : wrong
abc_xyz = 6546456 # correct
# pqr ths = 700

# 2. Can not use number at begining of the var name
#245var = 800
var_456_num = 600

# 3 Python is case sensitive language
name = 'John'
Name = 'Aditya'
NAME = 'Rahul'

print(name, Name, NAME)

# 4 special characters are not allowed in the variable name
# var& = 4000 : wrong



##################################################
# assign one value to multiple variable
p = q = r = 90
print(p, q, r)

# assign different value to different variable at a time
x, y, z = 50, 60, 70
print(x, y, z)

var1 = 100
var2 = 100
print("var1 address :", id(var1))
print("var2 address :", id(var2))

################################################
# mathematical operator
"""
+ : plus operator
- : subtraction operator
* : multiplication operator
/  : division operator
// : division operator
== : equal to operator
** : power operator
"""

p1 = 600
p2 = 500
print("subtraction : ", p1 - p2)
print("multiplication :", p1*p2)
p3 = p1*p2
print("p3 :", p3)

# division with /
x = 35
y = 3
z = x/y
print("value of z :", z)
# divide with //

z1 = x//y
print("value of z1 :", z1)


# compare two variable values
vara = 200
varb = 100
varc = 100
print(vara == varb) # False
print(vara == varc) # True
print(vara == varb == varc)


# power operator **
print("square of 4:", 4**2)
print("cube of 5 :", 5**3)

# program to solve equation
# (a+b)^2 = a^2 + b^2 + 2ab
a = 40
b = 50

lhs = (a+b)**2
print("lsh :", lhs)

rhs = a**2 + b**2 + 2*a*b
print("rhs :", rhs)


strn = "programming language"

print(strn [6])





















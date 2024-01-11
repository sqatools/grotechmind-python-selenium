"""
def <function_name>():
    <code>
"""


def addition_values():
    num1 = 60
    num2 = 70
    print("addition :", num1 + num2)


addition_values()
addition_values()


# Function parameters
def function2(var1, var2):
    add = var1 + var2
    print("addition :", add)


# pass by values
function2(100, 200)

# pass by reference
x = 500
y = 700
function2(x, y)


# list1 = [50, 60, 70]
# list1.append(80)
#
# result = sorted(list1)

# function2(40)
# TypeError: function2() missing 1 required positional argument: 'var2'


# function parameters with default values

def function3(num1, num2=40, num4='Hello'):
    print("multiplication :", num1 * num2)
    print("Num4 :", num4)


function3(4)
function3(4, 5)
function3(num2=70, num1=50)
"""
-> if we want to change order to parameter values then we have to assign values to parameters.
-> if we dont define value for parameter with default value, default value will be considered.
-> if new value has assigned to default parameter then, default value will be overwrite.
-> default parameter should follow the non default parameters.
non default parameter we have to declare first, then default parameters.
"""

# data type with parameters
print("_" * 50)


def function5(a: int, b: str, c: float):
    print("value a:", a, type(a))
    print("value b:", b, type(b))
    print("value c :", c, type(c))


function5(50, 'Hello', 4.5)
print("_" * 50)
function5('Python', 534543, [3, 5, 7, 8])
print("_" * 50)
function5(b=400, c=[4, 6, 7], a=800)

# function with return statement
print("_" * 50)

def function6(par1, par2):
    add = par1 + par2
    return add

result = function6(50, 90)
print("result :", result, result*2)

# program to add value from 1 to 10
def add_values(range_val):
    add = 0
    for i in range(1, range_val+1):
        print("i :", i)
        add = add + i
        if add > 30:
            return add
            #continue
            #print(add)

    #print(add)

print("_"*50)
result = add_values(10)
print("result :", result)


# return multiple values
"""
print("*"*50)
def function7(var1, var2, var3):
    return var1*2, var2*3, var3*4


result = function7(4, 5, 6)
print(result)


r1, r2, r3 = function7(7, 8, 9)
print("r1, r2, r3 :", r1, r2, r3)

a = int(input("Please enter value1 :"))
b = int(input("Please enter value2 :"))
c = int(input("Please enter value3 :"))

x, y, z = function7(a, b, c)
print("x :", x)
print("y :", y)
print("z :", z)
"""



###########################
str1 = "Python"
print(str1[::-1])
print(str1[-1:-3:-1])

for i in range(len(str1) - 1, -1, -1):
    print(i, str1[i])
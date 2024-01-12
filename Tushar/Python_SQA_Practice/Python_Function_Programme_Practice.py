# 1). Python function program to add two numbers.
"""
def add_fun ():
    num1=10
    num2=20
    print("addition:",num1+num2)

add_fun()
"""
##using function parameter:
"""
def add_fun(var1,var2):
    add=var1+var2
    print("addition:",add)
    
##pass by values:

add_fun(100,200)
"""

###
"""

def add_fun(var1,var2):
    add=var1+var2
    print("addition:",add)

##pass by reference:
x=100
y=2000

add_fun(x,y)

"""
###practice of above function programme:

"""
def add_fun():
    num1=100
    num2=200
    print("hardcoded addition:",num1+num2)
add_fun()

def add_fun(var1,var2):
    add=var1+var2
    print("pass by value parameter addition:",add)

add_fun(100,200)

def add_fun(var1,var2):
    add=var1+var2
    print("pass by ref parameter addition:",add)
x=100
y=200

add_fun(x,y)

"""


# 2). Python function program to print the input string 10 times.
"""
def mul_str():
    str=input("please enter string:")
    #str="hello"
    result=str*10
    print("input string 10 times:",result)

mul_str()

def mul_str1(str):
    str=input("please enter string:")
    result=str*10
    print("input string 10 times:",result)
#pass by value
str='hello'
mul_str1(str)

def mul_str2(str):
    result=str*10
    print("input string 10 times:",result)
#pass by ref
x=input("please enter string:")
x='hello'
mul_str2(x)

"""
# 3). Python function program to print a table of a given number.
"""
def table(num):
    for i in range(1,11):
        result=i*num
        print("Table of given no:",result)
table(2)

"""

# 4). Python function program to find the maximum of three numbers.
# Input: 17, 21, -9
# Output: 21
"""
def max_num(num1,num2,num3):
    if num1>num2 and num1>num3:
        print("num1 is greater",num1 )
    # else:
    #      print("num3 is greater:",num3)
    elif num2>num1 and num2>num3:
        print("num2 is greater:",num2)
    else:
        print("num3 is greater",num3)

max_num(10000000000000,20000,500000)
"""
#
# 5). Python function program to find the sum of all the numbers in a list.
# Input : [6,9,4,5,3]
# Output: 27

# Create a function total
# Use the def keyword to define the function.
# Pass a parameter i.e. list to the function.
# Create a variable and assign its value equal to 0.
# Use a for loop to iterate over the values in the list.
# After each iteration add the values to the variable.
# Print the output.
# Create a list and pass that list to the function while calling the function.
"""
def total(lst):
    var= 0
    for i in lst:
        var = var+i
    print("sum of list number:",var)
lst=[6,9,4,5,3]
total(lst)
"""


# def total(lst):
#     var=0
#     for i in lst:
#         var= var+i
#     print(var)
# lst=[1,2,3]
# total(lst)

# 6). Python function program to multiply all the numbers in a list.
# Input : [-8, 6, 1, 9, 2]
# Output: -864
"""
def multiplicarion(lst):
    var=1
    for i in lst:
        var=var*i
    print(var)
lst=[-8,6,1,9,2]
multiplicarion(lst)
"""
#
# 7). Python function program to reverse a string.
# Input: Python1234
# Output: 4321nohtyp
"""
def reverse(str):
    new_str=str[::-1]
    print(new_str)
str='Python1234'
reverse(str)
"""
#
# 8). Python function program to check whether a number is in a given range.
# Input : num = 7, range = 2 to 20
# Output: 7 is in the range

# Create a function check
# Use the def keyword to define the function.
# Pass a parameter i.e. number to the function.
# Check whether the number lies between 1-20 using an if-else statement.
# If the number lies between 1-20 then print True else print False.
# Take a number through the user as input and pass it to the function while calling the function.

"""
def check(num):
    if num in range (1,20):
        print(True)
    else:
        print(False)
num=25
check(num)

"""

# 9). Python function program that takes a list and returns a new list with unique elements of the first list.
# Input : [2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
# Output : [2, 3, 1, 4, 6 ]

# Create a function unique
# Use the def keyword to define the function.
# Pass a parameter i.e. list to the function.
# Convert the list to set using set() to remove the duplicate values.
# Now convert it back to the list using list().
# Print the output.
# Create a list and pass that list to the function while calling the function.

"""
def unique(lst):
    set_lst=set(lst)
    print(list(set_lst))
lst=[1,1,2,2,3,3]
unique(lst)

"""

# 10). Python function program that take a number as a parameter and checks whether the number is prime or not.
# Input : 7
# Output : True
#
# def prime(num):
#     for i in range (2,num):
#         if num%i==0:
#           print(False)
#         else:
#             print(True)
# num=10
# prime(num)
"""
def prime(num):
    for i in range (2,num):
        if num%i==0:
          print(False)
          break
    else:
     print(True)
num=11
prime(num)
"""

# 11). Python function program to find the even numbers from a given list.
# Input : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Output : [2, 4, 6, 8]
"""
new_lst=[]
def even(lst):
    for val in lst:
        if val%2==0:
            new_lst.append(val)
    print(new_lst)
lst=[2,4,56,3,1]
even(lst)


"""

# 12). Python function program to create and print a list where the values are squares of numbers between 1 to 10.
# Input: 1 to 10
# Output: 1, 4, 9, 16, 25, 36, 49, 64, 81
"""
def square(square):
    for i in range (1,10):
        square=i**2
        print(square,end=' ')
square(square)
"""
# 13). Python function program to execute a string containing Python code.

# mycode = 'print("Python")'
# code = """
# def mutiply(x,y):
#     return x*y
#
# print('sqatools')
# """
# exec(mycode)
# exec(code)

# 14). Python function program to access a function inside a function.
"""
def outer_fun():
    print("its outer")
    def inner_fun():
        print("its inner")
    inner_fun()
    def inner_fun1():
        print("its inner_fun1")
    inner_fun1()
outer_fun()

"""
# def test(a):
#         def add(b):
#                 nonlocal a
#                 a += 0
#                 return a+b
#         return add
# func= test(10)
# print(func(10))


# 15). Python function program to find the LCM of two numbers.
# Input: 12, 20
# Output: 60

# LCM Definition
# The LCM of two or more numbers is defined as the smallest number that can be divided by all of the numbers.
#
# LCM is the least number that is a common multiple of all the given numbers.
#
# For an example, let’s find the LCM of 6 and 18.
#
# Solution:
#
# Multiple of 6 = 6, 12, 18, 24, 30, …
#
# Multiple of 18 = 18, 36, 54, …
#
# LCM = first common multiple (least common multiple)
#
# LCM = 18


# def lcm(num1,num2):
#     if num1>num2:
#         greater=num1
#     else:
#         greater=num2
#     while(True):

# def lcm(num1,num2):
#     if num1 > num2:
#         greater = num1
#     else:
#         greater = num2
#
#     while(True):
#         if((greater % num1 == 0) and (greater % num2 == 0)):
#             lcm = greater
#             break
#         greater += 1
#
#     print(f"L.C.M of {num1} and {num2}: {lcm}")
#
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# lcm(num1,num2)
"""
def lcm(num1,num2):
    for i in range(1,num1*num2+1):
        if i%num1==0 and i%num2==0:
         print(i)
         break

num1=15
num2=42
lcm(num1,num2)
"""
"""
def lcm(num1,num2):
    for i in range(1,num1*num2+1):
        if i%num1==0 and i%num2==0:
         print(i)
         break
num1=24
num2=54
lcm(num1,num2)
"""

# 16). Python function program to calculate the sum of numbers from 0 to 10.
# Output: 55
"""
def sum():
     total=0
     for i in range(0,10):
         total=total+i
     print(total)
sum()
"""
#
# 17). Python function program to find the HCF of two numbers.
# Input: 24 , 54
# Output: 6

"""
def hcf(num1 ,num2):
    if num1>num2:
        smaller=num2
    else:
        smaller=num1
    for i in range(1,smaller+1):
        if num1%i==0 and num2%i==0:
            hcf=i
    print(hcf)
num1=24
num2=54
hcf(num1,num2)
"""
#24=1,2,3,4,6,8,12,24
#54=1,2,3,6,9,18,27

#24=24,48,72,96,120,144,168,192,216
#54=54,108,162,216

# 18). Python function program to create a function with *args as parameters.
# Input: 5, 6, 8, 7
# Output: 125 216 512 343
"""
def argument(*args):
    for num in args:
        print(num**3,end=' ')
argument(1,2,3,7)
"""
# 19). Python function program to get the factorial of a given number.
# Input: 5
# Output: 120
"""
def facorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
facorial(5)
"""

# 20). Python function program to get the Fibonacci series up to the given number.
# Input: 10
# Output: 1 1 2 3 5 8 13 21 34
"""
def fibo(num):
    a=0
    b=1
    for i in range(2,num):
        c=a+b
        a=b
        b=c
    print(c)
fibo(11)
"""
























































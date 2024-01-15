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
# 21). Python function program to check whether a combination of two numbers has a sum of 10 from the given list.
# Input : [2, 5, 6, 4, 7, 3, 8, 9, 1]
# Output : True
"""
def check_sum(nums, k):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == k:
                return True
    return False
print(check_sum([2, 5, 6, 4, 7, 3, 8, 9, 1], 10))
"""
#
# 22). Python function program to get unique values from the given list.
# Input : [4, 6, 1, 7, 6, 1, 5]
# Output : [4, 6, 7, 5]
"""
def unique():
    new_lst=set(lst)
    print(new_lst)
lst=[4,6,1,7,6,1,5]
unique()
"""

# 23). Python function program to get the duplicate characters from the string.
# Input: Programming
# Output: {‘g’,’m’,’r’}
"""
def duplicate():
    lst=[]
    for char in str:
        if str.count(char)>1:
            lst.append(char)
    print(set(lst))
str="programming"
duplicate()
"""


# 24). Python function program to get the square of all values in the given dictionary.
# Input = {‘a’: 4, ‘b’ :3, ‘c’ : 12, ‘d’: 6}
# Output = {‘a’: 16, ‘b’ : 9, ‘c’: 144, ‘d’, 36}
"""
def square(dict1):
    dict2={}
    for key, val in dict1.items():
        value=val**2
        dict2[key]=value
    print(dict2)
dict1= {'a': 4, 'b' :3, 'c' : 12, 'd': 6}
square(dict1)
"""

# 25). Python function program to create dictionary output from the given string.
# Note: Combination of the first and last character from each word should be
# key and the same word will the value in the dictionary.
# Input = “Python is easy to Learn”
# Output = {‘Pn’: ‘Python’, ‘is’: ‘is’, ‘ey’: ‘easy’, ‘to’: ‘to’, ‘Ln’: ‘Learn’}

"""
def dicttostr(str):
    dict={}
    word=str.split()
    for char in word:
       dict[char[0]+char[-1]]=char
    print(dict)
str='Python is easy to Learn'
dicttostr(str)

"""

# 26). Python function program to print a list of prime numbers from 1 to 100.
"""
def prime1to100():
    for num in range(1,100):##1#2##4
        count=0
        for i in range(1,num+1):##1,2#1,2,3##1,2,3,4,5
           if num%i==0:
            count=count+1
        if count==2:
           print(i,end=' ')
prime1to100()

"""

# 27). Python function program to get a list of odd numbers from 1 to 100
"""
def odd1to100():
    for num in range(1,100):
        if num%2!=0:
           print(num,end=' ')
odd1to100()

"""
# 28). Python function program to print and accept login credentials.
"""
def auth():
    name='admin'
    password='admin123'
    print('login succesfully')
auth()

"""

# 29). Python function program to get the addition with the return statement.
"""
def addition(a,b):
    total=a+b
    return total
result=addition(10,222)
print(result)

"""
def addition(a,b):
    total=a+b
    print(total)
addition(10,20)









# 30). Python function program to create a Fruitshop Management system.
# Create a function fruit.
# Use the def keyword to define the function.
# Pass three parameters i.e. fruit name, fruit price, and fruit quantity.
# Print the fruit name, fruit price, and fruit quantity.
# Calculate the total bill by multiplying fruit price and fruit quantity.
# Print the bill.
# Pass the fruit name, fruit price, and fruit quantity to the function while calling the function.

"""
def fruit(fruit_name,fruit_price,fruit_quantity):
    fruit_name='apple'
    fruit_price=100
    fruit_quantity=5
    bill=fruit_price*fruit_quantity
    print(bill)
fruit('apple',200,5)

"""
"""
def fruit(fname,fprice,quantity):
    print("Fruit name: ",fname)
    print("Fruit price: ",fprice)
    print("Fruit quantity in kg: ",quantity)
    print("Bill : ",fprice*quantity)
fruit("Apple",10,2)
"""

# 31). Python function program to check whether the given year is a leap year.
"""
def leap(year):
    if year%400==0 and  year%4==0:
        print("leap year")
    else:
        print("not leap year")
leap(2000)
"""


# 32). Python function program to reverse an integer
"""
def rev(num):
    print(str(num)[::-1])
rev(254)
"""
"""
def rev(num):
    rev=0
    while num>0:
        r=num%10
        rev=(rev*10)+r
        num=num//10
    print(rev)
rev(789)
"""
"""
def rev(num):
    rev=0
    while num>0:
        r=num%10
        rev=(rev*10)+r
        num=num//10
    print(rev)
rev(456)

"""


# 33). Python function program to create a library management system.

# Create a function library.
# Use the def keyword to define the function.
# Pass two parameters i.e. book name and customers name.
# Print the book name and customer name.
# Pass the book name and customer name to the function while calling the function.
"""
def library(book_name,cust_name):
    print("book_name:",book_name)
    print("customer_name:",cust_name)
library('python','tushar')
"""

# 5- write a program which takes the name of the user as input and print the index of character 'a' in the string.
# write a program which takes the name of the user as input and print the index of character 'a' in the string.
# if 'a' is not there then return -1.

# str='tushr'
# # x=str.index('a')
# # print(x)
#
# y=str.find('a')
# print(y)

# 6-  Display the number of letters in the below string
# my_word = "antidisestablishmentarianism"




# str='ggggggggggsssss'
# x=str.count('g')
# print(x)
































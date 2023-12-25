#1). Python program to check given number is divided by 3 or not.
"""
num1=int(input("Please enter the number:"))

if num1%3==0:
    print("The given number is divided by 3",num1)
else:
    print("The Given number is not divided by 3",num1)

"""

#2). If else program to get all the numbers divided by 3 from 1 to 30.
"""
for num in range(1,31):
    #print(num)
    if num%3==0:
        print(num)

"""

#3). If else program to assign grades as per total marks.
# marks > 40: Fail
# marks 40 – 50: grade C
# marks 50 – 60: grade B
# marks 60 – 70: grade A
# marks 70 – 80: grade A+
# marks 80 – 90: grade A++
# marks 90 – 100: grade Excellent
# marks > 100: Invalid marks
"""
marks=int(input("Please enter student marks:"))


if marks<40:
    print("You are Fail")
elif marks>=40 and marks<50:
    print("You pass with  c grade")
elif marks>=50 and marks<60:
    print("You Pass with B grade")
elif marks>=60 and marks <75:
    print("you pass with A grade")
elif marks>=75 and marks<90:
    print("you pass with A+ grade")
elif marks>=90 and marks<=100:
    print("you are topper")
else:
    print("plese enter marks between 1 to 100")

"""
#4). Python program to check the given number divided by 3 and 5.
"""
num=int(input("please enter the number:"))

if num%3==0 and num%5==0:
    print("number is divide by 3 and 5")
else:
    print("number is not divided by 3 and 5")
"""
#5). Python program to print the square of the number if it is divided by 11.

"""
num=int(input("please enter the number:"))

square_num=num**2

if square_num%11==0:
    print("square of no is divided by 11:",square_num)
else:
    print("square of no is not divided by 11: ",square_num)
    
"""

#6). Python program to check given number is a prime number or not.
"""
num1=int(input("please enter the number:"))

prime=True
for i in range (2,num1):  
    
    if num1%i==0:
        prime= False
        
if prime:
    print("This is prime number:",num1)
else:
    print("This is not prime number:",num1)

"""
"""
num1=int(input("Please enter the no:"))

prime=True

for i in range (2,num1):
    if num1%i==0:
        prime=False
if prime:
    print("no is prime")
else:
    print("no is not prime")

"""
"""
num=int(input("please enter the number:"))

prime=True

for i in range (2,num):
    if num%i==0:
        prime=False
if prime:
    print("no is prime")
else:
    print("no is not prime")

"""
"""
num1=int(input("please enter no:"))

prime=True

for i in range (2,num1):
    if num1%i==0:
        prime=False
if prime:
    print("no is prime")
else:
    print("no is not prime")
    
    """

#7). Python program to check given number is odd or even.
"""

num=int(input("please enter no:"))

if num%2==0:
    print("no is even")
else:
    print("no is odd")

"""

#8). Python program to check a given number is part of the Fibonacci series from 1 to 10.

#The Fibonacci sequence is a type series where each number is the sum of the two that precede it.
# It starts from 0 and 1 usually. The Fibonacci sequence is given by 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on.
# The numbers in the Fibonacci sequence are also called Fibonacci numbers.
"""
a=0
b=1
for i in range (10):
    print (b,end=" ") #by default print fun have /n means it prints on next line so here used end " " to print op in single line
    a,b=b,a+b
"""
    # 0,1=1,0+1
    # 1,1=1,2
    # 2,1=2,3
    # 3,2=3,5
    # 4,3=4,7
    # 5,4=5,9
    # 6,5=6,11
    # 7,6=7,13
    # 8,7=8,15
    # 9,8=9,17
    # 10,9=10,19

##################################
"""
a=0
b=1

print(a)
print(b)
for i in range (2,10):
    c=a+b
    a=b
    b=c
    print(c)

"""


"""
a=0
b=1
print(a)
print(b)
for i in range (2,10):
    c=a+b
    a=b
    b=c
    print(c)

"""

#9). Python program to check authentication with the given username and password.

# Steps to solve the program
# Take Username and password as input through the user.
# If the username and password is equal then it is authenticate.
# Use if-else statement for this purpose.
# Print the output.

"""
user_name=input("Please enter user name:")
password=input("please enter password:")

if user_name==password:
    print("Login successful")
else:
    print("login fail")
    
    """


#10). Python program to validate user_id in the list of user_ids.
"""
user=int(input("please enter user id:"))

for user_id in range (1,10):
    if user in user_id:
        print("valid user")
    else:
        print("invalid user")
   """


"""
id_list = [1,2,3,5,6,7,8]
id_ = int(input("Enter ID number: "))

if id_ in id_list:
    print("Valid ID")
else:
    print("Invalid ID")


"""

#############################################

#11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
"""
user_input=int(input("please enter the number:"))

square=user_input**2
cube=user_input**3

if square%2==0 or cube%3==0:
    print("given no square or cube is divisible by 2 or 3")
else:
    print("given no square or cube is not divisible by 2 or 3 ")
"""

# Take a number as input through the user.
# If the number is divided by 2 then print its square.
# If the number is divided by 3 then print its square.
# Use if-else statement for this purpose.
# Print square or cube.

"""
num=int(input("please enter the no:"))
if num%2==0:
    print("square of no:",num**2)
elif num%3==0:
    print("cube of no:",num**3)
else:
    print("no is not divisible by 2 or 3")

"""

#12). Python program to describe the interview process.
"""
round1="pass"
round2="fail"
if round1=="pass":
    print("first round cleared")
    if round2=="pass":
        print("second round cleared")
    else:
        print("second round not cleared")
else:
     print("first round is not cleard")
   """

"""
round1 = input("Enter round1 result:")
round2 = input("Enter round2 result:")

if round1 == "passed":
    print("Congrats your 1st round is clear")
    if round2 == "passed":
        print("Congrats 2nd round is clear, you are placed")
    else:
        print("Failed in 2nd round, please try next time")
else:
    print("Failed in 1st round, please try next time")

"""


#13). Python program to determine whether a given number is available in the list of numbers or not.

"""
num=int(input("please enter no:"))
list=[1,2,3,4,5]
if num in list:
    print("number is available in list")
else:
    print("number is not available in list")
"""

#14). Python program to find the largest number among three numbers.

"""

num1=int(input("please enter first no:"))
num2=int(input("please enter second no:"))
num3=int(input("please enter third no:"))

if num1>num2:
    if num1>num3:
        print("num1 is large")
    #else:
        #print("num3 is large")
else:
    if num2>num3:
        print("num2 is large")
    else:
        print("num3 is large")
        """
"""
num1=int(input("please enter first no:"))
num2=int(input("please enter second no:"))
num3=int(input("please enter third no:"))

if num1>num2:
    if num1>num3:
        print("num1 is large")
    else:
        print("num3 is large")
else:
    if num2>num3:
         print("num2 is large")
    else:
        print("num3 is large")
        
"""
"""
num1=int(input("please enter first no:"))
num2=int(input("please enter second no:"))
num3=int(input("please enter third no:"))

if num1>num2:
    if num1>num3:
        print("num1 is large")
    else:
        print("num 3 is large")
else:
    if num2>num3:
        print("num2 is large")
    else:
        print("num 3 is large")
"""


#15). Python program to check any person eligible to vote or not
# age > 18+ : eligible
# age < 18: not eligible
"""
age=int(input("please enter your age:"))

if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to give vote")
    
    """

# 16). Python program to check whether any given number is a palindrome.
# Input: 121
# Output: palindrome

# What is palindrome number?
# A palindromic number (also known as a numeral palindrome or a numeric palindrome) is a number
# (such as 16461) that remains the same when its digits are reversed.
# In other words, it has reflectional symmetry across a vertical axis.
#
# Steps to solve the program
# Take a number as input.
# Reverse the given number and store it in another variable.
# Check whether both the numbers are equal or not using an if-else statement.
# Print the respective output.


"""
num1=122
num2=str(num1)

if num1==int(num2[::-1]):
    print("Given no is palindromic")
else:
    print("given no is not palindromi")
    
   """

"""
num1=int(input("please enter no:"))
num2=str(num1)

if num1==int(num2[::-1]):
    print("given no is palindrome")
else:
    print("given no is not palindrome")

"""

# 18). Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.
# Input = Enter marks: 45
# Output = Pass
"""
marks=int(input("please enter student marks:"))
if marks>=35:
    print("student is passed")
else:
    print("student is failed")
    """


# 19). Python program to check whether the given number is positive or not.
# Input = 20
# Output = True
#A positive number is any number greater than 0
"""
num=int(input("please enter no:"))

if num>0:
    print("The given no is positive")
else:
    print("The given no is negative")
  """


# 20). Python program to check whether the given number is negative or not.
# Input = -45
# Output = True

"""
num=int(input("Please enter no:"))

if num<0:
    print("The given no is negative")
else:
    print("The given no is positive")
"""

# 21). Python program to check whether the given number is positive or negative and even or odd.
# Input = 26
# Output = The given number is positive and even
"""
num=int(input("Please enter number:"))

if num>0:
    if num%2==0:
        print("The given no is positive and even")
    else:
        print("The given no is positive and odd")
else:
    if num%2==0:
        print("The given no is negative and even")
    else:
        print("The given no is negative and odd")
        
        """

# 22). Python program to print the largest number from two numbers.
# Input:
# 25, 63
# Output = 63

"""
num1=int(input("please enter first no:"))
num2=int(input("please enter second no:"))

if num1>num2:
    print("num1 is largest",num1)
else:
    print("num2 is largest",num2)

"""
#
# 23). Python program to check whether a given character is uppercase or not.
# Input = A
# Output = The given character is an Uppercase
"""
str1=input("please enter string:")
result=str1.isupper()
print(result)
"""
"""
char = input("Enter a character: ")
if char.isupper():
    print("True")
else:
    print("False")
    
    """

# 24). Python program to check whether the given character is lowercase or not.
# Input = c
# Output = True
"""
char=input("please enter char:")
result=char.islower()
print(result)

"""
"""
char=input("please enter char:")
if char.islower():
    print("true")
else:
    print("false")
    
    """

# 25). Python program to check whether the given number is an integer or not.
# Input = 54
# Output = True

# An integer is a whole number (not a fractional number) that can be positive, negative, or zero.
# Examples of integers are: -5, 1, 5, 8, 97, and 3,043.
# Examples of numbers that are not integers are: -1.43, 1 3/4, 3.14,

#num=int(input("please enter no:"))
"""
num=3.4
if type(num)==int:
    print("The given no is integer")
else:
    print("The given no is not integer")
    
    """

# 26). Python program to check whether the given number is float or not.
# Input = 12.6
# Output = True
"""
num=input("please enter no:")
#num=4
if type(num)==float:
    print("The given no is float")
else:
    print("The given no is not float")
"""

# 27). Python program to check whether the given input is a string or not.
# Input = ‘sqatools’
# Output = True
"""
str1="sqatools"
print(type(str))
if type(str1)==str:
    print("string",str1)
else:
    print("not string",str1)


"""

# 28). Python program to print all the numbers from 10-15 except 13
# Output:
# 10
# 11
# 12
# 14

"""
for i in range(10,15):
    if i!=13:
        print(i)
        
        """

# 29). Python program to find the electricity bill. According to the following conditions:
# Up to 50 units rs 0.50/unit
# Up to 100 units rs 0.75/unit
# Up to 250 units rs 1.25/unit
# above 250 rs 1.50/unit
# an additional surcharge of 17% is added to the bill
# Input = 350
# Output = 438.75

"""
units=int(input("Please enter bill units:"))

if units<=50:
    print("Bill:",(units*0.50)+(units*0.50)*17/100)
elif units<=100:
    print("Bill:",(units*0.75)+(units*0.75)*17/100)
elif units<=250:
    print("Bill:",(units*1.25)+(units*1.25)*17/100)
elif units>250:
    print("Bill:",(units*1.50)+(units*1.50)*17/100)
    
    """

"""

total_unit = int(input("Total units Consumed="))
bill_amount = 0


for bill_unit in range(1, total_unit+1):
    if bill_unit <= 50:
        bill_amount = bill_amount + 0.50
    elif bill_unit > 50 and bill_amount <= 100:
        bill_amount = bill_amount + 0.75
    elif bill_unit > 100 and bill_amount <= 250:
        bill_amount = bill_amount + 1.25
    elif bill_unit > 250:
        bill_amount = bill_amount + 1.5

bill_amount_sur = bill_amount + bill_amount * (17/100)
print("Bill amount with surcharge :", bill_amount_sur)

"""

# 30). Python program to check whether a given year is a leap or not.
# Input = 2000
# Output = The given year is a leap year

# What is a leap year? To be a leap year, the year number must be divisible by four –
# except for end-of-century years, which must be divisible by 400.
# This means that the year 2000 was a leap year, although 1900 was not. 2024, 2028, 2032 and 2036 are all leap years.

"""
Year=int(input("please enter year:"))
if Year%4==0 and Year%400==0:
    print("This is leap year")
else:
    print("This is not leap year")
    
    """

"""
year = int(input("Enter the year: "))

if (year%100 != 0 or year%400 == 0) and year%4 == 0:
    print("The given year is leap year.")
else:
    print("The given year is not leap year.")
    
    """

# 31). Python Python program to check whether the input number if a multiple of two print “Fizz” instead of the number
# and for the multiples of three print “Buzz”. For numbers that are multiples of both two and three print “FizzBuzz”.
# Input = 14
# Output = Fizz
# Input = 9
# Output = Buzz
# Input = 6
# Output = FizzBuzz
"""
num=int(input("please enter no:"))
if num%2==0 and num%3==0:
    print("FizzBuzz")
elif num%2==0:
    print("Fizz")
elif num%3==0:
    print("Buzz")
else:
    print("Number is not multiple of 2 and 3")
    
"""













































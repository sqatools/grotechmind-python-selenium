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














































































#1). Python Program to add two integer values.
print("1). Python Program to add two integer values.")

x= 10
y= 20
z=x+y
print(z)

#2). Python Program to subtract two integer values.
print("2). Python Program to subtract two integer values.")

x=20
y=10
z=x-y

print(z)

#3). Python program to multiply two numbers.
print("3). Python program to multiply two numbers.")

Val1 = 20
Val2 = 30
Mult = Val1*Val2

print(Mult)

#4). Python program to repeat a given string 5 times.
print("4). Python program to repeat a given string 5 times.")

inp = "we are togather, "

print(inp * 5)

#5). Python program to get the Average of given numbers.
print("5). Python program to get the Average of given numbers.")

a = 40
b = 50
c = 30

Avg = (a+b+c)/3
print("Avarage:" ,Avg)

#6). Python program to get the median of given numbers. Note: (Doubts)
print("6). Python program to get the median of given numbers. Note: (Doubts)")

L1 = [45, 60, 61, 66, 70, 77,80]       #List
x = L1.sort()      # It is using for sort the list in ascending order and return None.
y = (len(L1))      # It is using for return the number of items in a container (List).
z = y/2
print(y)
print(z)
print("Median :",L1[int(z)])

#7). Python program to print the square and cube of a given number.
print("7). Python program to print the square and cube of a given number.")

s1 = 8
R1 = 8**2  # Num**2 is for square
R2 = 8**3  # Num**3 is for cube
print("sq:",R1)
print("Cube:", R2)

#8). Python program to interchange values between variables.
print("8). Python program to interchange values between variables.")

a =   200 #int(input("enter the value1 : "))
b =   300 #int(input("enter the value2 : "))
a,b = b,a
print("a:",a)
print("b:",b)

#9). Python program to solve this Pythagorous theorem.
# Theorem : (a2 + b2 = c2)
print("9). Python program to solve this Pythagorous theorem.")

import math
s1 = 3
s2 = 5
hypo = (s1**2 + s2**2)
print("hypotenuse side :" ,math.sqrt(hypo))

#10). Python program to solve the given math formula.
# Formula : (a + b)2 = a^2 + b^2 + 2ab
print("10). Python program to solve the given math formula.")

a = 5
b = 4
#R1 = a**2 + b**2 + 2*a*b
R1 = 5**2 + 4**2 + 2*5*4

#R2 = (a+b)**2
R2 = (5+4)**2
print("(a+b)^2 :", R1)
print("(a+b)^2 :", R2)

#11). Python program to solve the given math formula.
# Formula : (a – b)2 = a^2 + b^2 – 2ab
print("11). Python program to solve the given math formula.")

a = 8
b = 3

#R1 = a^2 + b^2 – 2ab
R1 = 8**2 + 3**2 - 2*8*3

#R2 = (a-b)^2
R2 = (8-3)**2

print("(a-b)^2 :", R1)
print("(a-b)^2 :", R2)

#12). Python program to solve the given math formula.
# Formula : a2 – b2 = (a-b)(a+b)
print("12). Python program to solve the given math formula.")

a = 5
b = 3

#R1 = (a-b)*(a+b)
R1 = (5-3)*(5+3)
#R2 = a^2-b^2
R2 = 5**2-3**2
print("(a^2-b^2):",R1)
print("(a^2-b^2):",R2)

#13). Python program to solve the given math formula.
# Formula : (a + b)3 = a3 + 3ab(a+b) + b3
print("13). Python program to solve the given math formula.")

a = 5
b = 6

# R1 = a^3 + 3*a*b(a+b) + b^3
R1 = 5**3 + 3*5*6*(5+6) +6**3
print("(a+b)^3:", R1)
# R2 = (a+b)^3
R2 = (5+6)**3
print("(a+b)^3:",R2)

# #14). Python program to solve the given math formula.
# Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3
print("14). Python program to solve the given math formula.")

a = 6
b = 4
# R1 = a^3 -3*a^2*b + 3*a*b^2 -b^3
R1 = 6**3 - 3*6**2*4 + 3*6*4**2 -4**3
print("(a-b)^3:", R1)
# R2 = (a-b)^3
R2 = (6-4)**3
print("(a-b)^3:",R2)

#15). Python program to calculate the area of the square.
# Formula : area = a*a
print("15). Python program to calculate the area of the square.")

a = 10 #int(input("enter the value of the square side: "))
# R1 = a**2
R1 = a**2
print("(Area of square:",R1)

# 16). Python program to calculate the area of a circle.
# Formula = PI*R^2
# R = Radius
# PI = 3.14    # value of Pi
print("16). Python program to calculate the area of a circle.")

R = 9 #int(input("Enter the value of R:"))
Pi = 3.14
Area = Pi * R**2
print("(Area of circle:)", Area)

# 17). Python program to calculate the area of a cube.
# Formula = 6*a*a
print("17). Python program to calculate the area of a cube.")

a = 7 #int(input("Enter the value of side:"))
R = 6 *a**2
print("(Area of cube:)", R)

# 18). Python program to calculate the area of the cylinder.
# Formula = 2*PI*r*h + 2*PI*r*r
print("18). Python program to calculate the area of the cylinder.")
#r = radius of cylinder
#h = Hight of cylinder

r =  5  #int(input("Enter the value of radius of cylinder:"))
h =  10 #int(input("Enter the value of hight of cylinder:"))
Pi = 3.14   # value of Pi
Area = 2*Pi*r*h + 2*Pi*r**2
print("(Area of cylinder:)",Area)

# 19). Python program to check whether the given number is an Armstrong number or not.
# Example: 153 = 1*1*1 + 5*5*5 + 3*3*3
print("19). Python program to check whether the given number is an Armstrong number or not.")

num = a =  151  # int(input("enter the arm value: "))
Rev = 0
while a>0:
    skt = a%10
    Rev = Rev + skt**3
    a = a//10
if Rev == num:
    print("it is a armstrong value")
else:
    print("it is not a armstrong value")

"""
20). Python program to calculate simple interest.
Formula = P+(P/r)*t
P = Principle Amount
r = Anual interest rate
t = time
"""
print("20). Python program to calculate simple interest.")

P = 20000
r = 12
t = 4
F = P+(P/r)*t
#F = 20000+(20000/12)*4
print("Intrest:",F)

# 21). Python program to print the current date in the given format.
# Output: 2023 Jan 05
# Note: Use the DateTime library
print("21). Python program to print the current date in the given format.")

#Current_Date = ("23 Dec 15")
#print(Current_Date)

import datetime
date = datetime.datetime.now()
print(date.strftime(" %y %b %d"))

# 22). Python program to calculate days between 2 dates.
# Input date : (2023, 1, 5) (2023, 1, 22)
# Output: 17 days
print("22). Python program to calculate days between 2 dates.")

from datetime import date
D1 = date(2023, 10, 29)
D2 = date(2023, 11, 15)
Result = (D2 - D1).days
print(" Days b/w 2 dates: ", Result, "Days")

# 23). Python program to get the factorial of the given number.
print("23). Python program to get the factorial of the given number.")

num = n = 5 #int(input("Enter the value: "))
fact = 1
while  n > 0 :
    fact =fact * n
    n = n - 1
    print("Value of Factorial=" , n , ":", fact)
# Or
print(" Or")
print("Factorial = " , num , ":", fact)

# 24). Python program to reverse a given number.
print("24). Python program to reverse a given number.")

num1 = 12345
rev = str(num1)
print("rev:" , rev[::-1])

# 25). Python program to get the Fibonacci series between 0 to 50.
print("25). Python program to get the Fibonacci series between 0 to 50.")

num1 = 0
num2 = 1
T_count = 1

print("Sequence is:", end= " ")
#for i in range (11):
while T_count <11:
    print( num2 , end=" ")
    num1 , num2 = num2 ,num1 + num2
    T_count = T_count+1

print()


# 26). Python program to check given number is palindrome or not.
print("26). Python program to check given number is palindrome or not.")

n = num = 121 #int(input("Enter the value: "))         # n = num = 121
R1 = 0                                            # R1 = 0
while n>0:                                        # 121 > 0
    r1 = n%10                                     # r1 = 1
    R1 = R1*10 + r1                               # R1 = 1
    n = n//10                                     # n  = 12
if num == R1:                                     # 121 == 1
    print(" it is a palindrome ")
else:
    print(" it is not a palindrome")

# 27). Python program to calculate compound interest.
#  Formula = p*((1+r/100)**n)

print(" 27). Python program to calculate compound interest.")

p = 10000  # int(input("enter the principle amount: "))
r = 5      # int(input("enter the intrest rate: "))
n = 3      # int(input("enter no of years: "))
f= p*((1 + r / 100) ** n)
print("Compound intrest :" , f)

#28). Python program to check the prime number.
print("28). Python program to check the prime number.")

num = 13      #int(input("enter the number : "))

prime = True

for i in range (2, num ):
    if num%i ==0:
        prime = False
if prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")











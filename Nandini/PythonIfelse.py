#1). Python program to check given number is divided by 3 or not.
"""
num1=7

if(num1%3==0):
    print("Number is divisible by 3 is", num1)
else:
    print("Number is not divisible by 3 is", num1)
"""
#Number is not divisible by 3 is 7

#2). If else program to get all the numbers divided by 3 from 1 to 30.
"""
for i in range(1,31):
   if(i%3==0):
        print("The number is divisible by 3 =",i)
   else:
       print("-")
"""
"""
#64). Python program to accept marks from the user allot the stream based on the following criteria.
Marks>85: Science
Marks>70: Commerce
35<Marks<70: Arts
Marks<35: Fail
Input = Marks: 88
Output = Science


marks = int(input("Marks :"))

if marks >= 85 and marks < 101:
    print("Output = Science")
elif marks >= 70 and marks < 85:
    print("Output = Commerce")
elif marks >= 35 and marks < 70:
    print("Output = Arts")
elif marks < 35 and marks > 0:
    print("Output = Fail")
else:
    print("Output is Invalid")

#Marks :97
#Output = Science

"""

"""
63). Python program to accept two numbers and mathematical operations from users and perform mathematical operations according to it.
Input:
A=30
B=45
Operation = +
Output = 75
"""

a = int(input("A="))
b = int(input("B="))
operation = input("operation=")

if operation == "+":
    print("The addition =", a+b)
elif operation == "-":
    print("The subtraction =", a-b)
elif operation == "*":
    print("The Multiplication =", a*b)
elif operation == "/":
    print("The Division =", a/b)
else:
    print("Invalid Input")

"""
62). Python program to accept the temperature in Fahrenheit and check whether the water is boiling or not.
Hint: The boiling temperature of water in Fahrenheit is 212 degrees
Input = Enter temperature: 190
Output = Water is not boiling
"""

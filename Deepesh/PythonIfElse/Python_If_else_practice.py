"""
if  condition:
    code
else:
    code
"""
"""
num1 = 50
num2 = 51
print(num1 == num2)
if num1 == num2:
    print("both numbers are equal", num1, num2)
else:
    print("both numbers are not equal", num1, num2)


user_input = input("Please enter the value :")
user_input = int(user_input)
print(user_input, type(user_input), user_input*2)
"""
"""
print(user_input%2 == 0)
if user_input%2 == 0:
    print("This is even number :", user_input)
else:
    print("This is odd number :", user_input)
"""

"""
> : greater than
>= : greater than equal to
< : less than
<= : less than equal to
!= : not equal
== : equal to

Logical operator and , or
cond1 and cond2 
True and False : False
False and True : False
True and True : True
False and False : False

cond1 or cond2

True or False : True
False or True : True
True or True : True
False or False : False
"""

#
print("_" * 40)
a = 80
b = 100
c = 40

#   True and True : True
#   True and False : False
#   False and False : False
#   False and True : False
"""
if a > b and a > c:
    print("and cond :a has greater value")
else:
    print("and cond : a does not have greater value")


#  False or True : True
if a > b or a > c:
    print("or cond : a has greater value")
else:
    print("or cond : a does not have greater value")
"""

"""
# program : check any number is divisible by 3 and 7
num1 = int(input("Please enter the number :"))
if num1%3 == 0 and num1%7 == 0:
    print("Given number can be divide by 3 and 7 :", num1)
else:
    print("Given number can not be divide by 3 and 7 :", num1)
"""

######### If- elif condition check #########
"""
if cond1:
    code
elif cond2:
    code
elif cond3:
    code
else:
    code
"""

"""
# program : write a program to print student grade as per marks percentage
marks = int(input("Enter students marks :"))


if marks >= 30 and marks <= 40:
    print("student passed with 3rd grade")
elif marks > 80 and marks <= 100:
    print("student passed with A++ grade")
elif marks >= 40 and marks <= 50:
    print("student passed with 2nd grade")
elif marks > 50 and marks <= 65:
    print("student passed with 1st grade")
elif marks > 65 and marks <= 80:
    print("student passed with A+ grade")
elif marks < 30:
    print("Really sorry you are failed")
else:
    print("Marks can not more than 100")
"""
"""
Nested if condition

if cond1:
     code
     if cond2:
        code
     else:
         code
else:
     code
"""
"""
round1 = "pass"
round2 = "fail"

if round1 == "pass":
    print("first round is cleared")
    if round2 == "pass":
        print("second round is cleared !!")
    else:
        print("second round is not clear, please try next")
else:
    print("first round is  not clear,  try next time")

"""
"""
Python program to find the electricity bill. According to the following conditions:
Up to 50 units rs 0.50/unit
Up to 100 units rs 0.75/unit
Up to 250 units rs 1.25/unit
above 250 rs 1.50/unit
an additional surcharge of 17% is added to the bill
Input = 350
Output = 438.75
"""

"""
total_unit = int(input("Total unit somsution :"))
rate = 0
if total_unit <= 50:
    rate = 0.5
elif total_unit > 50 and total_unit <=100:
    rate = 0.75
elif total_unit > 100 and total_unit <= 250:
    rate = 1.25
elif total_unit > 250:
    rate = 1.5

total_bill = total_unit*rate
print("total bill amount :", total_bill)

total_bill = total_bill + total_bill*(17/100)
print("total bill amount with surcharge :", total_bill)
"""

# Check given number is available in the list or not
list1 = [5, 7, 8, 2, 8, 23]
num1 = 15

"""
if num1 in list1:
    print("Value is available in the list :", num1)
else:
    print("value is not available in the list:", num1)
"""

if num1 not in list1:
    print("value is not available in the list :", num1)
else:
    print("value is available in the list :", num1)

var1 = 10

"""
if var1 is None:
    print("Var has empty value :", var1)
else:
    print("Var has some value to perform operation :", var1)
"""

if var1 is not None:
    print("Var has some value to perform operation :", var1)
else:
    print("var has empty value", var1)


# write if condition in one single line
vara = 51
output = "even" if vara%2 == 0 else "odd"
print("output :", output)


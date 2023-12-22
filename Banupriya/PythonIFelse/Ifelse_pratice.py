""""
if condition:
   code
else:
    code
"""

"""
num1=51
num2=50
print(num1>num2)
if num1 == num2:
    print("The numbers are equal")
else:
    print("The numbers are not equal")
"""
"""
print ("_"*50)
user_input1=int(input("Please enter the First value: "))
user_input2 =int(input("Please enter the second value: "))
if user_input1 == user_input2:
    print("The numbers are equal")
else:
    print("The numbers are not equal")
"""
"""
print("_"*50)
user_input=int(input("Please enter the First value: "))
print (user_input,type(user_input),user_input*2)
print(user_input%2 == 0)
if user_input%2 == 0:
   print("The numbers are even number",user_input)
else:
    print("The numbers are odd number",user_input)
"""
#Pratice program:
#1.Program to check if a number is divisible by 3
"""
print ("-"*50)
user_input = int(input("Please enter the value: "))
if user_input%3 == 0:
    print(user_input ,"The numbers is divisible by 3")
else:
    print(user_input,"The numbers is not divisible by 3")
"""
"""
#2.Python program to check number is divided by 3 and 5
num= int(input("Please enter the value: "))
if num%3 == 0 and num%5 == 0:
    print("The numbers are divisible by both 3 and 5")
else:
    print( "The numbers are not divisible by 3 and 5")
"""
#3.Program to get all numbers divided by 3 between 1 to 30
for i in range (1,31):
    if i%3 == 0:
        print (i,)

#4.If else program to assign grades as per total mark:
"""
marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks
"""
marks=int(input("Enter the mark scored:"))
if marks<40:
    print ("sorry you are  fail")
elif marks>=40 and marks>=50:
    print ("you are grade C")
elif marks<50 and marks>60:
    print ("you are grade B")




"""
print("_"*50)
evensum=0
oddsum=0
for i in range(1,21):
    if i%2 == 0:

        evensum=evensum+i
    else:
        oddsum = oddsum+i
print(evensum)
print(oddsum)
"""








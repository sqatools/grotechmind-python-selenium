#1). Python Program to add two integer values
'''
num1=100
num2=200
print(num1+num2)

user_input1=int(input("please enter number:"))
user_input2=int(input("please enter number:"))
print(user_input1+user_input2)
'''

#2). Python Program to subtract two integer values.
'''
num1=500
num2=300
print(num1-num2)

user_input1=int(input("please enter number:"))
user_input2=int(input("please enter number:"))
print(user_input1-user_input2)

'''

#Python program to multiply two numbers.
'''
num1=400
num2=500
print(num1*num2)

user_input1=int(input("please enter number:"))
user_input2=int(input("please enter number:"))
print(user_input1*user_input2)
'''
#4). Python program to repeat a given string 5 times.
#Input :
#str1 = “SQATools”
#Output :
#“SQAToolsSQAToolsSQAToolsSQAToolsSQATools”
'''
str1="SQATools"
print(str1*5)
'''

print('='*50)


#Python program to get the Average of given numbers.
#Formula: sum of all the number/ total number
#Input:
#a = 40
#b = 50
#c = 30
#Output :
#Average = 40

'''
a=40
b=50
c=30

print("Average:",(a+b+c)/3)
'''

#6). Python program to get the median of given numbers.
#Note: all the numbers should be arranged in ascending order
#Formula : (n+1)/2
#n = Number of values
#Input : [45, 60, 61, 66, 70, 77, 80]
#Output:  66
'''
input=[45,60,61,66,77,80]
input.sort()
a = (len(input))/2
print("Median: ",input[int(a)])

list1=[50,90,40,70,30,20,10]
list1.sort()
a=(len(list1))/2
print(list1[int(a)])
'''
#if we not used sort method then also it gives median but if we used sort method then first list will sort ascending order
# and then give median.
'''
list2=[10,70,20,90,50,40,60]
list2.sort()
a=(len(list2))/2
print(list2 [int(a)])

'''

#7). Python program to print the square and cube of a given number.
#Input :
#num1 = 9
#Output :
#Square = 81
#Cube =   729
'''
num1=9
print(num1**2)
print(num1**3)
'''
'''
user_input=int(input("enter the first value:"))
print(user_input**2)
print(user_input**3)

'''


#8). Python program to interchange values between variables.
#Input :
#a = 10
#b = 20
#Output :
#a = 20
#b = 10
'''
a=10
b=20

a,b = b,a

print("a: ",a)
print("b: ",b)
'''

#9). Python program to solve this Pythagorous theorem.
#Theorem : (a2 + b2 = c2)
'''
a=5
b=6

import math
hypo = a**2+b**2
print("Hypotenious side: ",math.sqrt(hypo))

'''

#10).Python program to solve the given math formula.
#Formula : (a + b)2 = a^2 + b^2 + 2ab
'''
a=5
b=6

lhs=a**2+b**2+2*a*b
print(lhs)

rhs=(a+b)*(a+b)
print(rhs)


result = a**2+2*a*b+b**2

print("(a+b)^2: ",result)

'''
#11). Python program to solve the given math formula.
#Formula : (a – b)2 = a^2 + b^2 – 2ab
'''
a=5
b=5
result=a**2+b**-2*a*b
print("(a-b)^2:",result)

'''


#12). Python program to solve the given math formula.
#Formula : a2 – b2 = (a-b)(a+b)
'''
a=5
b=10
result=(a-b)*(a+b)
print("a^2-b^2:",result)

'''

#13). Python program to solve the given math formula.
#Formula : (a + b)3 = a3 + 3ab(a+b) + b3
'''
a=5
b=5
result=a**3+3*a*b*(a+b)+b**3
print("(a+b)^3:",result)

'''

#14). Python program to solve the given math formula.
#Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3
'''
a=88
b=66

result=a**3-3*a*2*b+3*a*b**2-b**3
print("(a-b)^3:",result)

'''








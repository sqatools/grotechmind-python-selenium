# 1). Write a Python loops program to find those numbers
# which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
# Input1:1500
# Input2:2700
"""
for i in range (1500,2701):
    if i%7==0 and i%5==0:
        print("number is divisible by 7 and multiple of 5",i)
    else:
        print("number is not divisible by 7 and multiple of 5",i)
"""
import string

"""

for i in range(1500,2701):
        if i%7 == 0 and i%5 == 0:
            print(i, end=" ")

"""

# 2). Python Loops program to construct the following pattern, using a nested for loops.
# Output :
# *
# * *
# * * *
# * * * *
# * * * * *

"""

for i in range (1,6):
    for j in range(i):
        print("*",end=" ")
    print()
"""
"""
for i in range (1,6):
    for j in range (i):
        print("*",end=" ")
    print()
"""
#
# 2). Python Loops program to construct the following pattern, using a nested for loops.
# Output :
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
"""
for i in range (1,6):
    print("*"*i)
for i in range(4,-1,-1):
    print(i*"*")
"""
"""
for i in range(1,6):
    print(i*"*")
for i in range (4,-1,-1):
    print(i*"*")
"""

# 3). Python Loops program that will add the word from the user to the empty string using python.
# Input: “python”
# Output : “python”
"""
str=""
word=input("please enter string:")
for i in range (len(word)):
    str=str+word[i]
print(str)

"""
"""
str=""
word=input("please enter string:")
for i in range(len(word)):
    str=str+word[i]
print(str)

"""

"""
str=""
word=input("please enter string:")
for i in range (len(word)):
    str=str+word[i]
print(str)

"""
#
# 4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
# Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Output :
# Number of even numbers: 4
# Number of odd numbers: 5
"""
for i in range (1,10):
    if i%2==0:
        print("even",i)
    else:
         print("odd",i)
"""

# Steps to solve the program
# Take a series of numbers as input.
# Create two variables even and odd and assign their value equal to 0.
# Use for loop to iterate over each number from the series.
# If the number is even add 1 to the even and if the number is odd add 1 to the odd.
# Print the output.
"""
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even=0
odd=0
for val in numbers:
    if val%2==0:
        even=even+1
    else:
        odd=odd+1
print("count of even number:",even)
print("count of odd number:",odd)

"""
"""
numbers=(1,2,3,4,5,6,7,8,9,10)
odd=0
even=0

for val in numbers:
    if val%2==0:
        even=even+1
    else:
        odd=odd+1
print("count of even no:",even)
print("count of odd no:",odd)

"""


# 5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
"""
for i in range (0,7):
    if i!=3 and i!=6:
        print(i)

"""
#
# 6). Write a program to get the Fibonacci series between 0 to 20 using python.
# Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
"""
a=0
b=1
for i in range(2,20):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    
    """
#
# 7). Write a program that iterates the integers from 1 to 30 using python.
# For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
# For numbers that are multiples of both three and five print “FizzBuzz”.
"""
for i in range (1,31):
    if i%3==0 and i%5==0:
        print("FizzBuzz",i)
    elif i%3==0:
        print("Fizz",i)
    elif i%5==0:
        print("Buzz",i)

"""

# 8). Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python.
# Input : “SqaTOOlS”
# Output : “sqatools”
"""

input=input("please enter string:")
output=input.lower()
print("lOWER:",output)

"""

# input1 = input("Enter word: ")
# result = ''
# for char in input1:
#     if char.isupper():
#         print(char.lower(),end="")
#     else:
#         print(char,end="")


#
# a=340
# b=330
# print("A") if a>b else print("=") if a==b else print("B")

# 9). Python loops program that accepts a string and calculates the number of digits and letters using python.
# Input : “python1234”
# Output :
# Letters 6
# Digits 4
"""
str=input("please enter string:")

# Take a word as input.
# Create two variables to calculate the number of digits and letters and assign their values equal to 0.
# Use for loop to iterate over each character from the word.
# Check whether the character is a letter or a digit using isaplha() and isnumeric().
# Add 1 to the corresponding variable according to the type of the charater.
# Print the output.

digits=0
letters=0

for char in str:
    if char.isalpha()==True:
        letters=letters+1
    else:
        digits=digits+1
print("Digits in string:",digits)
print("letters in string:",letters)
"""

# 10). Python for loop program to print the alphabet pattern ‘O’ using python.
# Output:
#   ***
# *       *
# *       *
# *       *
# *       *
# *       *
#    ***

"""
for row in range(0, 7):
        for column in range(0, 7):
            # here in first and last row we want to three *
            if (row == 0 or row == 6) and (1 < column < 5) :
                print("*", end=' ')
            # here from 2 to 6 row, * will print on 1 and 5 index only.
            elif (0 < row <= 5) and (column ==1 or column ==5):
                print("*", end=' ')
            else:
                print(" ", end=' ')
        print()

"""

"""
for row in range (0,7):
        for column in range (0,7):
            if (row==0 or row==6) and (1<column<5):
               print("*",end=' ')
            elif (0 < row <= 5) and (column==1 or column==5):
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()

"""

#11). Python Loops program to print all natural numbers from 1 to n using a while loop in python.

"""
n = int(input("Enter the last number: "))
count = 1

while count <= n:
    print(count,end=" ")
    count += 1
"""

# 12). Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.
"""
n=int(input("please enter no:"))

count=n

while count!=0:
    print(count,end=" ")
    count=count-1
"""
"""
n=int(input("please enter no:"))

count=n

while count!=0:
    print(count,end=" ")
    count=count-1
    
"""
#
# 13). Python Loops program to print all alphabets from a to z using for loop
#         Take chr method help to print characters with ASCII values
#         chr(65) = ‘A’
#         A-Z ASCII Range  65-90
#         a-z ASCII Range  97-122
'''
import string

for letter in string.ascii_lowercase:
    print(letter,end=" ")
print("\nalphabet from A-Z:")
for letter in string.ascii_uppercase:
    print(letter,end=" ")
'''
#
# for letter in string.ascii_lowercase:
#
#     print(letter,end=" ")
# print("\n A_Z")
# for letter in string.ascii_uppercase:
#     print(letter,end=' ')

# 14). Python Loops program to print all even numbers between 1 to 100 in python.
'''

for val in range (1,101):
    if val%2==0:
        print(val,end=" ")
'''

# 15). Python Loops program to print all odd numbers between 1 to 100 using python.

'''
for val in range (1,101):
    if val%2!=0:
        print(val,end=' ')
'''



# 16). Python Loops program to find the sum of all natural numbers between 1 to n using python.

"""
n=int(input("please enter n value:"))

total=0
for n in range (1,n+1):
    total=total+n
print(total)
"""





























































































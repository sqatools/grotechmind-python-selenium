
"""
# 1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
# Input1:1500
print("1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).")

for i in range(1500 , 2700):
	if i%7 == 0 and i%5 == 0:
		print(i , end=",")
print()


# 2). Python Loops program to construct the following pattern, using a nested for loops.
print("2). Python Loops program to construct the following pattern, using a nested for loops.")

for i in range(6):
	print(i*" * ")
for i in range(4, -1,-1):
	print(i*" * ")

# 3). Python Loops program that will add the word from the user to the empty string using python.
# Input: “python”
print("3). Python Loops program that will add the word from the user to the empty string using python.")

W1 = input("Enter the word: ")
S1 = " "
for i in range(len(W1)):
	S1 = S1+W1[i]
print(S1)

# 4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
# Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
print("4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.")

Num1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for i in Num1:
	if i%2 == 0:
		even = even+1
	else:
		odd = odd+1
print("Number of even numbers: ",even)
print("Number of odd numbers: ",odd)

# 5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
print("5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.")

for i in range(0,7):
	if i != 3 and i != 6:
		print(i, end=",")

# 6). Write a program to get the Fibonacci series between 0 to 20 using python.
print("6). Write a program to get the Fibonacci series between 0 to 20 using python.")
num1 = 0
num2 = 1
count = 0
while count < 20:
	print(num1,end=",")         # 0,1 , 1, 2, 3, 5, 8, 13 .........
	num1 , num2 = num2 , num1+num2
	count= count+1

# 7). Write a program that iterates the integers from 1 to 30 using python.
# For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
# For numbers that are multiples of both three and five print “FizzBuzz”.

print('''7). Write a program that iterates the integers from 1 to 30 using python. 
For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
For numbers that are multiples of both three and five print “FizzBuzz”.''')

for i in range (1, 31):
	if i%3 == 0 and i%5 ==0:      # 15, 30
		print("FizzBuzz")
	elif i%3 == 0 :               # 3, 6, 9, 12, 18,21, 24,27,
		print("Fizz")
	elif i%5 == 0:                # 5 , 10, 20, 25
		print("Buzz")


# 8). Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python.
# Input : “SqaTOOlS”
print("8). Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python.")

User1 = input("Enter the value: ")
result = " "
for char in User1:
	if char.isupper():
		out1= char.lower()
		print(out1, end="")
	else:
		print(char, end="")


# 9). Python loops program that accepts a string and calculates the number of digits and letters using python.
# Input : “python1234”
print("9). Python loops program that accepts a string and calculates the number of digits and letters using python.")

input = "python12345"
digit = 0
latters = 0

for value in input:
	if value.isalpha():
		latters= latters+1
	elif value.isnumeric():
		digit= digit+1
print("digit: ", digit)
print("latters: ", latters)


# 10). Python for loop program to print the alphabet pattern ‘O’ using python.
print("10). Python for loop program to print the alphabet pattern ‘O’ using python.")

for row in range(0,7):
	for column in range(0,7):
		if (row ==0 or row ==6) and ( 1 <column <5):
			print("*", end="")

		elif (0 < row <= 5) and (column ==1 or column ==5 ):
			print("*", end="")

		else:
			print(" ", end="")
	print()


# 11). Python Loops program to print all natural numbers from 1 to n using a while loop in python.
print("11). Python Loops program to print all natural numbers from 1 to n using a while loop in python.")

n = int(input("Enter the number: "))
m = 1
while m <=n:
	print(m,end=" ")
	m = m+1

# 12). Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.
print("12). Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.")

n1 = int(input("Enter the last number: "))
count = n1
while count !=0:
	print(count, end=" ")
	count = count-1

# 13). Python Loops program to print all alphabets from a to z using for loop
#         Take chr method help to print characters with ASCII values
#         chr(65) = ‘A’
#         A-Z ASCII Range  65-90
#         a-z ASCII Range  97-122
print(''' 13). Python Loops program to print all alphabets from a to z using 
for loop Take chr method help to print characters with ASCII values.''')

import string
print("Alphabet from a-z:")
for latter in string.ascii_lowercase:
	print(latter, end=" ")
print("\nAlphabet from A-Z:")
for latter in string.ascii_uppercase:
	print(latter, end=" ")

# 14). Python Loops program to print all even numbers between 1 to 100 in python.
print("14). Python Loops program to print all even numbers between 1 to 100 in python.")

for i in range(1,101):
	if i%2 ==0:
		print(i, end=" ")

# 15). Python Loops program to print all odd numbers between 1 to 100 using python.
print("15). Python Loops program to print all odd numbers between 1 to 100 using python.")

for odd in range(1,101):
	if odd%2 != 0:
		print(odd,end=" ")


# 16). Python Loops program to find the sum of all natural numbers between 1 to n using python.
print("16). Python Loops program to find the sum of all natural numbers between 1 to n using python.")

N1 = 10 # int(input("Enter the last number: "))
t1 = 0
for i in range(1, N1+1):
	t1 = t1+i
print(t1)

# 17). Python program to find the sum of all even numbers between 1 to n using python.
print("17). Python program to find the sum of all even numbers between 1 to n using python.")
n = int(input("Enter the number: "))
number = 0
for i in range(1, n+1):
	if i%2 == 0:         # 2,4,6,8,10
		number = number+i
		print(number, end=" ")
print()
print(number)


# 18). Python Loops program to find the sum of all odd numbers between 1 to n using python.
print("18). Python Loops program to find the sum of all odd numbers between 1 to n using python.")
n1 = int(input("Enter the number: "))
numbr = 0
for i in range(1,n1+1):
	if i%2 != 0:
		numbr = numbr+i
		print(numbr, end=" ")
print()
print(numbr)


# 19). Write a program to count the number of digits in a number using python.
print("19). Write a program to count the number of digits in a number using python.")

num = "12345678910"
count = 0
for i in num:
	count= count+1
print(f"Total digits in {num}: ",count, end=" ")

# 20). Write a program to find the first and last digits of a number using python.
print("20). Write a program to find the first and last digits of a number using python.")

num1 = 2345
str1 = str(num1)
print(len(str1))
for i in range(len(str1)):
	if i == 0:
		print("First number in the gievn number: ",str1[i])
	elif i == len(str1)-1:
		print("Last number in the gievn number : ",str1[i])

# 21). Write a program to find the sum of the first and last digits of a number using python.
print("21). Write a program to find the sum of the first and last digits of a number using python.")

num1 = "2345"
#num1 = str(num)
numbr1 = 0
for i in range(len(num1)):
	if i == 0:
		numbr1 = numbr1+ int(num1[i])    # 0+2 = 2
	elif i == len(num1)-1:
		numbr1=numbr1+ int(num1[i])
print(numbr1)


# 22). Write a program to calculate the sum of digits of a number using python.
print("22). Write a program to calculate the sum of digits of a number using python.")

num1 = 2345
number1 = 0
while num1 > 0:
	count = num1 % 10				   # 5,4,3,2
	print("count:",count,",",end=" ")
	number1 = number1+count            # 0+5= 5, 5+4=9, 9+3=12, 12+2=14
	print("number1: ",number1)
	num1= num1//10                     # 234 , 23, 2, 0
	print(num1)
print("Sum of digits of a number: ", number1)

# 23). Write a program to calculate the product of digits of a number using python.
print("23). Write a program to calculate the product of digits of a number using python.")

num = int(input("Enter a number: "))
product = 1
while num > 0:
	rem = num % 10
	print(rem, end=" & ")            # 6 , 5
	product = product * rem
	print( product, end=" $ ")        # 6, 30
	num = num // 10
	print(num, end=" * ")          # 5 , 0
print("\n Product of given number is: ",product)

"""




















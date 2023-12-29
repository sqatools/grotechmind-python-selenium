
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

"""
# 6). Write a program to get the Fibonacci series between 0 to 20 using python.
print("6). Write a program to get the Fibonacci series between 0 to 20 using python.")








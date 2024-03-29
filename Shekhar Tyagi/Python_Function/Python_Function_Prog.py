

# 1). Python function program to add two numbers.
print("1). Python function program to add two numbers.")

def add(a,b):
	total = a+b
	print("Total:" , total)
inp1= 5   #int(input("Enter The num1: "))
inp2= 6  #int(input("Enter The num2: "))
add(inp1, inp2)

# or $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def add(a, b):
	return a + b

inp1 = 5
inp2 = 7

result = add(inp1, inp2)
print(f"The sum of {inp1} and {inp2} is: {result}")

# 2). Python function program to print the input string 10 times.
print("2). Python function program to print the input string 10 times.")

def str(str1):
	result = str1*10
	print("Result:",result)
inp1 = "Shekhar Tyagi "
str(inp1)

# or

def str(str1):
	return str1*10
Result = str("Shekhar Tyagi ")
print("Result:", Result)

# 3). Python function program to print a table of a given number.
print("3). Python function program to print a table of a given number.")

def table(num):
	total = 0
	for val in range(1, 11):
		total = val*num
		print("Table :" , val ,"*", num ,":", total)

inp1 = 6 #int(input("Enter the num: "))
table(inp1)

# 4). Python function program to find the maximum of three numbers.
print("4). Python function program to find the maximum of three numbers.")
Input: (17,21, -9)

def large(val1 , val2 , val3):
	if val1 >val2:
		if val1 > val3:
			print(f"{val1} is the greatest number")
	elif val2 > val1:
		if val2 > val3:
			print(f"{val2} is the greatest number")
	else:
		print(f"{val3} is the greatest number")
large(10,12,9)

# 5). Python function program to find the sum of all the numbers in a list.
print("5). Python function program to find the sum of all the numbers in a list.")

Input : [6,9,4,5,3]

def sum(list1):
	num = 0
	for val in list1:
		num = num+val
	print("Sum:", num)
inp1 = [6,9,4,5,3]
sum(inp1)

# 6). Python function program to multiply all the numbers in a list.
print("6). Python function program to multiply all the numbers in a list.")

Input : [-8, 6, 1, 9, 2]
def multi(lis1):
	num = 1
	for val in lis1:
		num = num * val
	print("Multi:", num)
inp1 = [-8, 6, 1, 9, 2]
multi(inp1)

# 7). Python function program to reverse a string.
print("7). Python function program to reverse a string.")

#Input: Python1234

def rev(str):
	char = str[::-1]
	print("Rev:", char)
inp1 = "Python1234"
rev(inp1)

# 8). Python function program to check whether a number is in a given range.
print("8). Python function program to check whether a number is in a given range.")

# Input : num = 7, range = 2 to 20
def check_range(num):
	if num in range(2,20):
		print(f"{inp1} is in range.")
	else:
		print(f"{inp1} is not in range.")
inp1 = 8             #int(input("Enter the num:"))
check_range(inp1)

# 9). Python function program that takes a list and returns a new list with unique elements of the first list.
print("9). Python function program that takes a list and returns a new list with unique elements of the first list.")

# Input : [2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
def unique_ele(list1):
	result = list(set(inp1))
	print("Unique_element: ", result)
inp1 = [2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
unique_ele(inp1)

# 10). Python function program that take a number as a parameter and checks whether the number is prime or not.
print("10). Python function program that take a number as a parameter and checks whether the number is prime or not.")

# Input : 7
def prime(num):
	count = 0
	for val in range(2, num):
		if num%val ==0:
			count= count+1
	if count > 0:
		print(f"{inp1} is not a prime number.")
	else:
		print(f"{inp1} is a prime number.")
inp1 = 11    #int(input("enter the num:"))
prime(inp1)


# 11). Python function program to find the even numbers from a given list.
print("11). Python function program to find the even numbers from a given list.")

# Input : [1, 2, 3, 4, 5, 6, 7, 8, 9]
def even(list1):
	list2 = []
	for val in list1:
		if val%2 ==0:
			list2.append(val)
	print("even num:", list2)
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even(list1)

# 12). Python function program to create and print a list where the values are squares of numbers between 1 to 10.
print("12). Python function program to create and print a list where the values are squares of numbers between 1 to 10.")

# Input: 1 to 10

def square(list1):
	for val in range(1, list1+1):
		result = val ** 2
		print(val ,result )
inp1 = 10
square(inp1)

# 13). Python function program to execute a string containing Python code.
print("13). Python function program to execute a string containing Python code.")

mycode = 'print("Python")'
code = '''

def mutiply(x,y):
	return x*y
result = int(2*3)
print('sqatools')
print(result)

'''
exec(mycode)
exec(code)

# 14). Python function program to access a function inside a function.
print("14). Python function program to access a function inside a function.")

def outer(a):
	def inner(b):
		result = a+b
		print("Result:", result)
	inner(20)
outer(10)

# or

def outer():
	print("It is a outer function")
	def inner():
		print("It is a inner function")
	inner()
outer()

# 15). Python function program to find the LCM of two numbers.
print("15). Python function program to find the LCM of two numbers.")

# Input: 12, 20

def lcm(num1 , num2):
	if num1 > num2:
		result = num1
	else:
		result = num2
	while(True):
		if ((result%num1==0) and (result%num2==0)):
			lcm = result
			break
		result = result+1
	print(f"lcm of {num1} and {num2}: {lcm}")
num1 = 22
num2 = 20
lcm(num1, num2)

# 16). Python function program to calculate the sum of numbers from 0 to 10.
print("16). Python function program to calculate the sum of numbers from 0 to 10.")

def sum():
	val = 0
	for ele in range(0,11):
		val = val+ele
	print("Sum:",val)
sum()

# 17). Python function program to find the HCF of two numbers.
print("17). Python function program to find the HCF of two numbers.")

# Input: 24 , 54
def hcf(num1 , num2):
	if num1 > num2:
		result = num2
	else:
		result = num1
	for i in range(1, result+1):
		if ((num1 % i ==0 ) and (num2%i ==0)):
			hcf = i
	print(f"hcf of {num1} and {num2}: {hcf}")
num1 = 24
num2 = 54
hcf(num1, num2)

# 18). Python function program to create a function with *args as parameters.
print("18). Python function program to create a function with *args as parameters.")

# Input: 5, 6, 8, 7

def func(*args):
	for num in args:
		result = num**3
		print("Result : " , result, end=", ")
func(5,6,8,7)

# 19). Python function program to get the factorial of a given number.
print("19). Python function program to get the factorial of a given number.")

# Input: 5
def fact(num):
	fact = 1
	while num >0 :
		fact= fact * num
		num = num -1
		print(f"Factorial of {inp1}: {fact}" )
inp1 = 5
fact(inp1)

# 20). Python function program to get the Fibonacci series up to the given number.
print("20). Python function program to get the Fibonacci series up to the given number.")

# Input: 10
def fibo():
	num1 = 0
	num2 = 1
	count = 0
	while count < 10:
		print(num1, end=", ") # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
		num1, num2 = num2, num1 + num2
		count = count +1   # 1,2,3,4,5,6,7,8,9
fibo()

print()

# 21). Python function program to check whether a combination of two numbers has a sum of 10 from the given list.
print("21). Python function program to check whether a combination of two numbers has a sum of 10 from the given list.")

# Input : [2, 5, 6, 4, 7, 3, 8, 9, 1]
def check_sum(num):
	for i in range(len(num)): # 0 1 2 3 4 5 6 7 8
		for j in range( i+1, len(num)):
			if num[i] +num[j] ==10:
				return  True
	return False

list1 = [2, 5, 6, 4, 7, 3, 8, 9, 1]
result= check_sum(list1)
print(result)

# 22). Python function program to get unique values from the given list.
print("22). Python function program to get unique values from the given list.")

# Input : [4, 6, 1, 7, 6, 1, 5]

def unique_val(list1):
	list2 = []
	for val in list1:
		if val not in list2:
			list2.append(val)
	print(sorted(list2))
num = [4, 6, 1, 7, 6, 1, 5]
unique_val(num)

# or
print("%"*50)
def unique(num):
	result = set(num)
	print(list(result))
inp = [4, 6, 1, 7, 6, 1, 5]
unique(inp)

# 23). Python function program to get the duplicate characters from the string.
print("23). Python function program to get the duplicate characters from the string.")

# Input: Programming
def unique_char(string):
	list1 =""
	for char in string:
		if string.count(char) >1:
			list1 = list1+char
			#list1.append(char)
	print(set(list1))
inp = 'Programming'
unique_char(inp)

# 24). Python function program to get the square of all values in the given dictionary.
print("24). Python function program to get the square of all values in the given dictionary.")

# Input = {‘a’: 4, ‘b’ :3, ‘c’ : 12, ‘d’: 6}

def square(val):
	dict1 = {}
	for key,value in val.items():
		dict1[key] = value**2
	return dict1
item = {'a': 4, 'b' :3, 'c' : 12, 'd': 6}
#result= square(item)
print(square(item))

# or

def square(val):
	dict1 = {}
	for key,value in val.items():
		dict1[key] = value**2
	print(dict1)
item = {'a': 4, 'b' :3, 'c' : 12, 'd': 6}
square(item)

# 25). Python function program to print a list of prime numbers from 1 to 100.
print("26). Python function program to print a list of prime numbers from 1 to 100.")

def prime(lower , upper):

	for num in range(lower , upper+1):
		count = 0
		for i in range(1, num + 1):
			if num%i == 0:
				count = count+1
		if count ==2 :
			print(i, end=" ")
prime(1, 100)

# 27). Python function program to get a list of odd numbers from 1 to 100.
print("27). Python function program to get a list of odd numbers from 1 to 100.")

def odd_even(min_num , max_num):
	even = []
	odd = []
	for num in range(min_num, max_num+1):
		if num % 2 ==0:
			even.append(num)
		else:
			odd.append(num)
	print("Even:", even)
	print("Odd:",odd)
odd_even(1, 100)













































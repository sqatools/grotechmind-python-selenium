# 1). Python Program to add two integer values.
print("1). Python Program to add two integer values.")

x = 10
y = 20
z = x + y
print(z)

print("-" * 50)

# 2). Python Program to subtract two integer values.
print(" 2). Python Program to subtract two integer values.")
x = 30
y = 20
print(x - y)

print("-" * 50)
# 3) python program to multiply two numbers.
print("3) Python program to multiply two numbers")
x = 3
y = 4

print(x * y)

print("-" * 50)
# 4) Python program to repeat a given string 5 times.

print("Hello" * 5)

print("-" * 50)
# 5). Python program to get the Average of given numbers.

x = 4
y = 5
z = 8
a = x + y + z
print("Average :", a / 3)

"""6). Python program to get the median of given numbers.
Note: all the numbers should be arranged in ascending order
Formula : (n+1)/2
n = Number of values"""

print("-"*50)
print("6). Python program to get the median of given numbers.")
list1 = [45,50,70,90,140,108,130]
list1.sort()
print(list1)
a = (len(list1))/2
print("Median :",list1[int(a)])

#7). Python program to print the square and cube of a given number.
print("-"*50)
print("enter the number")
a=int(input())
print(a**2)
print(a**3)
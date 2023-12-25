# 1). Python program to check given number is divided by 3 or not.

print("1). Python program to check given number is divided by 3 or not.")
num1 = 12 #int(input("enter the value: "))
if num1%3 == 0:
	print(f"{num1} is a divisible by 3," )
else:
	print(f"{num1} is not a divisible by 3,")

# 2). If else program to get all the numbers divided by 3 from 1 to 30.
print("2). If else program to get all the numbers divided by 3 from 1 to 30.")

for i in range (1,31):
	if i%3 == 0:
		print(i ,end=" ")

print()


"""
3). If else program to assign grades as per total marks.
marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks
"""

print("3). If else program to assign grades as per total marks.")
marks = 79 #int(input("enter the value : "))
if marks<40:
	print("marks: " , marks , ", Failed")

elif marks>=40 and marks <=50:
	print("marks : " , marks , ", Grade C")

elif marks >=50 and marks <= 60:
	print("marks: ", marks , ", Grade B")
elif marks >=60 and marks <=70:
	print("marks: ", marks , ", Grade A")
elif marks >=70 and marks <=80:
	print("marks: ", marks, ", Grade A+")
elif marks >=80 and marks <=90:
	print("marks: ", marks, ", Grade A++")
elif marks >=90 and marks <=100:
	print("marks:",marks, "Grade Excellent")
else:
	print("marks: ", marks, ": Invalid marks")

# 4). Python program to check the given number divided by 3 and 5.
print("4). Python program to check the given number divided by 3 and 5.")

num1 = 15 #int(input("enter the num: "))
if num1%3==0 and num1%5 == 0:
	print(f"{num1} is divisable  by 3 and 5: ",num1)
else:
	print(f"{num1} is not divisable by 3 and 5")


# 5). Python program to print the square of the number if it is divided by 11.
print("5). Python program to print the square of the number if it is divided by 11.")

num =  22 #int(input("Enter a number: "))
if num%11 == 0:
	print(num**2)
else:
	print(f"{num} is not divisable by 11")

# 6). Python program to check given number is a prime number or not.
print("6). Python program to check given number is a prime number or not.")

num = 11 # int(input("enter the value: "))
count = 0
for i in range (2 , num):
	if num%i == 0:
		count=count+1
if count > 0:
	print(f"{num} is not a prime number")
else:
	print(f"{num} is a prime number")

# 7). Python program to check given number is odd or even.
print("7). Python program to check given number is odd or even.")

num = int(input("enter the number:"))
if num%2 == 0:
	print(f"{num} is a even number")
else:
	print("num: " ,f"{num} is odd number")

# 8). Python program to check a given number is part of the Fibonacci series from 1 to 10.
print("8). Python program to check a given number is part of the Fibonacci series from 1 to 10.")




















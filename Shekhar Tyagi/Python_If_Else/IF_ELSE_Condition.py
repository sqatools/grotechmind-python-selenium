"""
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


""""""
3). If else program to assign grades as per total marks.
marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks
""""""

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

num =   97   # int(input("enter the number:"))
if num%2 == 0:
	print(f"{num} is a even number")
else:
	print("num: " ,f"{num} is odd number")

# 8). Python program to check a given number is part of the Fibonacci series from 1 to 10.
print("8). Python program to check a given number is part of the Fibonacci series from 1 to 10.")

""""""
f1=0
f2=1
for i in range(10):
	print(f2 ,end=",")
	f1,f2 = f2,f1+f2

print()
""""""

f1 = [1, 1, 2, 3, 5, 8, 13, 21, 34,55]

f_num=  21 #int(input("enter the numver: "))
if f_num in f1:
	print(f"{f_num} is available in f1 list")
else:
	print(f"{f_num} is not available in f1 list")

# 9). Python program to check authentication with the given username and password.
print("9). Python program to check authentication with the given username and password.")

name = "shekhar tyagi"  # input("Enter the User_Name: ")
Pass = "shekhar tyagi"  # input("Enter the Password: ")
if name == Pass:
	print("User Name & Pass is Valied")
else:
	print("User Name & Pass is not valied")

# 10). Python program to validate user_id in the list of user_ids.
print("10). Python program to validate user_id in the list of user_ids.")

user_ids = [1,2,3,4,5,6,7,8,9,10,"shekhartyagi112"]
user_id =   4 #int(input("Enter the user_id: ")) #input("Enter the user_id: ")
if user_id in user_ids:
	print("It is valied user_id")
else:
	print("It is not a valied user_id")

# 11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
print("11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.")

num =  15   #int(input("Enter the value: "))
if num%2==0:
	print("it is Squar")
elif num%3 ==0:
	print("it is a cube")
else:
	print("it is not aplicable")

# 12). Python program to describe the interview process.
print("12). Python program to describe the interview process.")

R1 = input("Enter the value: ")
R2 = input("Enter the value: ")

if R1== "passed":
	print(f"Congrats, you have cleared 1st Round.")
	if R2 =="passed":
		print("Congrats, You have cleared 2nd round, You are placed.")
	else:
		print("Failed in 2nd round, please try again next time")
else:
	print("Failed in 1st round, please try again next time")


# 13). Python program to determine whether a given number is available in the list of numbers or not.
print("13). Python program to determine whether a given number is available in the list of numbers or not.")

L1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21.22,23,24,25,26,27,28,29,30]
User1 = int(input("Enter the value: "))
if User1 in L1:
	print(f"{User1} is available in the list.")
else:
	print(f"{User1} is not available in the list.")


# 14). Python program to find the largest number among three numbers.
print("14). Python program to find the largest number among three numbers.")

U1 = int(input("Enter the value of U1: "))
U2 = int(input("Enter the value of U2: "))
U3 = int(input("Enter the value of U3: "))
if U1 > U2:
	if U1 > U3:
		print(f"{U1} is largest value in among three numbers.")
	else:
		print(f"{U3} is largest value in among three numbers.")
else:
	if U2 > U3:
		print(f"{U2} is largest value in among three numbers.")
	else:
		print(f"{U3} is largest value in among three numbers.")


# 15). Python program to check any person eligible to vote or not
print("15). Python program to check any person eligible to vote or not")

Voter = int(input("Enter the age of voter: "))
if Voter >= 18:
	print("Voter is eligible for Vote.")
else:
	print("Voter is not eligible for Vote.")


# 16). Python program to check whether any given number is a palindrome.
print("16). Python program to check whether any given number is a palindrome.")

num_1 = 121
num_2 = str(num_1)
if num_1 == int(num_2[::-1]):
	print("Number is palindrome")
else:
	print("Number is not palindrome")


# 17). Python program to check if any given string is palindrome or not.
# Input: ‘jaj’
print("17). Python program to check if any given string is palindrome or not.")
I_1 = "jaj"
if I_1 == I_1[::-1]:
	print("It is palindrome")
else:
	print("It is not palindrome")

# 18). Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.
# Input = Enter marks: 45
print("18). Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.")

marks = int(input("Enter the marks: "))
if marks >= 45:
	print("Student is passed")
else:
	print("Student is failed")

# 19). Python program to check whether the given number is positive or not.
# Input = 20
print("19). Python program to check whether the given number is positive or not.")

N_1 = int(input("Enter the number: "))
if N_1> 0:
	print(f"{N_1} is positive value")
else:
	print(f"{N_1} is not a positive value")


# 20). Python program to check whether the given number is negative or not.
# Input = -45
print("20). Python program to check whether the given number is negative or not.")

N_2 = int(input("Enter the number: "))
if N_2 < 0:
	print(f"{N_2} is a Negative value")
else:
	print(f"{N_2} is a Positive value")


# 21). Python program to check whether the given number is positive or negative and even or odd.
# Input = 26
print("21). Python program to check whether the given number is positive or negative and even or odd.")

N3 = int(input("Enter the number: "))
if N3 > 0:
	if N3 % 2 == 0:
		print(f"{N3} is positive & Even number.")
	else:
		print(f"{N3} is positive & Odd number.")
else:
	if N3 % 2 == 0:
		print(f"{N3} is Negative & Even number.")
	else:
		print(f"{N3} is Negative & Odd number.")



# 22). Python program to print the largest number from two numbers.
# Input: 25, 63
print("22). Python program to print the largest number from two numbers.")

I_1 = 25
I_2 = 63

if I_1 > I_2:
	print(f"{I_1} is largest number from two numbers.")
else:
	print(f"{I_2} is largest number from two numbers.")


# 23). Python program to check whether a given character is uppercase or not.
# Input = A
print("23). Python program to check whether a given character is uppercase or not.")

Inp_1 = input("Enter the Char: ")

if Inp_1.isupper():
	print(f"{Inp_1} is in uppercase.")
else:
	print(f"{Inp_1} is in lowercase.")

# 24). Python program to check whether the given character is lowercase or not.
# Input = c
print("24). Python program to check whether the given character is lowercase or not.")

Inp_2 = input("Enter the Char: ")
if Inp_2.islower():
	print(f"{Inp_2} is in lowercase.")
else:
	print(f"{Inp_2} is in Uppercase.")

# 25). Python program to check whether the given number is an integer or not.
# Input = 54
print("25). Python program to check whether the given number is an integer or not.")

Inp_3 = 54
if type(Inp_3) == int:
	print(f"{Inp_3} is integer number.")
else:
	print(f"{Inp_3} is not integer number.")

# 26). Python program to check whether the given number is float or not.
# Input = 12.6
print("26). Python program to check whether the given number is float or not.")

Inp_4 = 12.6

if type(Inp_4) == float:
	print("True")
else:
	print("False")


# 27). Python program to check whether the given input is a string or not.
# Input = ‘sqatools’
print("27). Python program to check whether the given input is a string or not.")

Inp_4 = "Shekhar Tyagi"
if type(Inp_4) == str:
	print("True")
else:
	print("False")

# 28). Python program to print all the numbers from 10-15 except 13.
print("28). Python program to print all the numbers from 10-15 except 13")


for i in range(10, 16):
	if i != 13:
		print(i)

# 29). Python program to find the electricity bill. According to the following conditions:
# Up to 50 units rs 0.50/unit
# Up to 100 units rs 0.75/unit
# Up to 250 units rs 1.25/unit
# above 250 rs 1.50/unit
# an additional surcharge of 17% is added to the bill
# Input = 350
print("29). Python program to find the electricity bill. According to the following conditions:")

u1 = int(input("Enter the Units: "))
Bill_Amount = 0

for Bill_Unit in range (1 , u1+1):
	if Bill_Unit <= 50:
		Bill_Amount = Bill_Amount+0.50
	elif Bill_Unit >50 and Bill_Amount <= 100:
		Bill_Amount = Bill_Amount+0.75
	elif Bill_Unit >100 and Bill_Amount <=250:
		Bill_Amount = Bill_Amount + 1.25
	elif Bill_Unit >250:
		Bill_Amount = Bill_Amount + 1.50
Bill_Amount_surcharge = Bill_Amount + Bill_Amount * (17/100)
print("Total Bill amount with 17% surcharge: " , Bill_Amount_surcharge)


# 30). Python program to check whether a given year is a leap or not.
# Input = 2000
print("30). Python program to check whether a given year is a leap or not.")

y1 = int(input("Enter the year: "))
if (y1%100 != 0 or y1%400 == 0) and y1%4 == 0:
	print("It is a leap year")
else:
	print("It is not a leap year")

"""





































































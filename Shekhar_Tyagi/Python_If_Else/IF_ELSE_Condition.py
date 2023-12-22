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
marks = int(input("enter the value : "))
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






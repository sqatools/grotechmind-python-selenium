
"""

*
**
***
****
*****

"""
"""
for i in range ( 1,6):
    print()
    for j in range (i):
        print(j , end=" ")
print()
print("_"*39)

num = 1
while num <=15:
    if num >5 and num <8:
        num = num+1
        break
    print(num)
    num = num+1


print("_"*50)

num = 6
fact = 1
for i in range (num , 0 ,-1):
    print(i)
    fact = fact*i
    print("fact:",fact)

print("@@@@@@@@@@@@@@@@@@@@@@@@")

a = 0
b = 1

for i in range (10):
    print(b, end=" ")
    a,b = b, a+b


print()


print("__"*40)

num = 11
prime = True
for i in range (2, num):
    if num%i==0:
        prime = False
if prime:
    print("This is prime value:" ,num)
else:
    print("this is not prime value:",num)


# Python program to check given number is palindrome or not.              (Note:)

n = num = 121    #int(input("Enter the value: "))         # n = num = 121
R1 = 0                                            # R1 = 0
while n>0:                                        # 121 > 0
    r1 = n%10                                     # r1 = 1
    R1 = R1*10 + r1                               # R1 = 1
    n = n//10                                     # n  = 12
if num == R1:                                     # 121 == 1
    print(" it is a palindrome ")
else:
    print(" it is not a palindrome")



stra= "python programming"
f_val = stra[:6]
print(stra + " " + f_val)



print("$"*20)

stra = "python programming"

a="0"
print(a.isnumeric())
print(a.isdigit())


strng = "Learning Python Programing"
str1 = strng.split(" ")
output1 = { }
for val in str1:
	first_char = val[0]
	seccond_char = val[-1]
	result = first_char+seccond_char
	output1[result] =val
print(output1)


strng = "Learning Python Programing"
str1 = strng.split(" ")
output1 = { }
for val in str1:
	first_char = val[0]
	seccond_char = val[-1]
	result = first_char + seccond_char
	rev_word = val[::-1]
	output1[result] = rev_word
print(output1)


def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

def main():
    for num in range(1, 16):
        print(fizz_buzz(num))

if __name__ == "__main__":
    main()

if __name__ == '__main__':
	n = 24
if n%2 or 6 <= n <= 20:
    print('Weird')
else:
    print('Not Weird')

n = int(input("Enter the num: "))
if n % 2==0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")


# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10]
# list3 =list1+list2
# print(list3)
#
# list1 = [1,2,3,4]
# list1.insert(4,(5,6,7,8))
# list1.insert(5,[9,10])
# list1.insert(12,{'name': "shekhar tyagi"})
#
# print(list1)

# listd =  [4, 6, 8, 22, 14]
# listd.insert(2, 500)
# print("listd :", listd)
# # [4, 6, 500, 8, 22, 14]
# listd.insert(3, (4, 7, 8))
# listd.insert(4, [6, 8, 9])
# listd.insert(-1, {'name': 'rahul', 'age': 25})
# print("listd :", listd)

string1 = "Hello World"

result = " "

for i in string1:
	if 'A'<= i <= 'Z':
		result= result+ chr(ord(i)+32)

	elif 'a' <= i <='z':
		result= result+chr(ord(i)-32)
	else:
		result=result + i
print(result)


string1 = "Hello World"
char = string1.split()
result = " "

for i in char:
	if i.isupper():
		result = result+ i.lower()
	elif i.islower():
		result = result + i.upper()
	else:
		result = result + i

print(result)

"""

# Create a class structure for a IT Company.
# Create a class structure for a school Institute.



class ITCompany:
    def __init__(self, company_name):
        self.company_name = company_name
        #self.departments = []

    # def add_department(self, department):
    #     self.departments.append(department)

    def display_info(self):
        print(f"Company Name: {self.company_name}")
        # print("Departments:")
        # for department in self.departments:
        #     department.display_info()
if __name__ == "__main__":
	it_company = ITCompany("GrowTechMind")
	it_company.display_info()




print("&"*40)

def func(*args):
	for num in args:
		result = num**3
		print("Result : " , result)
func(5,6,8,7)
print("%"*40)

try:
	num1 = 40
	num2 = 20

	result = num1 / num2

	if result >= 0:
		print("Result is positive or zero:", result)
	else:
		print("Result is negative:", result)

except ZeroDivisionError:
	print("Error: Division by zero!")
except ValueError:
	print("Error: Please enter valid numbers!")
except Exception as e:
	print("An unexpected error occurred:", e)





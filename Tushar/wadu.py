#1). Python program to check given number is divided by 3 or not.
"""
num=int(input("please enter no:"))

if num%3==0:
    print("num is divided by 3")
else:
    print("num is not divided by 3")

  """
#2). If else program to get all the numbers divided by 3 from 1 to 30.


# for i in range (1,31):
#     if i%3==0:
#         print(i,end=" ")

# 4). Python program to check the given number divided by 3 and 5.

# num=int(input("please enter no:"))
#
# if num%3==0 and num%5==0:
#     print("num is divided by 3 and 5")
# else:
#     print("num is not divided by 3 and 5")


# 6). Python program to check given number is a prime number or not.


# num=int(input("please enter no:"))
#
# prime=True
#
# for i in range (2,num):
#     if num%i==0:
#
#         prime=False
#
#
#         print("prime",num)
#
#     else:
#
#
#         print("not prime",num)
#

# num1=int(input("please enter no:"))
# prime=True
# for i in range (2,num1):  ###num1//2   11: 2 3 4 5 6 7 8 9 10
#     #print("i:",i)
#     if num1%i==0:
#         prime= False
#         #break
# if prime:
#     print("This is prime number:",num1)
# else:
#     print("This is not prime number:",num1)
#
# print("+"*50)




# num=int(input("please enter no:"))

# for i in range (2,num): #11:2 3 4 5 6 7 8 9 10
#     if num%i==0:
#         print("not prime")
#         break
# else:
#     print("prime"

# for num in range (1,100):
#     prime= True
#     for i in range (2,num):
#         if num%i==0:
#             prime=False
#     if prime:
#         print("this is prime no:",num)
#     else:
#             print("This is not Prime no:",num)


 # a b c
# 0,1,1 ,2, 3,5,8,13,21
#    a b c
# 8). Python program to check a given number is part of the Fibonacci series from 1 to 10.

# a=0
# b=1
#
# for num in range (2,11):
#     c=a+b
#     b=a
#     print(c)


# a=0
# b=1
#
# for i in range (2,11):
#
#     c=a+b
#     a=b
#     b=c
#     print(c)


#9). Python program to check authentication with the given username and password.
#
# username=input("enter user name:")
# password=int(input("enter password:"))
#
# x="tushar"
# y=12345
# if username==x and password==y:
#     print("valid user")
# else:
#     print("invalid user")


#13). Python program to determine whether a given number is available in the list of numbers or not.

user_input=int(input("please enter no:"))

lst=[1,2,3,4,5]

if user_input  not in lst:
    print("number is not available in list")
else:
    print("num is  available in list")



#
# 14). Python program to find the largest number among three numbers.



# num1=int(input("please enter first no:"))
# num2=int(input("please enter second no:"))
# num3=int(input("please enter third no:"))
#
#
#
# if num1>num2 and num1>num3:
#     print("num1 is greter")
# elif num2>num1 and num2>num3:
#     print("num2 is greter")
# else:
#     print("num3 is greater")


# 16). Python program to check whether any given number is a palindrome.
# Input: 121
# Output: palindrome

# num1=int(input("please enter no:"))  #int
# num2=str(num1) #str
# if num1==int(num2[: : -1]): #str indexing covert int
#     print("palindrome")
# else:
#     print("not palindrome")


#1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included).
# Input1:1500
# Input2:2700

# for num in range (1,100):
#     if num%7==0 and num%5==0:
#         print(num,"num is div by 7 and mul by 5")
#     # else:
#     #     print(num,"num is not div by 7 and mul by 5")
#
#
#
#
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


#
# for i in range (1,6):
#     #for j in range (1,6):
#         if i==i+1:
#             print("*")


for i in range(6):
    print(i*"*")
for i in range(4,0,-1): #4 3 2 1
    print(i*"*")


print("*"*40)

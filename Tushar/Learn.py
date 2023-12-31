
"""
a=2
b=3
print("additino of a and b:",a+b)
"""
'''
a=int(input("please enter first no:"))
b=int(input("please enter second no"))

print("additino of a and b:",a+b)
'''

# a=int(input("please enter first no:"))
# b=int(input("please enter second no"))

# num1=200
# num2=245881566772
# num3='c'
# print(type(num1),type(num2),type(num3))
#
# print(num1 + num2)

# list=[1,2,3,4]
# list[2]=100
# print (list)
#
# a=int(input("please enter first no:"))
#
# b=int(input("please enter second no:"))
#
# if a>=10:
#     print(a+b)
# else:
#     print(a*b)



# 1). Python program to check given number is divided by 3 or not.

# a=int(input("please enter first no:"))
# b=a%3
# if b==0:
#     print('number is devided by 3')
# else:
#     print('number is not devided by 3')




# 4). Python program to check the given number divided by 3 and 5.
#
# a=int(input("please enter first no:"))
#
# if a%3==0 and a%5==0:
#     print("num is divided by 3 and 5")
# else:
#     print("num is not divided by 3 and 5")


# 6). Python program to check given number is a prime number or not.


num =  int(input("Enter a number: "))

count = 0

for i in range(2,num):

    if num%i == 0:

        count += 1

if count > 0:

    print("It is not a prime number")
else:

    print("It is a prime number")





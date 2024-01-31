# num=int(input("x"))
#
# for i in range(2,num):
#     if num%i==0:
#         print(num,"is not prime number")
#         break
# else:
#     print(num,"is prime number")
#
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


#-------How many prime number in 100

# num=100
# ##  prime number :2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,79, 83, 89, 97.
#
# for i in range(2,num):
#     if num%i==0:
#         print(num,"is not prime number")
#         break
# else:
#     print(num,"is prime number")

num1=int(input("please enter first no:"))
num2=int(input("please enter second no:"))
num3=int(input("please enter third no:"))
if num1>num2 and num1>num3:
    print("num1 is greter")
elif num2>num1 and num2>num3:
    print("num2 is greter")
else:
    print("num3 is large")








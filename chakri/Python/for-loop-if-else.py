#1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
'''Input1:1500
Input2:2700
for i in range(1500,2701):
        if i%7 == 0 and i%5 == 0:
            print(i, end=" ")

#3). Python Loops program that will add the word from the user to the empty string using python.
word = input("Enter the word: ")
str1 = ""
for i in range(len(word)):
    str1 += word[i]
print(str1)

#4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for val in numbers:
    if val%2 == 0:
        even += 1
    else:
        odd += 1
print(even)
print(odd)


#5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
for i in range(0,6):
    if i != 3 and i != 3:
     print(i)

#7). Write a program that iterates the integers from 1 to 30 using python. For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
#For numbers that are multiples of both three and five print “FizzBuzz”.
for i in range(1,31):
    if i%3 == 0 and i%5 == 0 :
        print('fizzbuzz')
    elif i%3 == 0 :
        print('fizz')
    elif i%5 == 0 :
        print('buzz')


for i in range(6):
    print(i*'*')
for i in range(4,0,-1):
    print(i*'*')

num = 2
fact = 1
for i in range(num, 7, 1):
    fact = fact*i
    print("fact :", fact)


a = 0
b = 1
for _ in range(10):
    print(b, end=" ")
    a ,b = b,a+b

even = 0
odd = 0
for i in range(1,10):
    if i%2 == 0:
        even = even+i
    else:
        odd = odd+i
print('sum of even numbers:',even)
print('sum of odd number:',odd)



#8). Write program that accepts a word from the user and converts all uppercases in the word to lowercase using python.
input1 = input('enter any text to covert to lower case :')
for char in input1:
    if char.isupper():
        print(char.lower(),end='')
    else:
        print(char,end='')



#9). Python loops program that accepts a string and calculates the number of digits and letters using python.
a = input('enter to know how many number and alphabets in input:')
ls = 0
ds = 0
for i in a:
    if i.isalpha():
        ls = ls + 1
    if i.isnumeric():
        ds = ds + 1
print('latters',ls)
print('digits', ds)



#11). Python Loops program to print all natural numbers from 1 to n using a while loop in python.
n = int(input('enter any number:'))
count = 1
while count <= n:
    print(count,end=' ')
    count = count+1

#12). Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python
n = int(input('enter any number :'))
for i in range(n,0,-1):
    print(i,end='  ')


#13). Python Loops program to print all alphabets from a to z using for loop
#       Take chr method help to print characters with ASCII values
#      chr(65) = ‘A’
#     A-Z ASCII Range  65-90
#    a-z ASCII Range  97-122
import string
print("a - z alphabets lower case")
for letters in string.ascii_lowercase:
    print(letters, end='  ')
print('-'*50)
print("A - Z alphabets upper case :")
for letters in string.ascii_uppercase:
    print(letters, end='  ')


#14). Python Loops program to print all even numbers between 1 to 100 in python.
for i in range(2,101,2):
    print(i,end=' ')

for i in range(1,10):
    print('chakri i:',i)
    for s in range(1,5):
        print('sainath s :',s)
    print('-'*20)

for i in range(1,6):
    print()
    for j in range(i):
        print('*',end=' ')

num = 1
while num <= 10:
    print(num,end=' ')
    num = num + 1

for i in range(1,6):
    print('*'*i)
    if i >= 5:
        for s in range(4,1,-1):
            print('*'*s)

#15). Python Loops program to print all odd numbers between 1 to 100 using python.
for i in range(1,100,2):
    print(i,end=' ')

#16). Python Loops program to find the sum of all natural numbers between 1 to n using python.

n = int(input('enter any number:'))
san = 0
for i in range(1,n+1):
    san = san + i
print(san)



#17). Python program to find the sum of all even numbers between 1 to n using python.
n = int(input('sum of all even numbers between 1 to n:'))
sen = 0
for i in range(1,n):
    if i%2 == 0:
        sen = sen+i
print(sen)

#18). Python Loops program to find the sum of all odd numbers between 1 to n using python.
n = int(input('sum of all odd numbers between 1 to n :'))
to = 0
for i in range(1,n):
    if i%2 != 0:
        to = to + i
print(to)

#19). Write a program to count the number of digits in a number using python.
n = '2hakri143'
s = 0
for i in n:
    if i.isnumeric():
        s = s+1
print(s)

#20). Write a program to find the first and last digits of a number using python.
c = 123456789
a = str(c)
for i in range(len(a)):
    if i == 0:
        print(a[0])
    elif i == len(a)-1:
        print(a[-1])

#21). Write a program to find the sum of the first and last digits of a number using python.
a= 123456789
b = str(a)
total = 0
for i in range(len(b)):
    if i == 0:
        total = total + int(b[0])
    elif i == len(b)-1:
        total = total+int(b[-1])
print(total)

#22). Write a program to calculate the sum of digits of a number using python.
a = '2556'
b = 0
for i in a:
    if i.isnumeric():
        '''


'''while True:
    a = int(input('enter first value:'))
    b = int(input('enter second value :'))
    print("1. addition \n"
          "2. multiplication \n"
          "3. subtraction \n"
          "4. divide\n"
          "5. stop application")
    c = int(input('enter your choice : '))
    if c == 1:
        print('addition :',a+b)
    elif c == 2:
        print('multiplication:',a*b)
    elif c == 3 :
        print('subtraction:', a-b)
    elif c == 4 :
        print('division:',a//b)
    else:
        break

a = int(input('enter any number to find the table :'))
for i in range(1,21):
    print(a,'*',i,'=',i*a)
'''
a = int(input('enter number, the table you want :'))
b = int(input('enter range of your table:'))
for i in range(1,b+1):
    print(a,'*',i,'=',i*a)


















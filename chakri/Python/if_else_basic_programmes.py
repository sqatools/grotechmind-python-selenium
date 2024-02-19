#1). Python program to check given number is divided by 3 or not.

'''N = int(input('enter any number : ') )
if N%3 == 0:
    print(N , ' can be divided with 3')
else:
    print(N , 'can not be divide with 3')


#2). If else program to get all the numbers divided by 3 from 1 to 30.
for i in range(1,30):
    if i%3 == 0:
        print(i,end = " ")

print('-'*40)
#3), If else program to get all the numbers divided by 9 from 1 to 30.

for i in range(1,30):
    if i%9 == 0:
        print(i,end= " ")

print('-'*50)

3). If else program to assign grades as per total marks.
marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks
m = int(input('enter student marks : '))
if m < 40:
    print('failed')
elif m>=40 and  m<=50:
    print('grade c')
elif m>50 and  m<=60:
    print('grde B')
elif m>60 and  m<=70:
    print('grade A')
elif m>70 and  m<=80:
    print('grade A+')
elif m>80 and  m<=90:
    print('grade A++')
elif m>90 and  m<=100:
    print('good excelent')
else:
    print('invalid marks')
######################################################################
#4). Python program to check the given number divided by 3 and 5.
n = int(input('enter any number : '))
if n%3 == 0:
    print(n, 'can divided with 3')
else:
     print(n,'can not be divide with 3')
if n%5 == 0:
        print(n,'can divided with 5')
else:
        print(n,'can divided with 5')

#5). Python program to print the square of the number if it is divided by 11.

a = int(input('enter any number : '))
if a%11 == 0:
    print(a**2)
else:
    print(a,' can not divided by 11 ')

#7). Python program to check given number is odd or even.

e = int(input('enter any number to know given number is even or not :'))
if e%2 == 0:
    print('given nuber is even number')
else:
    print('given number is odd number')

#9). Python program to check authentication with the given username and password.

user = 'chakri'
password = 'chakri@180'
u = input('enetr user name:')
p = input('enter passwod : ')
if u == user and password == p:
    print('logged in successfully')
else:
    print('incoreect credentials')



#10). Python program to validate user_id in the list of user_ids.

ls1 = ['chakri','siragam','9154',350]
n = input('enter user id : ')
if n in ls1:
    print('user id is valid')
else:
    print('user id not valid')

#11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.

n = int(input('enter any nuber : '))
if n%2 == 0:
    print(n,'square' ,n**2)
else:
    print('given number cant divided by 2')
if n%3 == 0:
    print(n ,'qube ',n**3)
else:
    print('given number cant be diveded by 3')

#12). Python program to describe the interview process.

r1 = input('enter round 1 result (passed or failed):')
r2 = input('eneter round 2 result (passed or failed) :')
if r1 == 'passed':
    print('round 1 passed get ready for round 2 ')
    if r2 == 'passed':
        print('passed in round 2 and you are placed ')
    else:
        print('sorry you are failed round 2 better luck next time')
else:
    print('sorry you are failed round 1 better luck next time')
    '''

#13). Python program to determine whether a given number is available in the list of numbers or not.

'''l = [12,33,44,45,70,80,87]
n = int(input('enter any number : '))
if n in l:
    print(n , 'present in the list')
else:
    print(n,'not present in the list')
'''

#14). Python program to find the largest number among three numbers.

'''a = int(input('enter first value : '))
b = int(input('enter seond value  : '))
c = int(input('enter third value :'))
if a>b and a>c:
    print(a,'is the largest number among these three')
if b>a and b>c:
    print(b,'is the largest number among these three')
if c>a and c>b:
    print(c,'is the largest number among these three')
else:
    print('two of values among these three are equal')
'''

'''
#15). Python program to check any person eligible to vote or not

age = int(input('enter your age : '))
b = 18-age
if age >= 18:
    print('you are eligible  to vote and please register')
else:
    print('sorry you have to waite',b, 'more years to vote')
    '''
#18). Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.

'''s = int(input('enter student marks :'))
if s >= 35:
    print('you have passed')
else:
    print('sorry you have failed in the exam')
'''
'''#19). Python program to check whether the given number is positive or not.
p = int(input('enter any number ;'))
if p > 0:
    print( 'true', p ,'is positive number')
else:
    print('false', p , 'is negative number')
#20). Python program to check whether the given number is negative or not.
n = int(input('enter any number ;'))
if n <= 0:
    print('true',n,'is negative number')
else:
    print('false',n,'is postive number')'''

#21). Python program to check whether the given number is positive or negative and even or odd.
'''p = int(input('enter any number ;'))
if p>0:
    if p%2 == 0:
        print('give number is positive and even number')
    else:
        print('given number is positive and odd')
else:
    if p%2 == 0:
        print('given number is negative and even')
    else:
        print('given number is negative and odd ')
    
'''
#25). Python program to check whether the given number is an integer or not.
'''a = 22
if type(a) == int:
    print('true')
else:
    print('false')
'''
#26). Python program to check whether the given number is float or not.
'''f = 12
if type(f) == float:
    print('true')
else:
    print('false')'''


'''for i in range(10,15):
  if i != 13 :
    print(i)
'''
'''
#22). Python program to print the largest number from two numbers.
n1 = int(input('enetr fisrt number:'))
n2 = int(input('enter second number:'))
if n1>n2:
    print( n1 ,'is grater number ')
else:
    print(n2 ,'is grater number')
'''

'''#23). Python program to check whether a given character is uppercase or not.
c = input('enter any character:')
if c.isupper():
    print(c,'is upper case')
else:
    print(c,'is lower case')
'''
'''#24). Python program to check whether the given character is lowercase or not.
c = input('enter any character:')
if c.islower():
    print(c,'is upper case')
else:
    print(c,'is lower case')
'''

#31). Python Python program to check whether the input number if a multiple of two print “Fizz” instead of the number and for the multiples of three print “Buzz”. For numbers that are multiples of both two and three print “FizzBuzz”.
'''num = int(input("Enter a number: "))

if num%2 == 0 and num%3 == 0:
    print("FizzBuzz")
elif num%2 == 0:
    print("Fizz")
elif num%3 == 0:
    print("Buzz")'''


#37). Python program to check whether a triangle is isosceles or not. An isosceles triangle is a triangle with (at least) two equal sides.
''' a = int(input('enter triangle side1:'))
b = int(input('enter triangle side2:'))
c = int(input('enter triangle side3:'))
if (a == b) or (a == c):
    print('this is a isosceles triangle')
elif (b == c) or (b == a):
    print('this is a isosceles triangle')
else:
    print('not a isosceles triangle')
    '''


'''#38). Python program that reads month and returns season for that month.
m = input('enter first three letters of month :')
if m == 'feb' or m == 'mar' or m == 'apr' or m =='may':
    print('summer season')
elif m == 'jun' or m == 'jul' or m == 'aug' or m == 'sep':
    print('rainy season')
else:
    print('winter season')
'''
#39). Python program to check whether the input number is a float or not if yes then round up the number to 2 decimal places.

'''num = float(input('enter ny float value : '))

if type(num) == float:
    print(round(num,2))
else:
    print(num)
'''

#40). Python program to check whether the input number is divisible by 12 or not.
a = int(input('enter any number :'))
b = a/12
c = int(b)
if a%12 == 0:
    print(a,'is divisible by',c,'times')
else:
    print(a,'is not divisible by 12')


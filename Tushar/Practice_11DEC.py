####To check given number available in list or not####
'''
list1=[5,10,15,20,40,50]
num1=25
if num1 in list1:
    print("number is available in list:",num1)
else:
    print("number is not available in list:",num1)

'''

'''
list1=[1,2,3,4,5,20,80,40]
num1=int(input("enter the number:"))
if num1 in list1:
    print("number is available in list:",num1)
else:
    print("number is not available in list:",num1)
'''

###same scenario using not in ###
'''
list1=[4,5,8,9,70,50]
num1=1
if num1 not in list1:
    print("number is not available in list:",num1)
else:
    print("number is available in list:",num1)

'''
'''
list1=[40,50,20,1,3,8,9]
num1=int(input("please enter the number:"))
if num1 not in list1:
    print("num1 is not available in list1",num1)
else:
    print("number is availbale in list1",num1)
    
'''

######is ###########

'''
var1=None

if var1 is None:
    print("var1 has empty:",var1)
else:
    print("var1 has some value:",var1)
'''

#######IS NOT####################
'''
var1=20

if var1 is not None:
    print("var1 has some value:",var1)
else:
    print("var1 has empty",var1)
    
    '''

###write if condition in one single line###To check even or Odd
'''
var1=55
result="even" if var1%2==0 else "odd"
print("output:",result)

'''

####################loop Condition#################################

###print 1 to 10 Number###########
for i in range (10):
    print(i)

#range method with default value is zero and diif  value is 1

for var in range(1,5):
    print(var)
#initial value is 1 and last value is 5 and diff is 1


#initail value 1 end value 10 and diff value is 2

for i in range (1,10,2):
    print(i)

print("_"*20)
#programm to print even no from 1 to 20

for i in range (1,20):
    if i%2==0:
        print(i)

##print table of any given number

num=6
for i in range (1,11):
    print(num,"*",i,":",i*num)

print("_"*50)
##write programme to find out all the number which are divisible by 3
#betweeen 1 to 50

for i in range (1,51):
    if i%3==0:
        print(i)




###str="abcdef"
"""""""
a=80
b=100
c=40

print("_"*40)
"""""""
""""
if a>b and a>c:
    print("a has greater value")
else:
    print("a does not have greater value")
### a has greater value
"""
"""""
if a>b and a>c:
    print("a has greater value")
else:
    print("a does not have greater value")
"""

# Program: check any number is dividible by 3 and 7
""""
num1=int(input("Please inter first number:"))
if num1%3 == 0 or num1%7 == 0:
    print("given number can be divide by 3 and 7:", num1)

else:
    print("given number can not be divide by 3 and 7 :", num1)
    
  """""
### Program: write a program to print student marks percentage
"""""
marks =int(input("Enter student marks:"))

if marks>30 and marks<40:
    print("student passed with 3rd grade")
elif marks>40 and marks<50:
    print("student passed with 2nd grade")
elif marks>65 and marks <80:
    print("student passed with A+ greade")
elif marks <30:
    print("Really sorry are failed")
else:
    print("mark can not more than 100")
    
    """"

#############

"""""
Nested if condition

if condi1:
code
if condi2:
  code
else:
 code
 
else:
 code
 
 """""

## Write a program to check nesteed if else condition

round1 ="pass"
round2= "pass"

if round1=="pass":
    print("first round is cleared")
    if round2=="pass":
        print("second round is not clear")
    else:
        print("second rount is not cleae , please try nect")
else:
    print("frist rund is not clear, please try firt round")


















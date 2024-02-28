"""
19). Python program to check whether the given number is an Armstrong number or not.
Example: 153 = 1*1*1 + 5*5*5 + 3*3*3
"""

num = a = int(input("enter a value to tests an armstrong number"))
rev = 0

while a>0:
    rem = a%10
    rev = rev +rem**3
    a= a//10

if rev == num:
    print("armstrong number")
else:
    print("not an armstrong number")



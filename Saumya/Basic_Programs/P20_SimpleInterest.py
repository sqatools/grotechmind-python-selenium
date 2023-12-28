"""
20). Python program to calculate simple interest.
Formula = P+(P/r)*t
P = Principle Amount
r = Anual interest rate
t = time
"""
P = int(input("enter principal amount"))
R = int(input("enter rate of interest"))
T = int(input("enter duration/time"))
print("calculated simple interest is: ", P+(P/R)*T)
###########Logical Operator#################3
#and
#or

a=50
b=60
c=40

if a>b and a>c:
    print("a is greater value")
else:
    print("a is small value ")


if a>b or a>c:
    print("a is greter ")
else:
    print("a is small")

###programmefor check any number is divisible by 3 and 7

num=50
if num%3==0 and num%7==0:
    print("number is divisible by 3 and 7")
else:
    print("number is  not divisible by 3 and 7")
#number is  not divisible by 3 and 7


num=51
if num%3==0 and num%7==0:
    print("number is divisible by 3 and 7")
else:
    print("number is  not divisible by 3 and 7")
#number is  not divisible by 3 and 7

num=21
if num%3==0 and num%7==0:
    print("number is divisible by 3 and 7")
else:
    print("number is  not divisible by 3 and 7")
#number is divisible by 3 and 7

###############################

"""
num1=int(input("Please enter number:"))

if num1%3==0 and num1%7==0:

    print("Number is divisible by 3 and 7",num1)
else:
    print("Number is not Divisible by 3 and 7",num1)
    
    """

########################################################################

###################if elif condition################


"""
if cond1:
   code
elif cond2:
     code
elif cond3:
     code
else:
     code
"""

############################################################3


###programme for to print student grade as per mark
"""
marks=int(input("Please enter student marks:"))

if marks<40:
    print("You are Fail")
elif marks>=40 and marks<50:
    print("You pass with  c grade")
elif marks>=50 and marks<60:
    print("You Pass with B grade")
elif marks>=60 and marks <75:
    print("you pass with A grade")
elif marks>=75 and marks<90:
    print("you pass with A+ grade")
elif marks>=90 and marks<=100:
    print("you are topper")
else:
    print("plese enter marks between 1 to 100")
    
    """

##########################################################################################

###nested if condition###
"""
if cond1:
      code
      if cond2:
          code
       else:
            code
else:
     code


"""

"""
print("*"*100)

round1="pass"
round2="fail"

if round1=="pass":
    print("you cleared first round")
    if round2=="pass":
        print("you cleared second round")
    else:
        print("you have not cleared second round")
else:
    print("you have not cleared first round")


"""








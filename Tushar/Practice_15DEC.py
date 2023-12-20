#write a programme to calculator which accepts continue input###
"""
while True:
    num1=int(input("Please enter first value:"))
    num2=int(input("please enter second value:"))
    print("1. Addition\n"
          "2. Subtraction\n"
          "3. Multiplication\n"
          "4. Division\n"
          "5. Stop The Application")
    opr_input=int(input("Please enter your Choice:"))
    if (opr_input)==1:
        print("Addition:",num1+num2)
    elif (opr_input)==2:
        print("Subtraction:",num1-num2)
    elif (opr_input)==3:
        print("Multiplication:",num1*num2)
    elif(opr_input)==4:
        print("Division:",num1//num2)
    elif(opr_input)==5:
        print("Stop The Application:")
"""

###################################STRING###############################################

var1='good Morning'
print(var1,type(var1))

var2="Good Morning"
print(var2,type(var2))

var3="""hello
good morning
have nice day
"""
print(var3,type(var3))

var4='''we are learnig Python Programming
here is todays topic is string datatype
afetr that we can learn other datatypes
'''

print(var4,type(var4))

var5="have 'nice' day"

print(var5,type(var5))

var6='i love "Python" Programming'

print(var6,type(var6))

var7="13"
print(var7,type(var7))

#############string Concatation#####################

#1.Concatation

str1="Good"
str2="Morning"
str3=str1+" "+str2
print(str3)

print("+"*100)

Name="Tushar"
age=35
City="nashik"


#my name is tushar and age is 35 and live in nashik

var1="my name is "+ Name  +" and age is " + str(age)  +" and live in " + City
print(var1)

print("="*100)


#2. Format method

msg2="my name is {} and age is {} and live in {} ".format(Name,age,City)
print(msg2)

#3. f string Formatting

msg3=f"my name is {Name} and age is {age} and live in {City} "
print("msg3:",msg3)

##################String Indexing and String Slicing###########################

# String Indexing#

stra="Tushar Aher"
print(stra[5])
print(stra[-3])


#string Slicing#

#Rule.1
#str[initial_index: Last_index]
#return substring will considerinitial index value and skip last index value

str1="python Programming"
result=(str1[0:6])
print(result)

#Rule.2
#str[ : last_index]
#default initail_index will be zero and last_index is user defined

str2="India is my country"
result=(str2[:5])
print(result)

result1=(str2[:-2])
print(result1) #India is my count
#initial index is not given so by default initial index  is zero and last index is -2 so start from begineening till index -1

result2=(str2[-7:-2]) #count
print(result2)

#Rule.3
#str[initial_index :]
#initial index is user defined and by default last index will be end of string

str11="My Name is Tushar Aher"
print("str11:",str11[3:]) #str11: Name is Tushar Aher
print("str11:",str11[-5:]) #Aher



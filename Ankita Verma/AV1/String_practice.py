#String Introduction

#String is ordered and immmutable
"""f_string= "Hello World"
len( "Hello World")
print(len("Hello World"))"""

"""s_string="I AM LEARNING pYTHON"
add_string=str("Hello World" ""+" I AM LEARNING pYTHON ")
print(add_string)
print(len(add_string))"""

"""print(f_string[0])
print(f_string[1])
print(f_string[2])
print(f_string[3])
print(f_string[4])

print(f_string[0])
print(f_string[-1])
print(f_string[-2])
print(f_string[-3])
print(f_string[-4])

#Slicing: Access a range of characters in a string by using the slicing operator colon :
#print(f_string[0:8:3])"""

# id function
"""sting1="welcome"
sting1="Python"
print(id(sting1))


string1="Python Programming"
result=""
for i in range(-1 ,)"""

# Print Write the string after the first occurrence of ','
# and the string after the last occurrence of ',' in the string "Hello, Good, Morning". World".


#Replace Method
"""string_1= "I want to learn C#"
print(string_1.replace('C#', 'Python').replace('learn','Study'))
#print(string_1.count('l').replace('C#', 'D#')) Error"""

#Count Method
"""string_2="I am going to school"
print(string_2.count('o'))"""
#
#split method
"""str1="We have to be  responsible for our actions"
result=str1.split('be')
print(result)"""

#find method return index value and if value is not avaliable then -1
"""stri1="Happy new year"
result=stri1.find('new')
print(result)


print("stri1 :", stri1.find('Happy'))

print("stri1 :", stri1.find('O'))
print("stri1 :", stri1.find('D'))
print("stri1 :", stri1.find('o'))
"""





#fruits = ["apple", "banana", "cherry"]
"""for x in fruits:
  print(x)
  if x == "banana":"""


"""name_string= "Happy New Year"
name_string= "Happy New Year" [0::-1]
print(print(name_string))"""

######################################################################################
list2 = [5,6,8,9,10]
#without indexin
for val in list2:
  print(val)
############################################
list3 = [5,6,8,9,10]
#with indexing
for i in range(len(list3)):
    print(i,"i",list3[i])
####################################################################

"""list3 = [5,6,8,9,10]
#with indexing

for i in range(len(list3)):
    print(i,"i",list3[[i][3]])"""

#print(""--""*2)
"""name = 'Alice'
greeting = "Hello, world!"
quote = "'”Learn a new programming language by writing programs in it.” – Lord Walles”’"
print(name[0])
print(greeting[0:-1])
print(quote[0::])
string1=quote.split()
print(string1)
string2=quote.count(0)
print(string2)"""

"""name="Ankita"
you_are_in ="Python"
Duration =" 3 months "
msg="Hi !name= "+name+", you_are_in = "+you_are_in+" , Duration= "+Duration+""
print(msg)"""

#####################################################################
"""Name=input("Enter your Name")
you_are_in=input("Enter Trainning")
Duration =str(input("Enter duration"))
msg2=msg="Hi ! "+Name+", you_are_in "+you_are_in+"Duration= "+Duration+"months"
print(msg2)"""

str="Python Programming"
"Rule 1=str[start index :last INdex]"
str1=str[::-1]
print(str1)
#str3=str.split()
#print(str3)


#Question to asked difference of index??
print("_"*50)
# Rule 4 : str[initial_index : last_index : difference of index]
strb = "Good Morning, How are you"
#strp=strb[10::]
#print(strp)
"""stro=strb[::-1]
print(stro)"""

#1: Write a program to reverse a string in python.
str_user= input("Enter String for Reverse: ")
for val in range(len(str_user)-1,-1,-1):
    print(str_user[val],end="")
    print("/n")

#for i in range(len(str) - 1, -1, -1):
#  print(str[i], end="")
#print("\n")

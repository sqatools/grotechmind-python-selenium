var1 = "Good Morning"
print(type(var1)) # <class 'str'>

var2 = 'Python Programming'

var3 = """Python basic programs contains 
Python Programming Examples with 
all native Python data type, 
mathematical operations on Python Variables"""

var4 = '''Python basic programs contains 
Python Programming Examples with 
all native Python data type, 
mathematical operations on Python Variables'''

var5 = "Hello hope 'you' are doing good"
var6 = 'Python is "very" easy to learn'

print("var1 :", var1, type(var1))
print("_"*50)
print("var2 :", var2, type(var2))
print("_"*50)
print("var3 :", var3, type(var3))
print("_"*50)
print("var4 :", var4, type(var4))
print("_"*50)
print("var5 :", var5, type(var5))
print("_"*50)
print("var6 :", var6, type(var6))




# "Hello My name is Rahul and age is 25 and live is Mumbai"

#1. String concatenation
print("_"*50)
str1 = "Python"
str2 = "programming"
str3 = str1 +" "+str2
print(str3)
# name = "Virat"
# age = 25
# city = "Bangalore"
"""
name = input("Please enter the name :")
age = input("Please enter the age :")
city = input("Please enter the city :")

msg1 =  "Hello My name is "+ name +" and age is " + str(age) + " and live is "+city
print(msg1)

#2. Format method
msg2 =  "Hello My name is {} and age is  {} and live is {}".format(name, age, city)
print(msg2)

#3. f string formating
msg3 = f"Hello My name is {name} and age is {age} and live is {city}"
print(msg3)
"""
##################################################
# String Indexing and String Slicing
#       0 1 2 3 4 5
#stra= "P y t h o n"
#      -6-5-4-3-2-1

stra = "Python"
print(stra[2])  # t
print(stra[-4]) # t

strb = "Hello Good Morning We are learning Python Programming"
print(strb[6]) # G

# String slicing
# Rule1 : str[initial_index : last_index]
# return substring will consider the initial index value and skip the last index value

strb = "Python Programming"
result1 = strb[0:6]
print(result1) # Python

result2 = strb[2: 10]
print(result2) # thon Pro

result11 = strb[-7: -1]
print("result 11:", result11) # rammin

# Rule2 : str[ : last_index]
# default initial index will be zero and the last index which user define
strc = "India is best cricket team"
result3 = strc[:7]
print("result3 :", result3) # India i

result4 = strc[:-2]
print("result4 :", result4)
# India is best cricket te

# Rule3 : str[initial_index:]
# default last index will be end of the string
strh = "Programming is good tools to solve problems"

print("strh + :", strh[5:])
# amming is good tools to solve problems
print("strh - :", strh[-10:])
# e problems

print("_"*50)
# Rule 4 : str[initial_index : last_index : difference of index]
strb = "Good Morning, How are you"

print(strb[2: 20: 1]) # od Morning, How ar

print(strb[2: 20: 2]) # o onn,Hwa

print(strb[-1: 20: -1]) # uoy

print(strb[-1: 2: -1]) # uoy era woH ,gninroM duoy
print(strb[2: -1: 2]) #

# Rule5 str[:last_index:difference]
# initial index will be zero if difference is positive and initial index will -1 if the different negative

strc = "We are learning Python Programming"

print(strc[:10:1])  # We are lea  # initial index is zero
print(strc[:10:-1]) # gnimmargorP nohtyP gnin  # initial index will be -1
print(strc[:10:-2]) #

# Rule5 : str[::difference]
# initial index will be zero and last index will be end of the string with positive difference
# initial index will be -1 and begining of string will be end of the output with negative difference

strj = "Have a nice day, hope you are doing good"
print(strj[::1])  #Have a nice day, hope you are doing good
print(strj[::2])  # Hv  iedy oeyuaediggo
print(strj[::-1]) # doog gniod era uoy epoh ,yad ecin a evaH


#####################################################
print("_"*50)
# program : Arrange the words as per expectation
strk = "Python Programming"
output = "gython ProgramminP"
p_val = strk[0]
g_val = strk[-1]
rem_val = strk[1:-1]
print(rem_val)
print(g_val+rem_val+p_val)
# gython ProgramminP

# output = "Python Programming Python"
strk = "Python Programming"
var1= strk
var2 = strk[:6]
var3= var1+" "+ var2
print(var3)


################################################################
print("_"*50)
# get values from string using loop
strl = "Made In India"
for var in strl:
    print(var)

# apply loop with indexing
str_len= len(strl)
print("string_len :", str_len)
for i in range(str_len):
    print(i, strl[i])

######################### String Methods ################################
print("_"*50)
print(dir(str))

"""
'capitalize', 'casefold', 'center', 'count', 'encode', 
'endswith', 'expandtabs', 'find', 'format', 'format_map',
 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 
 'isdigit', 'isidentifier', 'islower', 'isnumeric', 
 'isprintable', 'isspace', 'istitle', 'isupper',
  'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
  'partition', 'removeprefix', 'removesuffix', 
  'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 
  'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
   'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
"""


num = 4
fact = 1
for i in range(num, 0, -1):
    fact = fact * i

print("factorial :", fact)



tup1 = (4, 6, 8, 50, 'Hello', [4, 7, 8], 'a')

print(tup1[4])
print(tup1[4:5])

str2 = "Programming"
print(str2[4])
print(str2[4:5])

list2 = [4, 6, 8, 50, 'Hello', [4, 7, 8], 'a']
print(list2[3])
print(list2[3:7:1])

print(list2.index('Hello'))


###########################################################
print("_"*50)
# upper method
str1 = "Hello Good Morning"
print(str1.upper()) # HELLO GOOD MORNING

# lower case
print(str1.lower()) # hello good morning

# check given string is upper or lower
str2 = "python"
print(str2.islower())  # True
print(str2.isupper())  # False

str3 = "PROGRAMMING"
print("str3 :", str3.isupper())
str4 = "Hello"
print("str4: ", str4.islower()) # False
print("str4 :", str4.isupper()) # False

# swapcase method
str5 = "Good Morning How Are You?"
print("str5 :", str5.swapcase())
# gOOD mORNING hOW aRE yOU?

# title method
str6 = "Tata motor is good vehicle company"
print("str6 :", str6.title())
# Tata Motor Is Good Vehicle Company

# istitle method
str7 = "Mahindra make good SUV cars"
print("str7 :",str7.istitle()) # False

str8 = "Tata Motor Is Good Vehicle Company"
print("str8 :",str8.istitle()) # True

# Index method : this method find the position of any character or substring in given sentence
str8 = "Tata Motor Is Good Vehicle Company"
print(str8.index('I')) # 11
# print(str8.index('w'))
# when char is not available
# ValueError: substring not found
print(str8.index("o")) # 6


print("_"*50)
str9 = "Tata Motor Is Good Vehicle Company"
count = 0
for i in range(len(str9)):
    if str9[i] == 'o':
        count = count+1
        print(i, "count :", count)
        if count == 4:
            print(i)
        else:
            continue
    else:
        continue


# find method : find method return the index position of char/substring
# if it is available, or it will return -1 if not available
str10 = "India lost second ODI"
print("str10 :", str10.find('ODI')) # 18

print("str10 :", str10.find('Win')) # -1

print("str10 :", str10.find('O')) # 18
print("str10 :", str10.find('D')) # 19
print("str10 :", str10.find('o')) # 7


# Split method : this method split the string from specific delimeters/char/substring
# and return the output as list of substrings

str11 = "Hello,Good,Morning"
result11 = str11.split(",")
print("result11:", result11) # result11: ['Hello', 'Good', 'Morning']
print(str11.split("o")) # ['Hell', ',G', '', 'd,M', 'rning']

stra = "Hope you are doing good"
result = stra.split() # by default parameter is space
print("result :", result)

for word in result:
    print(word, word[0])

# count method
print("stra :", stra.count("o")) # 5
print("stra :", stra.count("doing")) # 1


# Replace method :
print(stra.replace('good', 'bad')) # Hope you are doing bad
print(stra.replace('good', 'bad').replace('you', 'all'))

# Hope all are doing bad
print(stra.replace('good', 'bad').replace('you', 'all').count('a')) # 3
print(stra.replace("H", "h")) # hope you are doing good

print(dir(str))
print("Hello world")

print("_"*40)
# join, strip, isspace, isnumeric, isalpha, isalnum

# Join Method:

str2 = "Python"
#P-y-t-h-o-n

print("-".join(str2))
print(" ".join(str2))
print("^&^*&".join(str2))


stra = "Python Programming"
result = ''
for i in range(len(stra)):
    if i%3 == 0 and i != 0:
        result = result + "-" + stra[i]
    else:
        result = result + stra[i]
    print(result)

print("Result :", result)


# reverse the string

stra = "Python Programming"
output = ''
for i in range(-1, -len(stra)-1, -1):
    output = output + stra[i]
    print(i, stra[i], output)

print("Result :", output)

####################
# strip method : this method remove the trailing spaces from given string
# space available before and after the string known as trailing space.
print("_"*50)
strb = " Hello Programming "
print(strb)

print(strb.strip()) # remove all trailing space
print(strb.lstrip()) #
print(strb.rstrip())

##################################
# isspace
print("_"*50)
strv = "Hello Program"

result = ''
for char in strv:
    #print(char, ":", char.isspace())
    if char.isspace():
        result = result + "-"
    else:
        result = result + char

print("result :", result)
print(strv.replace(" ", "-"))


# isnumeric method : This  method check the given string has only number
stra = "python 123"
print(stra.isnumeric())  # False
strb = "543452345"
print(strb.isnumeric())  # True

# isalnum
strc = "python123"
print(strc.isalnum()) # true

# isalpha
strd = "Python"
print(strd.isalpha()) # True

stre = "Python Hello"
print(stre.isalpha()) # False

# isdigit
strf = "4567336355"
print("strf :", strf.isdigit())

print("%".isdigit())
print("%".isnumeric())

print('H3ll0'.isdigit())
print('%'.isdigit())
print('45/2'.isnumeric())
print('45^2'.isdigit())

print("\u0668".isdigit())
print("\u0668".isnumeric())

val = "\u0668"
print("val :", int(val), val)

print('II'.isdigit())
print('IX'.isnumeric())
print('45^2'.isdigit())
print('$300'.isnumeric())













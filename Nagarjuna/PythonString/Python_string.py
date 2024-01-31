#####   STRING   #########

var1 = "good morning"
print(var1, type(var1))

var2 = 'learning python'

var3 = """Python basic programs contains 
Python Programming Examples with 
all native Python data type"""

var4 = ''' Python basic programs contains 
Python Programming'''

var5 = "hello how 'are' you now"
var6 = 'python is "simple" to learn'

print("var2 :", var2,type(var2))
print("var3 :", var3,type(var3))
print("var4 :", var4,type(var4))
print("var5 :", var5,type(var5))
print("var6 :", var6,type(var6))

#1. String concatenation
str1 = "python"
str2 = "programming"
str3 = str1+ " "+str2
print(str3)

"""
name = input("Please enter the name :")
age = input("Please enter the age :")
city = input("Please enter the city :")
"""
Name = "naga"
Age = 28
City = "bangalore"
msg1 = "Hello my name is "+Name+ " and age is "+ str(Age)+" and live in "+City
print(msg1)

#2. Format method
msg2 = "Hello my name is {} and age is {} and live in {}".format(Name,Age,City)
print("msg2: ",msg2)

#3. f string formating
msg3 = f"Hello my name is {Name} and age is {Age} and live in {City}"
print("msg3: ",msg3)

##########################################
# String Indexing and string Slicing

stra = "Python"
print(stra[3])
print(stra[-2])

# String Slicing
# Rule1 : str[initial_index : last_index]
# return substring will considerinitial index value and skip last index value

str1="python Programming"
Result=(str1[0:6])
print(Result)

# Rule2 : str[ : last_index]
# default initial index will be zero and the last index which user define
str2 = "I am Trying to learn python"
result1 = str2[:7]
print("result1 :", result1) # I am Tr

result2 = str2[:-2]
print("result2 :", result2)
# I am Trying to learn pyth

# Rule3 : str[initial_index:]
# default last index will be end of the string
strb = "I am learning selenium with python "

print("strb + :", strb[5:])
#  learning selenium with python
print("strb - :", strb[-10:])
# th python

print("%"*40)

# Rule 4 : str[initial_index : last_index : difference of index]
strc = "i am learning python from MKT online"

print("strc: ",strc[3:13:1])   # m learning
print("strc: ", strc[3:13:2])  #  mlann

#when we use diff value is minus then our initial index is always minus and read from right to left in reverse order
strc = "i am learning python from MKT online"

print("strc: ",strc[3:13:-1]) #strc: not giving any result due to initial index is positive

print("strc: ", strc[-3:13:-1])  #ilno TKM morf nohtyp


# Rule5 :
# str[:last_index:difference]
# initial index will be zero if difference is positive and initial index will -1 if the different negative

strc = "i am learning python from MKT online"

print(strc[:10:1])  # i am learn #diff is positive so initial indesx is zero  print from left to right
print(strc[:10:-1]) # enilno TKM morf nohtyp gn #diff is negative so initial index is -1 . so print from right to left
print(strc[:10:-2]) # ein K ofnhy n

#Rule6 :
#str[: :  Difference]
#when diff is positive : initial index is zero and last index is end of string .print left to right
#when diff is negative : initial index is -1 and last index is begining of string .print right to left


strd= "i am learning python from MKT online"

print(strd[::1]) # i am learning python from MKT online
print(strd[::-1]) # enilno TKM morf nohtyp gninrael ma i

###########################################################
print("-"*40)
# program: Arrange the words as per expectations
stre = "Python Programming"
output = "gython Programminp"
p_val = stre[0]
g_val = stre[-1]
rem_val = stre[1:-1]
print(rem_val)
print(g_val+rem_val+p_val)
 # gython ProgramminP

# output = "Python Programming Python"
strf = "Python Programming"
var1 = strf
var2 = strf[0:6]
var3 = var1+" "+var2
print(var3)  # Python Programming Python

# get values from string using loop
strl = "Made In India"
for var in strl:
    print(var)

# apply loop with indexing
str_len= len(strl)
print("string_len :", str_len)
for i in range(str_len):
    print(i, strl[i])

############## STRING METHODS #################
print("+"*40)
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

##  upper method ###
str1 = "string is in upper method"
print(str1.upper())  # STRING IS IN UPPER METHOD

## lower case method
str2 = "THIS IS LOWER CASE METHOD"
print(str2.lower())  # this is lower case method

# check given string is upper or lower
str3 ="success is not easy"
print(str3.isupper()) # False
print(str3.islower()) # True

str4 = "TRY AS HARD AS POSSIBLE"
print("str4: ",str4.islower()) # False
print("str4 : ",str4.isupper()) #True

# swapcase method
# swapcase Method converts the string upper to lower and lower to upper
str5 = "Python For Selenium is MORE"
print("str5 : ",str5.swapcase()) # pYTHON fOR sELENIUM IS more

# Title method
# ## Title Method converts first letter is captial
str6 = "now a days it is not easy for seeking a good job"
print("str6: ",str6.title()) # Now A Days It Is Not Easy For Seeking A Good Job

#istitle method
# to check string is title or not
print("str6: ",str6.istitle())  # False

str7 ="Now A Days It Is Not Easy For Seeking A Good Job"
print("str7 : ",str7.istitle()) # True

# Index method : this method find the position of any character or substring in given sentence
str8 = "Python For Selenium is MORE"
print("str8 : ",str8.index('S')) # 11
# when char is not available
# ValueError: substring not found

print("?"*50)
str9 = "Tata Motor is Good Vehicle company"
count = 0
for i in range(len(str9)):
    if str9[i] =='o':
        count = count+1
        print(i, "count : ", count)
        if count ==4:
            print(i)
        else:
            continue
    else:
        continue

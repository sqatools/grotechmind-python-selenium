#1). Write a Python program to get a string made of the first and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string
"""
str=input("please enter string:")
if len(str)<2:
    print(True)
else:
    print(str[0] +str[-2:])
"""
"""
str=input("please enter string:")
if len(str)<2:
    print(True)
else:
    print(str[0]+str[-2:])
"""

#2). Python string program that takes a list of strings and returns the length of the longest string.


# str=input("please enter string:")
# print(str.split())
#
# word_length=0
# for word in str:
#     length=len(word)
#     if length>word_length:
#         word_length=length
# print(word_length)



"""
string = ["i", "am", "learning", "python"]
temp = 0

for word in string:
    a = len(word)
    if a > temp:
        temp = a

#Printing output
print(temp)

"""
"""
str=input("please enter string:")
string=str.split()
temp=0
for word in string:
    a=len(word)
    if a>temp:
        temp=a
print("longest_length:",temp)
print("longest_string:",word)

"""

"""
str=input("please enter string:")
string=str.split()
temp=0

for word in string:
    a=len(word)
    if a>temp:
        temp=a
print(temp)

"""


#3). Python string program to get a string made of 4 copies of the last two characters of a specified string
# (length must be at least 2).
'''
str=input("please enter string:")
string=str[-2:]
print(string*4)
'''
#4). Python string program to reverse a string if it’s length is a multiple of 4.
"""
str=input("please enter string:")

if len(str)%4==0:
    print(str[: : -1])
else:
    print("string length is not multiple of 4")

"""


#5). Python string program to count occurrences of a substring in a string.
'''
str=input("please enter string:")
substr=str.split()
count=substr.count('my')
print(count)
'''

#6). Python string program to test whether a passed letter is a vowel or consonant.
'''
str=input("please enter letter:")

if str=='a' or str=='e' or str=='i' or str=='o' or str=='u':
    print("its vowel")
else:
    print("its consonant")

'''

'''

letter = input("Please enter letter")

for char in letter:
    if char == "a" or char =="e" or char =="i" or char =="o" or char =="u":
        print(f"{char} is vowel")
    else:
        print(f"{char} is consonant")
'''
'''
str=input("please enter string:")

for char in str:
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
        print("its ovel")
    else:
        print("its consonent")
'''

#7). Find the longest and smallest word in the input string.
'''
string = input('please enter string:')
list1 = string.split(" ")

#printing output
print("Longest word: ", max(list1, key = len))
print("Smallest word: ", min(list1, key = len))

'''

'''
string=input("Please enter string:")

list=string.split()

print("longest word:",max(list,key=len))
print("smallest word:",min(list,key=len))
'''


#8). Print most simultaneously repeated characters in the input string.
'''
str=input("please enter string:")
max_count=0
max_rchar=''
temp=''

for char in str:
    if char not in temp and str.isspace() is False:
        char_count=str.count(char)
        temp=temp+char
        if char_count>max_count:
            max_count=char_count
            max_rchar=char
print(max_rchar)
print(max_count)
'''
'''
max_count=0
max_rchar=''
temp=''

str=input("please enter string:")

for char in str:
    if char not in temp and str.isspace() is False:
        char_count=str.count(char)
        if char_count>max_count:
            max_count=char_count
            max_rchar=char
print(max_count)
print(max_rchar)
'''


# 9). Write a Python program to calculate the length of a string with loop logic.
'''
str=input("please enter string:")
print(len(str))

'''
"""
str=input("please enter string:")
count = 0

for char in str:
    count +=1
print(count
      
      """


# 10). Write a Python program to replace the second occurrence of any char with the special character $.
# Input = “Programming”
# Output = “Prog$am$in$”

# Take a string as input and create an empty string.
# Using For loop add each character of the given string to the empty string.
# If a character repeats then do not add that character add $ instead.
# Print the output.
'''
str=input("please enter string:")

result=''

for char in str:
    if char in result:
        result=result+'$'
    else:
        result=result+char
print(result)
'''
'''
str=input("please enter string:")

result=''

for char in str:
    if char in result:
        result=result+'$'
    else:
        result=result+char
print(result)
'''

#11). Write a python program to get to swap the last character of a given string.
# Input = “SqaTool”
# Output = “IqaTooS”
'''
str=input("please enter string:")
print(str[-1]+str[1:-1:]+str[0])
'''

#12). Write a python program to exchange the first and last character of each word from the given string.
# Input = “Its Online Learning”
# Output = “stI enlino gearninL”
'''
str=input("please enter string:")

list=str.split()

for word in list:
    new_word=word[-1]+word[1:-1:]+word[0]
    print(new_word,end=" ")
'''
'''
str=input("please enter string:")

list=str.split()

for word in list:
    new_word=word[-1]+word[1:-1:]+word[0]
    print(new_word,end=' ')

'''

#13). Write a python to count vowels from each word in the given string show as dictionary output.
# Input = “We are Learning Python Codding”
# output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”}
'''
str=input("please enter string:")

list=str.split()

vowels='aeiou'

dictionary=dict()

for word in list:
    count=0
    for char in word:
        if char in vowels:
            count=count+1
    dictionary[word]=count
print(dictionary)
'''
'''
str=input("please enter string:")

list=str.split()

vowels='aeiou'


dictionary=dict()

for word in list:
    count=0
    for char in word:
        if char in vowels:
            count=count+1
    dictionary[word]=count
print(dictionary)

'''

# 14). Write a python to repeat vowels 3 times and consonants 2 times.
# Input = “Sqa Tools Learning”
# Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg”

'''
str=input("please enter string:")
result=''
vowels='aeiou'
for char in str:
    if char in vowels:
        result=result+char*3
    else:
        result=result+char*2
print(result)
'''

'''
str=input("please enter sttring:")

vowels='aeiouAEIOU'

result=''

for char in str:
    if char in vowels:
        result=result+char*3
    else:
        result=result+char*2
print(result)
'''
#
# 15). Write a python program to re-arrange the string.
# Input = “Cricket Plays Virat”
# Output = “Virat Plays Cricket”

# str='cricket plays virat'
#
# list=str.split(' ')
#
# list.reverse()
#
# " ".join(list)



"""
string = "Happy new Year"
lst = string.split(" ")
print(lst)
rev=lst.reverse()
print(rev)
"""



# 16). Write a python program to get all the digits from the given string.
# Input = “””
# Sinak’s 1112 aim is to 1773 create a new generation of people who
# understand 444 that an organization’s 5324 success or failure is
# based on 555 leadership excellence and not managerial
# acumen
# “””
# Output = [1112, 5324, 1773, 5324, 555]

"""
str=input("please enter string:")

lst1=str.split()

lst2=[]

for value in lst1:
    if value.isdigit():
        lst2.append(value)
print(lst2)
"""
#Append in Python is a pre-defined method used to add a single item to certain collection types.
# Without the append method, developers would have to alter the entire collection's code for adding a single value or item.
# Its primary use case is seen for a list collection type.
"""
str=input("please enter string:")

list1=str.split()

list2=[]

for value in list1:
    if value.isdigit():
        list2.append(value)
print(list2)
"""
"""
str=input("please enter string:")

list1=str.split()

list2=[]

for val in list1:
    if val.isdigit():
        list2.append(val)
print(list2)


"""


# 17). Write a python program to replace the words “Java” with “Python” in the given string.
# Input = “JAVA is the Best Programming Language in the Market”
# Output = “Python is the Best Programming Language in the Market”
"""
str=input("please enter string:")

result=str.replace('java','python')
print(result)

"""


"""
string = "JAVA is the Best Programming Language in the Market"
List1 = string.split(" ")

for word in List1:
    if word == "JAVA":
        index = List1.index(word)
        List1[index] = "PYTHON"

#Printing output
print(" ".join(List1))
"""

"""

str=input("please enter string:")

lst=str.split()

for word in lst:
    if word=='JAVA':
        index=lst.index(word)
        lst[index]='PYTHON'
print(' '.join(lst))

"""
"""
str=input("please enter string:")

lst=str.split()

for word in lst:
    if word=='JAVA':
        index=lst.index(word)
        lst[index]='PYTHON'
print(' '.join(lst))

"""
'''
str=input("please enter string:")

list=str.split()

for word in list:
    if word=='tushar':
        index=list.index(word)
        list[index]='pratibha'
print(' '.join(list))

'''

# 18). Write a Python program to get all the palindrome words from the string.
# Input = “Python efe language aakaa hellolleh”
# output = [“efe”, “aakaa”, “hellolleh”]
"""
str=input("please enter string:")

list=str.split()

new_list=[]

for word in list:
    if word==word[::-1]:
        new_list.append(word)
print(new_list)
"""
"""
str=input("please enter string:")

list=str.split()

new_list=[]

for word in list:
    if word==word[::-1]:
        new_list.append(word) #The append() method appends an element to the end of the list.
print(new_list)

"""
'''
str=input("please enter string:")

lst=str.split()

new_list=[]

for word in lst:
    if word==word[::-1]:
        new_list.append(word)
print(new_list)

'''
"""
str=input("please enter string:")

list=str.split()

new_list=[]

for word in list:
    if word==word[::-1]:

        new_list.append(word)
print(new_list)

"""

"""
str=input("please enter string:")

list=str.split()

new_list=[]

for word in list:
    if word==word[::-1]:
        new_list.append(word)
print(new_list)

"""




# 19). Write a Python program to create a string with a given list of words.
# Input = [“There”, “are”, “Many”, “Programming”, “Language”]
# Output = There are many programming languages.

"""

list = ["my","name","is"]
print("  ".join(list))
"""

"""
#Input list
list1 = ["There", "are", "Many", "Programming", "Language"]

#Printing output
print(" ".join(list1))

"""



# 20). Write a Python program to remove duplicate words from the string.
# Input = “John jany sabi row john sabi”
# output = “John jany sabi row”
"""
str=input("please enter string:")

lst=str.split()

new_list=[]
for word in lst:
    if word not in new_list:
        new_list.append(word)
print(" ".join(new_list))
"""

"""
str=input("please enter string:")

lst=str.split()

new_list=[]

for word in lst:
    if word not in new_list:
        new_list.append(word)
print(' '.join(new_list))
"""



# 21). Write a Python to remove unwanted characters from the given string.
# Input = “Prog^ra*m#ming”
# Output = “Programming”
#
# Input = “Py(th)#@&on Pro$*#gram”
# Output = “PythonProgram”


# str=input("please enter string:")
#
# for word in str:
#     if word.isalnum():
#         print(' '.join(word))

# str=input("please enter string:")

# for word in str:
#     if word.isalnum():
#         print(" ".join(word),end="")


# # 22). Write a Python program to find the longest capital letter word from the string.
# # Input = “Learning PYTHON programming is FUN”
# # Output = “PYTHON”
#
#
#
# #Importing re
# import re
#
#
# string=input("please enter string:")
#
# #Finding all capital letters words
# word = re.findall(r"[A-Z]+", string)
#
# #Printing output
# print(max(word, key=len))


#
# 23). Write a Python program to get common words from strings.
# Input String1 = “Very Good Morning, How are You”
# Input String1 = “You are a Good student, keep it up”
# Output = “You Good are”































































































































































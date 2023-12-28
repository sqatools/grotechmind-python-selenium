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




















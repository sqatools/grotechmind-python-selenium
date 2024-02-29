# #1.Python string program that takes a list of strings and returns the length of the longest string.
# strl= []
# list1 =["darani","sunkara","durgaBhavani","fagjbdjnefrkjnfrkjenfk"]
# for i in list1:
#     if len(i)>len(strl):
#         strl=i
# print(strl)

# #2.Python string program to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
# str1='Darani'
# print(str1[-2:]*4)

# #3. Python string program to reverse a string if it’s length is a multiple of 4.
# str2='selenium'
# if len(str2)%4 ==0:
#     print(str2[::-1])

# #4.Python string program to tests whether a passed letter is a vowel or consonant.
# str3="grotechmind"
# for char in str3:
#     if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
#         print(f"{char} is vowel")
#     else:
#         print(char,'consonent')
#
#
# #5. Find the longest and smallest word in the input string.
# str4="I am darani sunkara"
# spl=str4.split(" ")
# print(spl)
# print("long" ,max(spl))
# print("small" ,min(spl))

#6. Write a Python program to replace the second occurrence of any char with the special character $.
# cha=''
# str5='Programming'
# for i in str5:
#     if i in cha:
#         cha=cha+'$'
#     else:
#         cha=cha+i
# print(cha)

# #7. Write a python program to get to swap the last character of a given string.
# Input = 'SqaTool'
# print(Input[-1]+Input[1:-1]+Input[0])
from operator import index

# Inut = 'Its Online Learning'
# valu= Inut.split(' ')
# for i in valu:
#     print(i[-1]+i[1:-1]+i[0],end=' ')

#Write a python program to re-arrange the string.
#
# input1 = 'Cricket Plays Virat'
# value1 = input1.split(' ')
#
# value1.reverse()
# print(' '.join(value1))
#
#

#10). Write a python program to replace the words “Java” with “Python” in the given string.
# input3 = 'JAVA is the Best Programming Language in the Market'
# value3= input3.split(' ')
#
# for i in value3:
#     if i in 'JAVA':
#         index1= value3.index(i)
#         value3[index1]='Python'
# print(" ".join(value3))


# # 11. Write a Python program to create a string with a given list of words.
# input11 = ['There', 'are', 'Many', 'Programming', 'Language']
# print(" ".join(input11))

#12). Write a Python program to remove duplicate words from the string.
#
# input12 = 'john jany sabi row john sabi'
# value12 = input12.split(' ')
# output=[]
# for i in value12:
#     if i not in output:
#
#         output.append(i)
#
#
# print(output)
#13). Write a Python program to get common words from strings.
# string1 = 'Very Good Morning, How are You'
# string2= 'You are a Good student, keep it up'
# list1= string1.split(' ')
# list2=string2.split(' ')
# list3=[]
# for i in list1:
#     if i in list2:
#         list3.append(i)
# print(list3)
# #14). Write a Python program to find the smallest and largest word in a given string.
# input14 = 'Learning is a part of life and we strive'
# value14 =input14.split(' ')
# out=value14[0]
# out1=value14[0]
# for i in value14:
#     if len(i)>len(out):
#         out= i
#     if len(i)<len(out1):
#         out1= i
#
# 
# print(out,out1)

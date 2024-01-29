#1). Write a Python program to get a string made of the first and
# the last 2 chars from a given string. If the string length is less than 2,
# return instead of the empty string

# str1="tusha bhai jai n"
# # print(str1[0])
# # print(str1[-2:])
# str2=(f"{str1[0]}{str1[-2:]}")
# if len(str1)<2 :
#     print("string length is less", str1)
# else:
#     print(str2)
# # print(str2,type(str2))
#
# var1=(str1[0:1]+str1[-2:])
# #print(var1)
# if len(str1)<2 :
#     print("string length is less", str1)
# else:
#     print(var1)
#################################################################################

#2) Python string program that takes a list of strings and returns the length of the longest string.

#str2= "i am python programmer expert"
# var1=str1.split()
# word=""
# length=0
# for i in var1:
#     A=len(i)
#     if length<A:
#      length=word
#
# print(word)

#input string
# string = ["i", "am", "learning", "python"]
# temp = 0
#
# for word in string:
#     a = len(word)
#     if a > temp:
#         temp = a
#
# #Printing output
# print(temp)



# str1='hi i am neeta ghongheee'
# list1=str1.split()
# print(list1)
# longest_len=0
# longest_word=''
# for word in list1:
#
#     longest_len=len(word)
#     if longest_len>len(word):
#        longest_len=longest_len
#        longest_word=word
#
# print("longest_word:",word)
# print(longest_len)

# str10="tushar bhai is brillent boy"
# length=0
# word=""
# var=str10.split() #["tushar" bhai is brillent boy"]
# for i in var: #tushar,bhai,is,brillent,boy
#     if len(i)>length:#6>0,4>6,2>6,8>6,3>8
#         length=len(i) #6,8
#         word=i #tushar,brillent
# print(word)
# #########################################################
#
# #3). Python string program to get a string made of 4 copies of the last two
# #characters of a specified string (length must be at least 2).
#
# str11="happy newhp"
# var11=str11[-2:]*4
# print(var11)


#4). Python string program to reverse a string if it’s length is a multiple of 4.
#print("*"*60)

# str12="hppy new year hhappaji"
# if (len(str12)%4)==0:
#     print(str12[::-1])
# else:
#     print("string length is not multiple of 4")

# str12="hppy new year hhappaji is"
# var12=str12.split()
# print(var12)
#
# for i in var12:
#     if (len(i)%4)==0:
#      print(i[::-1])
########################################################
# #5). Python string program to count occurrences of a substring in a string.
#
# str13="happy new year year hinjeawadddi"
# print(str13.count("year"))
#
# #######################################################################
# #6). Python string program to test whether a passed letter is a vowel or consonant.
# print("*"*60)
# str14="welcome"
# vowel="a","A","E","e","i","I","U","u","o","O"
# for i in str14:
#     if i in(vowel):
#         print(i,"this charector is vowel")
#     else:
#        print(i,"this char is consonant")
#######################################################################
# print("*"*60)
# # 7.find Longest and smallest word in the input string
#
# str15="please inter your stringboy"
# # var15=str15.split()
# # for i in var15:
# #     print(max(var15))
# #     print(min(var15))
#
# #Input string
#
# list1 = str15.split(" ")
#
# #printing output
# print("Longest word: ", max(list1, key = len()))
# print("Smallest word: ", min(list1, key = len))

#######################################################################
#print("*"*60)


# str1 = "Helllllo ffdfdas sdfsfsd sssfdddd"
# max_repeat_count = 0
# max_repeat_char = ""
#
# temp = 1
# for i in range(len(str1)-1):
#
#     if str1[i] == str1[i+1]:
#         print(str1[i+1])
#         temp = temp + 1
#         if temp > max_repeat_count:
#             max_repeat_count = temp
#             max_repeat_char = str1[i]
#     else:
#         temp = 1
# print("Max repeated char :", max_repeat_char, "\nMax repeated count :", max_repeat_count)

#########################################################################################################
#9.Calculate the length of a string with loop logic

#Input string
# string = "im am learing python"
# A = 0
#
# for char in string:
#     print(char)
#     A +=1
#     print(A)
#
# #Printing output
# print("Length of the string using loop logic: ", A)
# print("Length of the string using len(): ", len(string))

#print("*"*60)
#Input string
# string = "im am learing python"
# #char = 0
#
# for char in range(len(string)):
#     A=char+1
#
#
# #Printing output
# print("Length of the string using loop logic: ", A)
# print("Length of the string using len(): ", len(string))
#
# print("*"*60)
# #Input string
# str1 = "Programming"
# A = ''
#
# #checking for repeated char
# for i in str1:
#     if i in A:
#         A=A+"$"
#         print(A)
#     else:
#         A=A+i
# print(A)
# print("*"*60)
#
str2="i am santosh"
a=''
for i in str2:
    a=a+i
print(a)
#
# print("*"*60)
#
# str3="i am santosh"
# a=str3[0]
# b=str3[-1:]
# c=a+b
# print(c)
#Printing output
#print("Result :", A)




# str10="tushar bhai is brillent boy"
# length=0
# word=""
# var=str10.split() #["tushar" bhai is brillent boy"]
# for i in var: #tushar,bhai,is,brillent,boy
#     if len(i)>length:#6>0,4>6,2>6,8>6,3>8
#         length=len(i) #6,8
#         word=i #tushar,brillent
# print(word)

#############################################################
# 10). Write a Python program to replace the second occurrence of any char with the special character $.
# Input = “Programming”
# Output = “Prog$am$in$”


str11="Programming"
A=""
for i in str11:
    if i in A:
        A=A+"$"
    else:
        A=A+i
print(A)
#############################################################
print("*"*60)
# 11). Write a python program to get to swap the last character of a given string.
# Input = “SqaTool”
# Output = “IqaTooS”

str12="Programming"
print(str12[-1]+str11[1:-1]+str11[0])








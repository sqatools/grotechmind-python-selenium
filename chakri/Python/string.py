#a = "python programming "
'''p = a[0:7]
print(a + p)
'''

#1). Write a Python program to get a string made of the first and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string
''''a = 'hi i have my own bike'
if len(a) < 2:
    print(True)
else:
    print(a[:2]+a[-2:])

print(len(a))


#2). Python string program that takes a list of strings and returns the length of the longest string.

a = 'sainath'
b = 'ramu'
c = 'chakradhar'
d = len(a)
e = len(b)
f = len(c)
if d > e and d > f:
    print(a,'is longest string in given ')
elif e > d and e > f:
    print(b,'is longest string in given ')
else:
    print(c,'is longest string in given ')

#3). Python string program to get a string made of 4 copies of
# the last two characters of a specified string (length must be at least 2).
a = 'chakri'
print(a[-2:]*4)


#4). Python string program to reverse a string if it’s length is a multiple of 4.

a = 'chakradh'
b = len(a)
if b%4 == 0:
    print(a[::-1])

stra = "Python Programming"
result = ''
for i in range(len(stra)):
    if i%3 == 0 and i != 0:
        result = result + "-" + stra[i]
    else:
        result = result + stra[i]
    

print("Result :", result)




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
print(strc.isalnum()) # true


strv = "Hello Program"
print(strv.isalpha())

print("%".isdigit())
print("%".isnumeric())

print('H3ll0'.isdigit())
print('%'.isdigit())
print('45/2'.isnumeric())
print('45^2'.isdigit())



al = "\u0668"
print("val :", int(val), val)

print('II'.isdigit())
print('IX'.isnumeric())
print('45^2'.isdigit())
print('$300'.isnumeric())


# program2 : write a python program to maximum repeated character.
print("_"*40)

str1 = "We arePPP learning Python Programming, ItPPPPPs very easy to learn"
max_count = 0
max_rchar = ''
temp = '' #Wea
for char in str1:
    if char not in temp and char.isspace() is False:
        print(char, str1.count(char))
        char_count = str1.count(char) #W=1, e=6, a =5, r=6, P = 10
        temp = temp + char # Wear
        if char_count > max_count: # 1 > 0 | 6 > 1 | 5 > 6 | 6 > 6 | 10 > 6
            max_count = char_count # 1, 6, 10
            max_rchar = char # W, e, P


print("max count", max_count)
print("max repeated char :", max_rchar)

#7). Find the longest and smallest word in the input string.

a = 'good cricketer and right hand bats man  '
b = a.split()
c = min(b,key = len)
d = max(b,key = len)
print(c)
print(d)

#8). Print most simultaneously repeated characters in the input string.
a = 'chakri is good cricketer and right hand bats man chakradhar '
b = a.split()
c = ''
for word in b:
    if len(word) > len(c):
        c = word
print(c)

#9). Write a Python program to calculate the length of a string with loop logic.
a = 'chakri is good cricketer and right hand bats man chakradhar '
b = 0
for i in a:
    b = b+1
print(b)
print(len(a))

#10). Write a Python program to replace the second occurrence of any char with the special character $.
a = 'Programming'
b = ''
#Output1 = 'Prog$am$:in$'
for i in a:
    if i in b:
        b = b+'$'
    else:
        b = b+i
print(b)


#11). Write a python program to get to swap the last character of a given string.
a = 'sqatool'
b = a[-1]+a[1:-1]+a[0]
print(b)

#12). Write a python program to exchange the first and last character of each word from the given string.
a = 'Its Online Learning'
#b = 'stI enlino gearninL'
b = a.split()
for i in b:
    print(i[-1]+i[1:-1]+i[0],end='  ')

#13). Write a python to count vowels from each word in the given string show as dictionary output.
a = 'We are Learning Python Codding'
#output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”}
b = a.split()
v = 'eoaiu'
c = 0
d = dict()
for word in b:
    c = 0
    for char in word:
        if char in v:
            c = c+1
        d[word] = c
print(d)

#14). Write a python to repeat vowels 3 times and consonants 2 times.
a = 'Sqa Tools Learning'
#Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg”
b = ''
v = 'eoaiu'
for char in a:
    if char in v:
        b = b+char*3
    else:
        b = b+char*2
print(b)

#15). Write a python program to re-arrange the string.
a = 'Cricket Plays Virat'
#Output = “Virat Plays Cricket”
#print(a[-6:]+' '+a[8:14]+' '+a[0:7])
l = a.split()
l.reverse()
b = str(l)
print(b)


#16). Write a python program to get all the digits from the given string.
a =  """Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen"""
#Output = [1112, 5324, 1773, 5324, 555]
b = a.split()
c = []
for word in b:
    if word.isnumeric():
        c.append(word)
print(c,end=' ')


#17). Write a python program to replace the words “Java” with “Python” in the given string.
a = 'JAVA is the Best Programming Language in the Market'
#Output = “Python is the Best Programming Language in the Market”
b = a.replace('JAVA','PYTHON')
print(b)

#19). Write a Python program to create a string with a given list of words.
a = ['There', 'are', 'Many', 'Programming', 'Language']
#Output = There are many programming languages.
b = " ".join(a)
#for word in a:
#    b = word
#    print(b,end=' ')p
print(b,type(b),type(a) )

#20). Write a Python program to remove duplicate words from the string.
#Input = “John jany sabi row john sabi”
#output = “John jany sabi row”
a = 'john jany sabi row john sabi'
b = a.split()
c = ' '
for word in b:
    if word not in c:
        c = c +' '+ word
print(c)


#21). Write a Python to remove unwanted characters from the given string.
a = 'Prog^ra*m#ming'
#Output = “Programming”
b = ''
c = []
for char in a:
    if char.isalpha():
      b = b+char
print(c)
#22). Write a Python program to find the longest capital letter word from the string.
a = 'Learning PYTHON programming LAHARI is FUN '
b = a.split()
e = 0
for word in b:
    if word.isupper():
        c = len(word)
        if c > e:
            e = c
            d = word
print(d,len(d))

#51). Write a python program to replace multiple words with certain words.
a = 'I am learning python at Sqatools'
#Replace python with SQA  and sqatools with TOOLS
b = a.replace('python','SQA').replace('sqatools','TOOLS')
print(b)

#52). Write a python program to replace different characters in the string at once.
a = 'Sqatool python'
#Replace a with 1,
#Replace t with 2,
#Replace o with 3
#Output = ‘sq1233l py2h3n”
b = a.replace('a','1').replace('t','2').replace('o','3')
print(b)

#53). Write a python program to remove empty spaces from a list of strings.
#Input lists
List1 =  ["Python", " ", " ","sqatools"]
List2 = []

for string in List1:
    if string != " ":
        List2.append(string)

#Printing output
print(List2)
#54).  Write a python program to remove punctuations from a string
a = 'Sqatools : is best, for python'
#Output = ‘Sqatools is best for python’
b = ''
for i in a:
    if i not in punc:
        b = b+i
print(b)

#55).  Write a python program to find duplicate characters in a string
a = 'hello world'
#Output = ‘lo’
b = []
c = ''
for char in a:
    if a.count(char) > 1:
        b.append(char)
print(str(set(b)))


#56).  Write a python program to check whether the string is a subset of another string or not
a = 'iamlearningpythonatsqatools'
b = 'pystlmi'
count = 0
#Output = True
c = set(a)
for char in c:
    if char in b:
        count = count+1
if len(b) == count:
    print(True)
else:
    print(False)

#57). Write a python program to sort a string
a = 'xyabkmp'
#Output = ‘abkmpxy’
print("".join(sorted(a)))
#61). Write a python program to print the index of the character in a string.
a = 'Sqatools'
#Output = ‘The index of q is 1’
b = a.index ('q')
print('the index number of q is ', b)

#62). Write a program to strip spaces from a string.
a = '    sqaltoolspythonfun     '
#Output = ‘ sqaltoolspythonfun’
b = ''
for i in a:
    if i.isalpha():
        b = b+i
print(b)
print(a.strip())

#63). Write a program to check whether a string contains all letters of the alphabet or not.
a = 'abc67dgjkvcvmsoug'
#Output = False
print(a.isalpha())

#64). Write a python program to convert a string into a list of words.
a = 'learning python is fun'
#Output = [learning, python, is, fun]
b = a.split()
c = []
for i in b:
    c.append(i)
print(c)

#65). Write a python program to swap commas and dots in a string.
a = 'sqa,tools.python'
#Output = sqa.tools,python
b = a.replace(',','.')
print(b)

#66). Write a python program to count and display the vowels in a string
a = 'welcome to Sqatools'
#Output = 7
b = 'aeiou'
c = ''
d = 0
for i in a:
    if i.lower() in b:
        d = d+1
        c = c+i
print(d,c)

#67). Write a Python program to split a string on the last occurrence of the delimiter.
a = 'l,e,a,r,n,I,n,g,p,y,t,h,o,n'
#Output = [‘l,e,a,r,n,I,n,g,p,y,t,h,o ‘ ,’n’]
print(a.split(',',1))
print(a.rsplit(',', 3))

#68). Write a Python program to find the first repeated word in a given string.
a = 'ab bc ca ab bd'
#Output = ‘ab’
a = a.split()
b = []
for i in a:
    if i in b:
        print(i)
    else:
        b.append(i)


#69). Write a program to find the second most repeated word in a given string using python.
a = 'ab bc ac ab bd ac nk hj ac'
#Output = (‘ab’, 2)
a = a.split()
b = []
for word in a:
    if word in b:
        print(word,a.count(word))
        break
    else:
        b.append(word)

#70). Write a Python program to remove spaces from a given string.
a = 'python at sqatools'
#Output = ‘pythonatsqatools’
b = ''
for i in a:
    if i.isalpha():
        b = b+i
print(b)

#71). Write a Python program to capitalize the first and last letters of each word of a given string.
a = 'this is my first program'
#Output = ‘ThiS IS MY FirsT PrograM’
for i in a.split(" "):
    print(i[0].upper()+i[1:-1]+i[-1].upper(),end= ' ')

#72). Write a Python program to calculate the sum of digits of a given string.
a = '12sqatools78'
b  = 0
#Output = 18
for i in a:
    if i.isnumeric():
        i = int(i)
        b = b+i
print(b)

#73). Write a Python program to remove zeros from an IP address.
a = '289.03.02.054'
b = ''
#Output = 289.3.2.54
for i in a:
    if i != '0':
        b = b+i
print(b)

#74). Write a program to find the maximum length of consecutive 0’s in a given binary string using python.
a = '10001100000111'
#Output = 5
a = a.split('1')
print(a)
b = (min(a,key=len))
print(len(b),b)


#75). Write a program to remove all consecutive duplicates of a given string using python.
a = 'xxxxyy'
#Output = ‘xy’
print(set(a))

#76). Write a program to create strings from a given string. Create a string that consists of multi-time occurring characters in the said string using python.
a = 'aabbcceffgh'
#Output = ‘abcf’
b = []
c = ''
for i in a:
    if a.count(i) > 1:
        if i not in b:
            b.append(i)
print(b)
b = []
for i in a:
    if a.count(i) > 1:
        b.append(i)
print(set(b))

#77). Write a Python program to create a string from two given strings combining uncommon characters of the said strings.

#Input string :
a = 'abcdefg'
b = 'xyzabcd'
c = ''
d = ''
for i in a:
    if i not in b:
        c =  c+i
print(c)
for i in b:
    if i not in a:
        d = d+i
print(c+d)


#78). Write a Python code to remove all characters except the given character in a string.
a = 'qatools pythonS'
#Remove all characters except S
#Output = ‘S’
for i in a:
    if i == 'S':
        a = 'S'
print(a)

#79). Write a program to count all the Uppercase, Lowercase, special character and numeric values in a given string using python.
a = '@SqaTools.lin'
sc = 0
uc = 0
lc = 0
#Output:
#Special characters: 1
#Uppercase characters: 2
#Lowercase characters: 8
for i in a:
    if i.isupper():
        uc = uc+1
    elif i.islower():
        lc = lc+1
    else:
        sc = sc+1
print('special characters :',sc)
print('upper case :',uc)
print('lower  case :',lc)

#81). Write a program to remove unwanted characters from a given string using python.
a = 'sqa****too^^{ls'
#Output = ‘Sqatools’
b = ''
for i in a:
    if i.isalpha():
        b = b+i
print(b)
 #82
#Input string
str1 = "Learning is fun in Sqatools"
str2 = "Sqatools Online Learning Platform"

import difflib
result =  difflib.SequenceMatcher(a=str1.lower(), b=str2.lower())

#Printing output
print(result.ratio())

#83). Write a program to extract numbers from a given string using python.
a = 'python 456 self learning 89'
#Output = [456, 89]
b = []
a = a.split()
for i in a:
    if i.isnumeric():
        b.append(i)
print(b)

#84). Write a program to split a given multiline string into a list of lines using python.
a ='This string Contains
Multiple
Lines'
#Output = [‘This string Contains’, ‘Multiple’, ‘Lines’]
a = a.split()
b = ''
for i in a:
    b = b+' '+i
print(b)

#85). Write a program to add two strings as they are numbers using python.
#Input :
a = '3'
b = '7'
#Output  = ’10’
print(int(a)+int(b))

#86). Write a program to extract name from a given email address using python.
a = 'student1@gmail.com'
b = ''
#Output = ‘student’
for i in a:
    if i.isalnum():
        b = b+i
    else:
        break
print(b)

#88). Write a program to insert space before every capital letter appears in a given word using python.
a = 'SqaTools pyThon'
#Output = ‘ Sqa Tools py Thon’
b = ''
for i in a:
    if i.isupper():
        b = b+' '+i
    else:
        b = b+i
print(b)

#89). Write a program to uppercase half string using python.
a = 'banana'
#Output = ‘banANA’
print(a[:4]+a[-3:].upper())
'''

























































































































































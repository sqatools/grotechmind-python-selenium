a = "python programming " \
    ""
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
'''
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





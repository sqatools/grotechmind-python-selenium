#######################string Method#####################

#1. upper

str1="i am doing string method practice"
print(str1.upper()) #I AM DOING STRING METHOD PRACTICE

#2.lower

str2="I am learning Lower Method for string manipulation"
print(str2.lower()) #i am learning lower method for string manipulation

#3.islower and isupper
# check given string is upper or lower

str3="I am learning Pyton islower and isupper method to check string is upper or lower"
print(str3.isupper()) #False
print(str3.islower()) #False

str4="I AM DOING STRING METHOD PRACTICE"
print(str4.isupper()) #True
print(str4.islower()) #False

str5="i am learning lower method for string manipulation"
print(str5.islower()) #True
print(str5.isupper()) # False

#4.swapcase Method converts the string upper to lower and lower to upper

str6="I Am Learning SWAPCASE Method To Converts The String UPPER To LOWER And LOWER To UPPER"
print(str6.swapcase())
#i aM lEARNING swapcase mETHOD tO cONVERTS tHE sTRING upper tO lower aND lower tO upper

#5. Title Method converts first letter is captial

str7="I am learning TITLE method to converts every first letter to upper and all other lower like initcap"
print(str7.title())
#I Am Learning Title Method To Converts Every First Letter To Upper Like Initcap

#6. istitle method to check string is title or not

str8=" I Am Learning Istitle Method To Check Given String Is Title Or Not"
print(str8.istitle()) #True

str9="I am learning istitle method to check given string is title or mot"
print(str9.istitle()) #False

#7. Index Method is used to find position of any character or substring in given string

str10="im learning index method to find out the index of any character or substring from main string"

print(str10.index('o')) #22

print(str10.index('any')) #50

#print(str10.index('tushar'))  #when string is not available #substring not found

print(str10.index('o')) #22

###find index of second o###########

count=0
for i in range (len(str10)):
    if str10[i]=='o':
        count=count+1
        if count==2: ##second occurance
            print(i)
        else:
            continue

#if substring or char is not available in main string then index method throws eroor like
#print(str10.index('tushar'))  #when string is not available #substring not found
#this is the drawback of index method so find method is introduced.

#8. Find Method

str11="I am learning find method to find position or index of particular char or string from main string"

print(str11.find('index')) #46
print(str11.find('m')) #3
print(str11.find('tushar')) # -1

#9.split method : used to split the string from specific delimeters/char/substring and return the op as list of substring

str12="I am learning split method "
print(str12.split(" ")) # ['I', 'am', 'learning', 'split', 'method', '']

str13="I Like SQL,Python and Testing"
print(str13.split(",")) #['I Like SQL', 'Python and Testing']

print(str13.split("t")) #['I Like SQL,Py', 'hon and Tes', 'ing']


stra="Hope you are doing good"
print(stra.split()) #['Hope', 'you', 'are', 'doing', 'good']
#by default parameter is space

stra="Hope you are doing good"
result=(stra.split())
print(result)

for word in result:
    print(word , word[0])

# Hope H
# you y
# are a
# doing d
# good g

#10. count method: used to count of occurances of char or substring

str14="I am learning count method to count occurance of char or substring"

print(str14.count('c')) #6

print(str14.count('count')) # 2

print("="*100)

#11. Replace method

str15="I am learning replace method to replace any substring"
print(str15.replace('replace','translate'))
#I am learning translate method to translate any substring

print(str15.replace('replace','translate').replace('I am','WE are').count('a'))



##################################################

msg="clcoding"
s=list(msg[:4])[::-1]
#print(s)

s=list(msg[:4]) [::-1]
print(s)

#['o', 'c', 'l', 'c']


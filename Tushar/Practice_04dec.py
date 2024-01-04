var1=400
print(var1)
#400 no need to specify datatype in python

var1=400
print(type(var1))
#<class 'int'> to check data type we used type function

var2="good morning"
print(var2,type(var2))
#good morning <class 'str'>

#python datatype

#1 number
# int
# float
# complex no

#2 sequential datatype
#string
#tuple
#list

#3 dictionary

#4 set

#5 boolean

#############################integer (int)########################################
#int is immutable datatypes
#there is no limit to set value for int datatypes

num1=200
num2=245881566772
num3=0
print(type(num1),type(num2),type(num3))
#<class 'int'> <class 'int'> <class 'int'>

num4=num1*2
print(num4,type(num4))
#400 <class 'int'>

num5=400*2.5
print(num5,type(num5))
#1000.0 <class 'float'>

#########################float ###########################

#flaot is immutable datatypes
#there is no limit to set value for float datatypes

var1=11.55
var2=0.01223
var3=4.87996
print(var1,type(var1))
print(var2,type(var2))
print(var3,type(var3))
#11.55 <class 'float'>
#0.01223 <class 'float'>
#4.87996 <class 'float'>

########################complex number################################

varp=50+40j
print(varp, type (varp))
#(50+40j) <class 'complex'>

####################################string##############################################

#string follow the sequence so its seq datatypes. follow the indexing
#string is also immutable data type

str1="tushar"
str2='aher'
str3="""tushar suresh aher
good morning
good day"""
str4='''my name is tushar
im from nashik
'''

str5="india won 't20' series"

str6='have "nice" day'

print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))
print(str5,type(str5))
print(str6,type(str6))

#tushar <class 'str'>
#aher <class 'str'>

#tushar suresh aher
#good morning
#good day <class 'str'>

#my name is tushar
#im from nashik
# <class 'str'>

#india won 't20' series <class 'str'>
#have "nice" day <class 'str'>


#positive index
#str= h e l l o
#negative index

str="hello"
print(str[2])
#l

######################################list#############################################

#it is kind of an array
#list defind in []
#list allows diff types of data
#list is mutable
#list folloes positive and negative index
#whenever data change randomly at that time we can use list.

list=[4,5,4.2,"apple"]
print(list,type(list))
#[4, 5, 4.2, 'apple'] <class 'list'>


list=[1,2,3,4]
list[2]=100
print (list)
#[1, 2, 100, 4]

#############################################tuple###########################################

#tuple is immutable datatype
#tuplee in ()
#accepts any kind of data int float string list tuple dict set boolean
#the internal properties of the data in tuple remains same.
#tuple folloes positive and negative index
#tuple is faster than list
#whenever data is fixed at that time we can use tple like months in year.


tup1=(1,2,8,9,'hello')
print(tup1)

tup1=(2,3,'tushar',[4,5,9],(2,7,8),7.7,{'a':400,'b':100},{10,20,30},True ,False)
print(tup1)

print(tup1[2],type(tup1))
#tushar <class 'tuple'>

var1=tup1[3]
print(var1,type(var1))
#[4, 5, 9] <class 'list'>

print(var1[1])
#5

print(tup1[3][0])
#4


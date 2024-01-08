# 1). Python Dictionary program to add elements to the dictionary.

dict={'a': 'apple','b':'ball','c':'cat'}
print(dict,type(dict))

dict['d']='dog'
print(dict)

dict['e']='elephant'
print(dict)


# 2). Python Dictionary program to print the square of all values in a dictionary.
# Input : {‘a’: 5, ‘b’:3, ‘c’: 6, ‘d’ : 8}
# Output :
# a : 25
# b : 9
# c : 36
# d : 64

dict={'a':5,'b':3,'c':6,'d':8}
dict['e']=10
print(dict)
for value in dict:
    print(value,dict[value]**2)

# 3). Python Dictionary program to move items from dict1 to dict2.
# Input :
# dict1 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}
# dict2 = {}
# Output :
# dict1 = {}
# dict2 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}

dict1={'name':'john','city':'landon','country':'uk'}

dict1['age']=35

print(dict1)

dict2={}
#
# Take one dictionary as input and create another empty dictionary.
# Use for loop to iterate over input dictionary.
# Add values from the input dictionary to the empty dictionary.
# Print the output

for val in dict1:
    print(val)
    dict2[val]=dict1[val]
print('dict2:',dict2)

#
# 4). Python Dictionary program to concatenate two dictionaries.
# Input :
# dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’}
# dict2 = {‘Age’ : 25, ‘salary’: ‘$25k’}
# Output :
# dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’, ‘Age’ : 25, ‘salary’: ‘$25k’}


dicta={'name':'harry','rollno':345,'address':'jordan'}
dictb={'age':25,'salary':'25k'}

dicta['dept']='hr'
print(dicta)

dictb['dept_id']=101
print(dictb)


dicta.update(dictb)
print("conacation:",dicta)
print(dictb)

# 5). Python Dictionary program to get a list of odd and even keys from the dictionary.
# Input :
# {1: 25, 5:’abc’, 8:’pqr’, 21:’xyz’, 12:’def’, 2:’utv’}
# Output :
# Even Key = [[8, ‘pqr’], [12, ‘def’], [2, ‘utv’]]
# Odd Key = [[1, 25], [5, ‘abc’], [21, ‘xyz’]]

dict={1:25,5:'abc',8:'pqr',21:'xyz',12:'def',2:'utv'}

dict[10]=100
print(dict)

dict2={}

dict2=dict
print('dict2:',dict2)

dict2[52]=655

dict.update(dict2)
print("dict1+dict2:",dict)

print('*'*100)

# set1={1,2,3,4,5,5,6,6,7}
# print('set:',set1)
#
# my_set=set([1,2,3,4])
# print("my_set:",my_set)

# tup=(1,2,3,4,1,2,3,4)
# my_set=set(tup)
# print("my:",my_set)
even_key=[]
odd_key=[]


for val in dict:
    if val%2==0:
        even_key.append(val)
    else:
        odd_key.append(val)
print(even_key)
print(odd_key)
######################

dict1 = {1:25,5:'abc',8:'pqr',21:'xyz',12:'def',2:'utv'}

list1 = [[val,dict1[val]] for val in dict1 if val%2 == 0]
list2 = [[val,dict1[val]] for val in dict1 if val%2 != 0]

print("Even key = ",list1)
print("Odd key = ",list2)

dict1 = {1:25,5:'abc',8:'pqr',21:'xyz',12:'def',2:'utv'}

lst1=[[val,dict1[val]]for val in dict1 if val%2==0]
lst2=[[val,dict1[val]]for val in dict1 if val%2!=0]

print("Even:",lst1)
print("odd:",lst2)


# 6). Python Dictionary Program to create a dictionary from two lists.
# Input :
# list1 = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’]|
# list2 = [12, 23, 24, 25, 15, 16]
# Output :
# {‘a’: 12, ‘b’: 23, ‘c’: 24, ‘d’: 25, ‘e’: 15}

list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [12, 23, 24, 25, 15, 16]

dict={}

for a,b in zip(list1,list2):
    dict[a]=b
print(dict)


# 7). Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
# Input :
# [4, 5, 6, 2, 1, 7, 11]
# Output :
# {4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}
# even_lst=[]
# odd_lst=[]
# lst=[4,5,6,2,1,7,11]
# for val in lst:
#     if val%2==0:
#         even_lst.append(val)
#     else:
#         odd_lst.append(val)
# print(even_lst)
# print(odd_lst)
# dict={}
# for a,b in zip(even_lst,odd_lst):
#     dict[a]=b
# print(dict)


lst=[4,5,6,2,1,7,11]
dict={}

for val in lst:
    if val%2==0:
        dict[val]=val**2
    else:
        dict[val]=val**3
print(dict)

# 8). Python Dictionary program to clear all items from the dictionary.

dict={'name':'tushar','age':25}
print(dict)

dict['city']='nashik'
print(dict)

dict.clear()
print(dict)


# 9). Python Dictionary program to remove duplicate values from Dictionary.
# Input :
# {‘a’: 12, ‘b’: 2, ‘c’: 12, ‘d’: 5, ‘e’: 35, ‘f’: 5}
# Output :
# {‘a’: 12, ‘b’: 2, ‘d’: 5, ‘e’: 35}

# Take a dictionary as input and create an empty dictionary.
# Use for loop to iterate over keys and values of the dictionary using dictionary.items().
# If the value is not in the list then add that value and its key to the empty dictionary.
# Print the output.

dict={'a': 12, 'b': 2, 'c': 12, 'd': 5, 'e': 35, 'f': 5}

x=dict.items()
print(x)

dict1={}

for key,value in dict.items():
    if value not in dict1.values():
        dict1[key]=value
print(dict1)





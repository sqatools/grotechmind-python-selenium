# 1). Python program to calculate the square of each number from the given list.
"""
list=[10,20,88,99,5,7]
for val in list:
 print("square of no:",val,val**2)

"""


# 2). Python program to combine two lists.
"""
lst1=[10,88.55,2,7,9,100]

lst2=[88,66,2,33,77,45]

lst3=lst1+lst2
print(lst3) #[10, 88.55, 2, 7, 9, 100, 88, 66, 2, 33, 77, 45]
"""
'''
lst1=[10,88.55,2,7,9,100]

lst2=[88,66,2,33,77,45]

lst1.extend(lst2)

print(lst1) #[10, 88.55, 2, 7, 9, 100, 88, 66, 2, 33, 77, 45]
'''

# 3). Python program to calculate the sum of all elements from a list.
'''
lst1=[1, 8 ,9 ,10,88,900 ]
sum=0
for val in lst1:
    sum=sum+val
print(sum)

'''
"""
lst1=[1, 8 ,9 ,10,88,900 ]

count=0
total=0

while count<len(lst1):

    total=total+lst1[count]
    count=count+1
print(total)
"""
'''
lst1=[1, 8 ,9 ,10,88,900 ]

print(sum(lst1))
'''
"""
lst2=[10,20,80,95,100]
total=0
for val in lst2:
    total=total+val
print(total)

"""
"""
lst2=[10,20,80,95,100]

count=0
total=0

while count<len(lst2):
    total=total+lst2[count]
    count=count+1
print(total)
"""
'''
lst2=[10,20,80,95,100]
print(sum(lst2))
'''


# 4). Python program to find a product of all elements from a given list.
'''
lst=[1,8]

product=1
for val in lst:
    product=product*val
print(product) #8

'''
'''
lst=[1,8,9]

product=1
count=0

while count<len(lst):
    product=product*lst[count]
    count=count+1
print(product)

'''


# 5). Python program to find the minimum and maximum elements from the list
"""
lst=[10,20,30,40,50]

lst.sort()

print("min no:",lst[0])
print("max no:",lst[-1])

"""
"""
lst=[10,20,30,40,50]
print("min:",min(lst))
print("max:",max(lst))
"""
'''
lst=[10,80,90,77,1000]

lst.sort()

print("min:",lst[0])
print("max:",lst[-1])
'''
'''
lst=[40,70,90,2,55,222]

print(min(lst))
print(max(lst))

'''

# 6). Python program to differentiate even and odd elements from the given list.
"""
lst=[70,50,56,87,95,23,50,87]

odd=[]
even=[]

for val in lst:
    if val%2==0:
        even.append(val)
    else:
        odd.append(val)
print(odd)
print(even)
"""
"""
lst=[70,80,90,55,25,32,45,32,90]

odd=[]
even=[]

for val in lst:
    if val%2==0:
        even.append(val)
    else:
        odd.append(val)
print(odd)
print(even)
"""


# 7). Python program to remove all duplicate elements from the list.
"""
lst=[10,20,30,10,30,50,60]

new_lst=[]

for val in lst:
    if val not in new_lst:
        new_lst.append(val)
print(new_lst)

"""

# 8). Python program to print a combination of 2 elements from the list whose sum is 10.

# lst=[2,5,8,5,1,9]
#
# import itertools
#
# var=10
#
# lst2=[]
#
# for val in range (len(lst)):
#
#     for combi in itertools.combinations(lst,val):
#         if sum(combi)==var:
#             lst2.append(combi)
# print(lst2)



'''

#Importing itertools
import itertools

#Input list
list1 = [0,1,2,3,4,5,6,7,8,9,10]

#Creating variable
var = 10

#Creating empty list
list3 = []

for i in range(len(list1)):
    for combi in itertools.combinations(list1,i):
        if sum(combi) == var:
            list3.append(combi)

#Printing output
print(list3)

'''


# 9). Python program to print squares of all even numbers in a list./

'''
lst=[1,2,3,4,5,6,7,8,9,10]

for val in lst:
    if val%2==0:
        print(val**2)
    else:
        continue
'''

# 10). Python program to split the list into two-part, the left side all odd values and the right side all even values.
# Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]
# Output = [5, 7, 11, 17, 19, 2, 8, 12, 22]
"""

lst=[5, 7, 2, 8, 11, 12, 17, 19, 22]
even=[]
odd=[]

for val in lst:
    if val%2==0:
        even.append(val)
    else:
       odd.append(val)
odd.extend(even)

print(odd)

"""
"""
lst=[5, 7, 2, 8, 11, 12, 17, 19, 22]

odd=[]
even=[]

for val in lst:
    if val%2==0:
        even.append(val)
    else:
        odd.append(val)
odd.extend(even)
print("new:",odd)
"""

# 11).  Python program to get common elements from two lists.
# Input =
# list1 = [4, 5, 7, 9, 2, 1]
# list2 = [2, 5, 8, 3, 4, 7]
# Outputt : [4, 5, 7, 2]


# lst1 = [4, 5, 7, 9, 2, 1]
# lst2 = [2, 5, 8, 3, 4, 7]
#
# new_lst=[]
#
# for val in lst1:
#     for val2 in lst2:
#         if val==val2:
#             new_lst.append(val)
# print(new_lst)
#

"""
list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]

new_list=[]

for val in list1:
    for val2 in list2:
        if val==val2:
            new_list.append(val2)
print(new_list)

"""


# 12). Python program to reverse a list with for loop.

# lst=[10,20,80,5,90]
#
# for val in range(len(lst)-1,-1,-1):
#     print(lst[val],end=' ')

"""
lst=[10,80,90,50,20]

for i in range(len(lst)-1,-1,-1):
    print(lst[i])

"""

# 13). Python program to reverse a list with a while loop.
#using slicing


# 14). Python program to reverse a list using index slicing.
"""
lst=[10,90,80,20,50]

new_lst=lst[::-1]

print(new_lst)
"""


# 15). Python program to reverse a list with reversed and reverse methods.
##using reverse fun:

"""
lst=[10,90,80,20,50]

lst.reverse()

print(lst)

"""
"""
lst=[10,90,80,20,50]

print("reversed:",list(reversed(lst)))
print(lst)
lst.reverse()
print("reverse:",lst)

print(lst)

"""
"""

lst=[10,90,80,20,50]

new_lst=[]

for i in lst:
    new_lst.insert(0,i)
    
print(new_lst)

"""

# 16). Python program to copy or clone one list to another list.
"""
lst1=[10,20,90,50,70]

new_lst=[]

new_lst=lst1.copy()

print(new_lst)
print(lst1)
"""

"""
list1 = [1,2,4,7,0,5]

list2 = []

for value in list1:
    list2.append(value)

print(list2)
print(list2)
"""


# 17). Python program to return True if two lists have any common member.
"""
lst1=[10,20,30,40,50]
lst2=[60,70,80,90,100,10]

for val1 in lst1:
    for val2 in lst2:
        if val1==val2:
            print(True)
"""

# 18). Python program to print a specific list after removing the 1st, 3rd, and 6th elements from the list.
 #wrong q
# lst1=[10,20,30,40,50,60,70,80,90,100]
#
# lst1.remove(10,)
#
# print(lst1)

# 19). Python program to remove negative values from the list.

lst=[10,20,30,-70,80,-60]
"""
for val in lst:
    if val >=0:
        print(val)
"""


"""
# 20). Python program to get a list of all elements which are divided by 3 and 7.

lst=[3,6,9,12,7,17,21,28,35,42,63,88]
new_list=[]
for val in lst:
    if val%3==0 and val%7==0:
        new_list.append(val)
print(new_list)
"""

# 21). Python program to check whether the given list is palindrome or not. (should be equal from both sides).
"""
lst=[11,15,15]

if lst==lst[::-1]:
    print("palindrome")
else:
    print("not palindrome")
"""

# 22). Python Program to get a list of words which has vowels in the given string.
# Input: “www Student ppp are qqqq learning Python vvv”
# Output : [‘Student’, ‘are’, ‘learning’, ‘Python’]

"""
str1='www Student ppp are qqqq learning Python vvv'

lst=[]

str2=str1.split()

for word in str2:
    for char in word:
        if char=='a'or char=='e'or char=='i'or char=='o'or char=='u':
            lst.append(word)
            break
print(lst)

"""


# 23). Python program to add 2 lists with extend method.
"""
lst1=[10,20,30,40,50]

lst2=[60.40,70,80,45,89]

lst2.extend(lst1)
print(lst1)
print(lst2)
"""

# 24). Python program to sort list data, with the sort and sorted method.
"""
lst=[84,54,12,87,65,2,4,1,0,85]
lst2=sorted(lst)
print(lst)
print(lst2)

lst.sort()
print(lst)
"""
# sort() directly modifies the original list, while sorted() keeps the original list intact and creates a new sorted list.
# This means that if you need to preserve the original order, sorted() is the safer choice.


# 25). Python program to remove data from the list from a specific index using the pop method.

"""
lst=[10,80,95,23,12,45]

lst.pop(2)
print(lst)
"""

# 26). Python program to get the max, min, and sum of the list using in-built functions.
"""
lst=[10,20,80,90,70,123]

print(max(lst))
print(min(lst))
print(sum(lst))
"""

# 27). Python program to check whether a list contains a sublist.

# Take two lists as input.
# Check whether list2 is a sublist of list1 (i.e. all the elements from the list2 are in list1.
# Use for loop for this purpose.
# Print the output.
"""
lst1=[10,20,30,40,50,60,70,80,90]
lst2=[40,10,20,90]
count=0
for val1 in lst1:
    for val2 in lst2:
        if val1==val2:
            count=count+1
if count==len(lst2):
    print("lst2 is sublist of lst1")
else:
    print("lst2 is not sublist of lst1")
"""
"""
lst1=[78,89,45,56,12,23]
lst2=[45,56,12,1]

count=0

for val1 in lst1:
    for val2 in lst2:
        if val1==val2:
            count=count+1
if count==len(lst2):
    print("list2 is sublist of list1")
else:
    print("list2 is not sublist of list1")

"""


# 28). Python program to generate all sublists with 5 or more elements in it from the given list.

# Take a list as input and create an empty list to store and generate all sublists.
# From itertools import combinations for generating sublists with 5 or more elements.
# Use for loop and range function for this purpose.
# If the generated list contains 5 or more elements add that list as a sublist to the empty list.
# Print the list to see the output.


# 29). Python program to find the second largest number from the list.

lst=[10,80,90,20,30]

# Take a list as input.
# Sort the list using sort().
# Print the second largest number from the list using indexing
"""
lst.sort()

print(lst)

print(lst [-2])
"""


# 30). Python program to find the second smallest number from the list.
"""
lst=[10,80,90,24,32,12,1,2]

lst.sort()
print(lst[1])
"""


# 31). Python program to merge all elements of the list in a single entity using a special character.
"""
lst=['a','b','c','d','e']

# Take a list of characters as input.
# Join the characters from the list using join() to merge all elements.
# Use “$” to join the character.
# Print the output.

print("$".join(lst))

"""
#
# num=4
# fact=1
#
# for i in range (num,0,-1):
#     print(i)
#     fact=fact*i
# print(fact)



# 32). Python program to get the difference between two lists.
"""

lst=[10,20,30]
lst2=[40,50,60]

new=[]
for val in lst:
    if val not in lst2:
        new.append(val)
print(new)
"""

























































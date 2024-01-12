# 1). Python tuple program to create a tuple with 2 lists of data.
# Input lists:
# list1 = [4, 6, 8]
# list2 = [7, 1, 4]
# Output= ((4, 7), (6, 1), (8, 4))

# Take two lists as input.
# Combine elements having the same index no using zip() and convert that list into a tuple using tuple().
# Print the output.
"""
list1 = [4, 6, 8]
list2 = [7, 1, 4]
tup =tuple(zip(list1,list2))
print(tup) #((4, 7), (6, 1), (8, 4))

"""
"""
lst1= [1, 2, 3]
lst2= [4, 5, 6]
tup=tuple(zip(lst1,lst2))
print(tup)
"""

# 2). Python tuple program to find the maximum value from a tuple.
# Input = (41, 15, 69, 55)
# Output = 69

# tuple = (41, 15, 69, 55)
#
# op=(max(tuple))
# print(op)

# 3). Python tuple program to find the minimum value from a tuple.
# Input = (36,5,79,25)
# Output = 5

# tup=(36,5,79,25)
# op=min(tup)
# print(op)

#
# 4). Python tuple program to create a list of tuples from a list having a number and its square in each tuple.
# Input = [4,6,3,8]
# Output = [ (4, 16), (6, 36), (3, 9), (8, 64) ]
"""
lst=[4,6,3,8]

lst2=[]

for val in lst:
    sqaure=val**2
    lst2.append(sqaure)
op=list(zip(lst,lst2))
print(op)
"""

# Take a list as input.
# Use the list comprehension method to create a list of tuples from a list having a number and its square in each tuple.
# Use for loop to iterate over elements in the list and use pow() to get the square of the elements.
# Perform the above operations inside a list to achieve list comprehension.
# Print the output.
"""
list1 = [4,6,3,8]

tup = [(val, pow(val, 2)) for val in list1]
print(tup)

"""

# 5). Python tuple program to create a tuple with different datatypes.
# Output= ( 2.6, 1, ‘Python’, True, [5, 6, 7], (5, 1, 4), {‘a’: 123, ‘b’: 456})

# You can simply create a tuple with different datatypes by adding elements with different datatypes in () to create a  tuple.
# Print the output.
"""
tup = (2.6,1,'Python',True,[5, 6, 7],(5, 1, 4),{'a':123,'b':456})
print("Tuple: ",tup)
"""
#
# 6). Python tuple program to create a tuple and find an element from it by its index no.
# Input = (4, 8, 9, 1)
# Index = 2
# Output = 9



# Create a tuple.
# Find the element from the tuple having index number 2 using tuple_name[index number].
# Print the output.
"""
tup = (4, 8, 9, 1)
print(tup[2])
"""

# 7). Python tuple program to assign values of tuples to several variables and print them.
# Input = (6,7,3)
# Variables = a,b,c
# Output:
# a, 6
# b, 7
# c, 3

# Create a tuple.
# Assign values of tuples to several variables by using variable_names=tuple.
# Print the variable name and their value.
"""
tup=(6,7,3)
(a,b,c)=tup
print(a)
print(b)
print(c)

"""

# 8). Python tuple program to add an item to a tuple.
# Input= ( 18, 65, 3, 45)
# Output=(18, 65, 3, 45, 15)

# Create a tuple.
# Convert the tuple into a list using list().
# Now add an item to the list using append().
# Then convert the list into a tuple using tuple().
# Print the output.
"""
tup= ( 18, 65, 3, 45)
lst=list(tup)
print(lst)
lst.append(15)
print(lst)
tup=tuple(lst)
print(tup)
"""

# 9). Python tuple program to convert a tuple into a string.
# Input = (‘s’, ‘q’, ‘a’, ‘t’, ‘o’, ‘o’, ‘l’, ‘s’)
# Output = Sqatools

# Create a tuple having characters and create an empty string.
# Use for loop to iterate over characters in the tuples and add each character to the empty string.
# Print the output.
"""
tup = ('s','q','a')

str=''

for char in tup:
    str=str+char
print(str)
"""

# 10). Python tuple program to get the 2nd element from the front and the 3rd element from the back of the tuple.
# Input = (‘s’, ‘q’, ‘a’, ‘t’, ‘o’, ‘o’ ,’l’, ‘s’)
# Output=
# q
# o


# tup = ('s','q','a','t','o','o','l','s')
# print(tup[1])
# print(tup[-3])

#
# 11). Python tuple program to check whether an element exists in a tuple or not.
# Input = ( ‘p’ ,’y’, ‘t’, ‘h’, ‘o’, ‘n’)
# P in A
# Output=
# True
"""
tup= ('p','y','t','h','o','n')

if 'q' in tup:
    print('true')
else:
        print('false')
        
"""

# 12). Python tuple program to add a list in the tuple.
# Input:
# L=[12,67]
# A=(6,8,4)
# Output:
# A=(6,8,4,12,67)

# tup=(6,8,4)
# lst=[12,67]
#
# lst2=list(tup)
# print(lst2)
# lst2.append(lst)
# print(lst2)
# tup1=tuple(lst2)
# print(tup1)

# Create a list and a tuple.
# Convert the tuple into a list using list() and add another list to it using ” + “.
# Now convert the combined list to a tuple using tuple().
# Print the output
"""
list1 = [12,67]
tup = (6,8,4)
result = tuple(list(tup) + list1)
print(result)
"""

#
# 13). Python tuple program to find sum of elements in a tuple.
# Input:
# A=(4,6,2)
# Output:
# 12
"""
tup=(4,6,2)

total=0

for val in tup:
    total=total+val
print(total)
"""
"""
tup = (4,6,2)
print("Sum of elements in the tuple: ",sum(tup))

"""



# 14). Python tuple program to add row-wise elements in Tuple Matrix
# Input:
# A = [[(‘sqa’, 4)], [(‘tools’, 8)]]
# B = (3,6)
# Output:
# [[(‘sqa’, 4,3)], [(‘tools’, 8,6)]]

tup1 = [[('sqa’, 4)], [(''tools', 8)]]
tup2 = (3,6)





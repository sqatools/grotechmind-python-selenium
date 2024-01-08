"""

# 1). Python program to calculate the square of each number from the given list.
print("1). Python program to calculate the square of each number from the given list.")

list1 = [3, 5, 7, 1, 8]
for val in list1:
	square = val**2
	print(val ,":", square)

print()
# or

list1 = [3, 5, 7, 1, 8]
count = 0
while count < len(list1):
	square = list1[count]**2
	print(list1[count] , ":" , square)
	count= count+1

# 2). Python program to combine two lists.
print("2). Python program to combine two lists.")

# Append method

list1 = [2,4,1,56,78,88]
list2 = [32,43,54,65,76]

list1.append(list2)
print(list1)

# concatenation of list data (+ operater method)
list1 = [2,4,1,56,78,88]
list2 = [32,43,54,65,76]

list3 = list1+list2
print(list3)

# insert method
list1 = [2,4,1,56,78,88]
list2 = [32,43,54,65,76]

list1.extend(list2)
print(list1)

print("%"*50)

# for loop condition with addition without repeating same number
list1 = [20,21,22,34,45,67,89,90]
list2 = [21,20,65,22,76,87,98]
ele = set( )
list3 =[ ]

for val1,val2 in zip(list1,list2):
	if val1 not in ele:
		list3.append(val1)
		ele.add(val1)
	if val2 not in ele:
		list3.append(val2)
		ele.add(val2)
print(sorted(list3))

# 3). Python program to calculate the sum of all elements from a list.
print("3). Python program to calculate the sum of all elements from a list.")

list1 = [2,3,4,5,6,7,8,9]
ele = 0
for val in list1:
	ele = ele+val
	print(ele, end=" ")
print()
print("sum of element: ", ele)

"""



















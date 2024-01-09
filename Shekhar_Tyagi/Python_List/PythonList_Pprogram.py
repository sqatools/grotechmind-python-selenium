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

# 4). Python program to find a product of all elements from a given list.
print("4). Python program to find a product of all elements from a given list.")

list1 = [3,9,4,8]
result = 1

for val in list1:
	result = result * val
print(result)

# or

list1 = [3,9,4,8]

result = 1
count = 0
while count < len(list1):            # 0<4, 1<4,2<4,3<4
	result = result * list1[count]   # 3,27,108,864
	count=count+1
print(result)


# 5). Python program to find the minimum and maximum elements from the list.
print("5). Python program to find the minimum and maximum elements from the list.")

print("Method 1 : Sorting and indexing")

list1 = [2,3,9,4,8,23,21]
list1.sort()
print(list1)
print(list1[0])
print(list1[-1])

print("Method 2 : Using in-built function")

list1 = [26,32,90,14,28,23,21]
print(min(list1))
print(max(list1))

# 6). Python program to differentiate even and odd elements from the given list.
print("6). Python program to differentiate even and odd elements from the given list.")

list1 = [26,32,90,14,28,23,21]
Even = []
Odd = []

for val in list1:
	if val%2 ==0:
		Even.append(val)
	else:
		Odd.append(val)
print("Even Value: ",Even)
print("Odd value: ",Odd)

# 7). Python program to remove all duplicate elements from the list.
print("7). Python program to remove all duplicate elements from the list.")

list1 = [26,32,90,14,32,14,28,23,22]

result = []

for val in list1:
	if val not in result:
		result.append(val)
print("Result : ", sorted(result))

# 8). Python program to print a combination of 2 elements from the list whose sum is 10.
print("8). Python program to print a combination of 2 elements from the list whose sum is 10.")
import itertools
list1 = [2,4,6,5,7,8,9,1,14]
val = 10
list2 =[ ]
list3 = []

for i in range(len(list1)):
	for j in itertools.combinations(list1,i):
			if sum(j) == val:
					list2.append(j)
print("Combination of 2 element: ", list2)

"""

























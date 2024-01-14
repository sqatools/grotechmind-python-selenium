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


# 9). Python program to print squares of all even numbers in a list.
print("9). Python program to print squares of all even numbers in a list.")

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list2 = [ ]
for val in list1:
	if val%2==0:
		list2.append(val)
print(list2)


# 10). Python program to split the list into two-part, the left side all odd values and the right side all even values.
# Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]
print("10). Python program to split the list into two-part, the left side all odd values and the right side all even values.")

list1 = [5, 7, 2, 8, 11, 12, 17, 19, 22]
odd = [ ]
even = [ ]
for char in list1:
	if char % 2 != 0:
		odd.append(char)
	else:
		even.append(char)
odd.extend(even)
print(odd)


# 11).  Python program to get common elements from two lists.
# Input =
# list1 = [4, 5, 7, 9, 2, 1]
# list2 = [2, 5, 8, 3, 4, 7]
print("11).  Python program to get common elements from two lists.")

list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]

comman_list = list(set(list1) & set(list2))
print(comman_list)

# or

list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
comman_list = []
for i in list1:
	if i in list2:
		comman_list.append(i)
print(comman_list)

# 12). Python program to reverse a list with for loop.
print("12). Python program to reverse a list with for loop.")

list1 = [4, 5, 7, 9, 2, 1]
for i in range(len(list1)-1,-1,-1):
	print(list1[i],end=" ")
print()

# 13). Python program to reverse a list with a while loop.
print("13). Python program to reverse a list with a while loop.")

list0 = [4, 5, 7, 9, 2, 1]
list0.sort()
print(list0)
num1 = len(list0) - 1
while num1 >= 0:
	list1 = (list0[num1])
	print(list1,end=" ")
	num1 -=1
# 14). Python program to reverse a list using index slicing.
print("14). Python program to reverse a list using index slicing.")

list0 = [4, 5, 7, 9, 2, 1]
list0.sort()
print(list0)
result = list0[::-1]
print(result)


# 15). Python program to reverse a list with reversed and reverse methods.
print("15). Python program to reverse a list with reversed and reverse methods.")

list0 = [4, 5, 7, 9, 2, 1]
list0.sort()
result = list(reversed(list0))
list0.reverse()
print(result)
print(list0)


# 16). Python program to copy or clone one list to another list.
print("16). Python program to copy or clone one list to another list.")

list1 = [4, 5, 7, 9, 2, 1]
#list1.sort()
#print(list1)
list2 = [ ]

for val in list1:
	list2.append(val)
print(list2)

list2.sort()
print(list2)

print(sorted(list2))


# 17). Python program to return True if two lists have any common member.
print("17). Python program to return True if two lists have any common member.")

list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
sorted(list1)
sorted(list2)
print(list1,'\n',list2)
for val in list1:
	if val in list2:
		print("Common value :",True)
	else:
		print("common value: ",False)


# 18). Python program to print a specific list after removing the 1st, 3rd, and 6th elements from the list.
print("18). Python program to print a specific list after removing the 1st, 3rd, and 6th elements from the list.")

list1 = [4, 5, 7, 9, 2, 1,12,14]

list2 = [0,2,5]
for val, element in enumerate(list1):
	if val not in list2:
		print(element, end=" ")
print()


# 19). Python program to remove negative values from the list.
print("19). Python program to remove negative values from the list.")

list1 = [3,5,-8,0,-20,-55,23,-10]
for val in list1:
	if val>= 0:
		print(val, end=" ")


# 20). Python program to get a list of all elements which are divided by 3 and 7.
print("20). Python program to get a list of all elements which are divided by 3 and 7.")

list1 = [3,7,0,2,6,14,88,21]

list2 = []

for i in list1:
	if i % 3==0:
		list2.append(i)
	elif i % 7 == 0:
		list2.append(i)
print(sorted(list2))


# 21). Python program to check whether the given list is palindrome or not.
print("21). Python program to check whether the given list is palindrome or not.")

list1 = [2,4,6,6,4,2]
list2 = list1[::-1]
if list2 == list1:
	print("List is palindrome")
else:
	print("List is not palindrome")


# 22). Python Program to get a list of words which has vowels in the given string.
# Input: “www Student ppp are qqqq learning Python vvv”
print("22). Python Program to get a list of words which has vowels in the given string.")

string=  "www Student ppp are qqqq learning Python vvv"
string1 = string.split()
list1  = []

for char in string1:
	for word in char:

		if word =="1" or word=="e" or word=="i" or word=="o" or word=="u" or word=="A" or word=="E" or word=="I" or word=="O" or word=="U":
			list1.append(char)
			break
print(list1)

"""

# 23). Python program to add 2 lists with extend method.
print("23). Python program to add 2 lists with extend method.")

list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
list3 = []
for val in list1:
	if val not in list2:
		list3.append(val)
		list1.extend(list3)
print(list1)














































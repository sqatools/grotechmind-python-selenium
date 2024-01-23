
# 1). Python program to create a set with some elements.
print("1). Python program to create a set with some elements.")

set1 = {1,2,3,4,5,'shekhar' , True}
print("Set:", set1)

# 2). Python program to add an element to a set.
print("2). Python program to add an element to a set.")

set1 = {1,2,3,4,5,'shekhar' , True}
set1.add('Sanat')
print("set1:", set1)

# 3). Python program to remove an element from a set.
print("3). Python program to remove an element from a set.")

set1 = {1,2,3,4,5,'shekhar' , True}
set1.remove(5)
print(set1)

# 4). Python program to find the length of a set.
print("4). Python program to find the length of a set.")

set1 = {1,2,3,4,5,'shekhar'}
print(len(set1))

# 5). Python program to check if an element is present in a set.
print("5). Python program to check if an element is present in a set.")

set1 = {1,2,3,4,5,'shekhar'}
if 'shekhar' in set1:
	print(True)
else:
	print(False)

# 6). Python program to find the union of two sets.
print("6). Python program to find the union of two sets.")

set1 = {1,2,3,4,5,12,13,14}
set2 = {7,6,12,15}

print(set1.union(set2))

# 7). Python program to find the intersection of two sets.
print("7). Python program to find the intersection of two sets.")

set1 = {1,2,4,5}
set2 = {7,8,9,1,2}
print(set1.intersection(set2))

# 8). Python program to find the difference of two sets.
print("8). Python program to find the difference of two sets.")

set1 = {1,2,4,5}
set2 = {7,8,9,1}
print(set1.difference(set2))

# 9). Python program to find the symmetric difference of two sets.
print("9). Python program to find the symmetric difference of two sets.")

set1 = {1,2,4,5}
set2 = {7,8,9,1}
print(set1.symmetric_difference(set2))

# 10). Python program to show if one set is a subset of another set.
print("10). Python program to show if one set is a subset of another set.")

set1 = {1,2,4,5}
set2 = {1,2}
print(set2.issubset(set1))

# 11). Python program to check if two sets are disjoint.
print("11). Python program to check if two sets are disjoint.")

set1 = {1,2,4,5}
set2 = {7,8,9}
print(set2.isdisjoint(set1))

# 12). Python program to convert a list to a set.
print("12). Python program to convert a list to a set.")

list1 = [1,2,4,5,6]
set1 = set(list1)
print(set1)

# 13). Python program to convert a set to a list.
print("13). Python program to convert a set to a list.")

set1 = {1,2,4,5,6}
list1 = list(set1)
print(list1)

# 14). Python program to find the maximum element in a set.
print("14). Python program to find the maximum element in a set.")

set1 = {1,2,3,4,55,12,13,14}

print(max(set1))

# Or

large = 0
for ele in set1:
	if ele > large:
		large = ele
print(large)

# 15). Python program to find the minimum element in a set.
print("15). Python program to find the minimum element in a set.")

set1 = {1,2,3,4,55,12,13,14}
print(min(set1))

# or

minimum = max(set1)
for ele in set1:
	if ele < minimum:
		minimum = ele
print(minimum)

# or

min1 = next(iter(set1))
for ele in set1:
	if ele < min1:
		min1 = ele
print(min1)

# 16). Python program to find the sum of elements in a set.
print("16). Python program to find the sum of elements in a set.")

set1 = {1,2,3,4,55,12,13,14}

sum_set = sum(set1)
print(sum_set)

# or

val = 0
for ele in set1:
	val = val+ele
print(val)

# 17). Python program to find the average of elements in a set.
print("17). Python program to find the average of elements in a set.")

set1 = {1,2,3,4,55,12,13,14}
len_of_set = len(set1)
print(len_of_set)
total = 0
for ele in set1:
	total = total+ele
print("Avg of set1:", total/len_of_set)

# or

set1 = {1,2,3,4,55,12,13,14}

sum_of_set1 = sum(set1)
len_of_set1 = len(set1)
avg = sum_of_set1/len_of_set1
print("avg of set2:", avg)

# 18). Python program to check if all elements in a set are even.
print("18). Python program to check if all elements in a set are even.")

set1 = {1,2,3,4,5}
char = 0

for ele in set1:
	if ele%2 == 0:
		char= char+1
		print(char)
if char == len(set1):
	print("elements in the set are even")
else:
	print("elements in the set are not even")

# 19). Python program to check if all elements in a set are odd.
print("19). Python program to check if all elements in a set are odd.")

set1 = {1,2,3,4,5}
char = 0

for ele in set1:
	if ele%2 != 0:
		char= char+1
		print(char)
if char == len(set1):
	print("elements in the set are odd")
else:
	print("elements in the set are not odd")

# 20). Python program to check if all elements in a set are prime.
print("20). Python program to check if all elements in a set are prime.")

set1 = {1,2,3,4,5}
list1 = []

for ele in set1:
	print("ele:",ele)
	count = 0
	for num in range(2,ele):
		print("num:",num)
		if ele%num ==0:
			count = count+1
			print("count:",count)
	if count ==0:
		list1.append(ele)
if len(list1) == len(set1):
	print("All the element in set are prime ")
else:
	print("All the element in set are not prime ")
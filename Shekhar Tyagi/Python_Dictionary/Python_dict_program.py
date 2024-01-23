
# 1). Python Dictionary program to add elements to the dictionary.
print("1). Python Dictionary program to add elements to the dictionary.")

dict1 = {}
dict1["Name"] = "Shekhar Tyagi"
dict1["age"] = 26
dict1["Contact"] = 9760939256
print(dict1)

# 2). Python Dictionary program to print the square of all values in a dictionary.
print("2). Python Dictionary program to print the square of all values in a dictionary.")

dict1 = {'a': 5, 'b':3, 'c': 6, 'd' : 8}
for val in dict1:
	print(val ,":" , dict1[val]**2)

# 3). Python Dictionary program to move items from dict1 to dict2.
print("3). Python Dictionary program to move items from dict1 to dict2.")

dict1 = {'name': 'john', 'city': 'Landon', 'country': 'UK'}
dict2 = {}
for val in dict1:
	dict2[val] = dict1[val]
print("dict2:",dict2)

# 4). Python Dictionary program to concatenate two dictionaries.
print("4). Python Dictionary program to concatenate two dictionaries.")

dict1 = {'Name': 'Harry', 'Rollno':345, 'Address': 'Jordan'}
dict2 = {'Age' : 25, 'salary': '$25k'}

dict1.update(dict2)
print(dict1)

# 5). Python Dictionary program to get a list of odd and even keys from the dictionary.
print("5). Python Dictionary program to get a list of odd and even keys from the dictionary.")

dict1 = {1: 25, 5:'abc', 8:'pqr', 21:'xyz', 12:'def', 2:'utv'}

even_list =[[val, dict1[val]] for val in dict1 if val%2 ==0]
odd_list = [[val, dict1[val]] for val in dict1 if val%2 !=0]

print("even_list:", even_list)
print("odd_list:",odd_list)

# 6). Python Dictionary Program to create a dictionary from two lists.
print("6). Python Dictionary Program to create a dictionary from two lists.")

list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [12, 23, 24, 25, 15, 16]

dict1 = {}
comb_list= list(zip(list1,list2))
# print(comb_list)
for ele1 , ele2 in comb_list:
	dict1[ele1] = ele2
print(dict1)

# 7). Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
print("7). Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.")

list1= [4, 5, 6, 2, 1, 7, 11]
dict1 = {}
for val in list1:
	if val%2 ==0:
		dict1[val] =val**2
	else:
		dict1[val] = val**3
print(dict1)

# 8). Python Dictionary program to clear all items from the dictionary.
print("8). Python Dictionary program to clear all items from the dictionary.")

dict1 = {4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}
dict1.clear()
print(dict1)

# 9). Python Dictionary program to remove duplicate values from Dictionary.
print("9). Python Dictionary program to remove duplicate values from Dictionary.")

dict1 = {'a': 12, 'b': 2, 'c': 12, 'd': 5, 'e': 35, 'f': 5}
dict2 = {}
list1 = []

for key , val in dict1.items():
	if val not in dict2.values():
		dict2[key] = val
print(dict2)

# 10). Python Dictionary program to create a dictionary from the string.
print("10). Python Dictionary program to create a dictionary from the string.")

string  = 'SQATools'
dict1 = {}
for char in string:
	dict1[char] = string.count(char)
print(dict1)

# 11). Python Dictionary program to sort a dictionary using keys.
print("11). Python Dictionary program to sort a dictionary using keys.")

dict1 = {'d' : 21, 'b' : 53,  'a': 13, 'c': 41}
sort_dict = sorted(dict1)
for key in sort_dict:
	print("%s : %s" % (key, dict1[key]))

# 12). Python Dictionary program to sort a dictionary in python using values.
print("12). Python Dictionary program to sort a dictionary in python using values.")

dict1 = {'d' : 14, 'b' : 52,  'a': 13, 'c': 1 }

result = {key : value for key , value in
		  sorted(dict1.items() , key = lambda item: item[1])}
print(result)

# 13). Python Dictionary program to add a key in a dictionary.
print("13). Python Dictionary program to add a key in a dictionary.")

dict1 = {1:'a', 2:'b'}
dict1.update({3:'c'})
dict1.update({5 : 'd'})
print(dict1)

# 14). Python Dictionary program to concatenate two dictionaries.

dict1 = {'name' : 'yash', 'city' :  'pune'}
dict2 = {'course' : 'python', 'institute' : 'sqatools'}

dict1.update(dict2)
print(dict1)

# 15). Python Dictionary program to swap the values of the keys in the dictionary.
print("15). Python Dictionary program to swap the values of the keys in the dictionary.")

dict1 = {'name':'yash', 'city': 'pune'}
dict2 = {}
for key , value in dict1.items():
	dict2[value] = key
print(dict2)

# or
print("$"*40)
dict1 = {'name':'yash', 'city': 'pune'}
swap_dict = {value : key for key , value in dict1.items()}
print(swap_dict)

# 16). Python Dictionary program to get the sum of all the items in a dictionary.
print("16). Python Dictionary program to get the sum of all the items in a dictionary.")

dict1 = {'x' : 23, 'y' : 10 , 'z' : 7}
sum = 0
for val in dict1.values():
	sum = sum+val
print(sum)

# 17). Python program to get the size of a dictionary in python.
print("17). Python program to get the size of a dictionary in python.")

# Hint : use sys.getsizeof(var) method.
import sys
dict1 = { 'name' : 'virat', 'sport' : 'cricket', 'name1' : 'Shekhar'}


print("Size of dict1 : " + str(sys.getsizeof(dict1)) + " bytes")

# 18). Python Dictionary program to check whether a key exists in the dictionary or not.
print("18). Python Dictionary program to check whether a key exists in the dictionary or not.")

dict1 = {'city':'pune', 'state' : 'maharashtra'}
count = 0
for key in dict1.keys():
	if key == "country":
		count= count+1
if count >0:
	print("key exists")
else:
	print("key dose not exists")

# 19). Python program to iterate over a dictionary.
print("19). Python program to iterate over a dictionary.")

dict1 = {'food':'burger', 'type':'fast food'}
for val in dict1:
	print(val , dict1[val])

# 20). Python Dictionary program to create a dictionary in the form of (n^3) i.e. if key=2 value=8
n=4
dict1 = {}
for val in range(1,n+1):
	dict1.update({val : val**3})
print(dict1)

# 21). Python Dictionary program to insert a key at the beginning of the dictionary.
print("21). Python Dictionary program to insert a key at the beginning of the dictionary.")

dict1 = { 'Course' : 'Python',  'Institute' : 'Sqatools' }
dict2 = {'Name' : 'Shekhar Tyagi'}
dict2.update(dict1)
print(dict2)

# 22). Python Dictionary  program to create a dictionary where keys are between 1 to 5 and values are squares of the keys.
print("22). Python Dictionary  program to create a dictionary where keys are between 1 to 5 and values are squares of the keys.")

dict1 = 5
dict2 = {}

for val in range(1, dict1+1):
		dict2.update({val : val**2})
print("square of dict : ", dict2)

# 23). Python Dictionary program to find the product of all items in the dictionary.
print("23). Python Dictionary program to find the product of all items in the dictionary.")

dict1 = { 'a' : 2, 'b' : 4, 'c' : 5}
ele1 = 1

for val in dict1.values():
	ele1 = ele1*val
	print(ele1)

# 24). Python Dictionary program to remove a key from the dictionary.
print("24). Python Dictionary program to remove a key from the dictionary.")

dict1= {'a':2,'b':4,'c':5}
dict2 = {}
for key , val in dict1.items():
	if key != "c":
		dict2[key] =val
print(dict2)

# 25). Python Dictionary program to map two lists into a dictionary.
print("25). Python Dictionary program to map two lists into a dictionary.")

inp1 = [ 'Name', 'Sport', 'Rank', 'Age']
inp2 = ['Virat', 'Cricket', 1,  32]
dict1 = zip(inp1,inp2)
print(dict(dict1))










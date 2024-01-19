
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






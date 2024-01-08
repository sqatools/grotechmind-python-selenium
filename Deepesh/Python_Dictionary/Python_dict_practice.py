# dict1 = {key : value}

"""
->  Dict is mutable data type
->  Only unique is allowed in the dictionary, duplicate keys are not allowed.
->  Only immutable data type can be key in the dict, int, float, string, tuple, boolean
->  All type of data can be value in the dictionary, int, float, string, tuple, list, dict, set, boolean.
"""

dict1 = {'a' : 345, 'b' : 678}
print(dict1, type(dict1))

# add data to dict
dict1['c'] = 600
print("dict1 :", dict1) # {'a': 345, 'b': 678, 'c': 600}

# get the data from dict
print(dict1['b']) # 678

dict1[5] = {4, 7, 8}
dict1[4.5] = [5, 8, 2]
dict1[(5, 7, 9)] = {'Name' : 'john', 'age' : 25}
dict1[True] = False

print("dict1 :", dict1)

# Add list as key
# dict1[[4, 6, 8]] = 'Programming'
# print("dict1 :", dict1)
# TypeError: unhashable type: 'list'

##### dictionary method ##########

print(dir(dict))

#  'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop',
#  'popitem', 'setdefault', 'update', 'values']


##### Add data to the dict #########
dict2 = {'Name' : 'John', 'Age' : 25}
dict2['Address'] = 'Mumbai'
print("dict2 :", dict2)

# update : this method update data from dict1 to dict2
dicta = {'Name' : 'John', 'Age' : 25}
dictb = {'email' : 'john@gmail.com', 'Address' : 'Mumbai'}

dicta.update(dictb)
print("dicta :", dicta)

# remove data from dict
print("_"*50)
dictf = {'email' : 'john@gmail.com', 'Address' : 'Mumbai', 'Phone': 56656435}

var = dictf.pop('Phone')
print(dictf)
print("var :", var)

dicth = {}
dicth['mobile'] = var
print("dicth :", dicth)

print("_"*50)
# popitem : this method remove the key value and return both

dictf = {'email' : 'john@gmail.com', 'Address' : 'Mumbai',
         'Phone': 56656435, 'country' : 'India'}

#var2 = dictf.popitem()
#print(var2)

for i in range(len(dictf)):
    print("dictf :", dictf)
    print(dictf.popitem())


# get method: this method return the value on the basis of key
dict1 = {'a': 456, 'b' : 555, 'c': 565}
val = dict1.get('b')
print(val)
print("dict1 :", dict1)

# keys and values method.
print("keys list :", dict1.keys()) # dict_keys(['a', 'b', 'c']
print("values list :", dict1.values()) # dict_values([456, 555, 565]

# items method
print("_"*50)
dict1 = {'a': 456, 'b' : 555, 'c': 565, 'd': 666, 'e': 676}
print(dict1.items())
# dict_items([('a', 456), ('b', 555), ('c', 565), ('d', 666), ('e', 676)])
output = dict1.items()
print(type(output))
print(list(output)[0][1])

for val in dict1.items():
    print(val)

for key, value in dict1.items():
    print("key :", key, "value :", value)


# Copy method:
# shallow copy and deep copy concept
print("_"*50)
dict2 = {'p': 'Python', 'q': 'Queen', 'r' : 'rabit'}
dict3 = dict2
dict3['s'] = 'Sandwitch'

print("dict2 :", dict2)
print("dict3 :", dict3)


# Deep copy concept
dicta = {'p': 'Python', 'q': 'Queen', 'r' : 'rabit'}
dictb = dicta.copy()
dictb['Programming'] = 'Python'

print("dicta :", dicta)
print("dictb :", dictb)


# del to delete dictionary data from memory

dicta1 = {'p': 'Python', 'q': 'Queen', 'r' : 'rabit', 's' : None}

#del dicta1
#print(dicta1)
# name 'dicta1' is not defined. Did you mean: 'dict1'?

del dicta1['r']
print("dicta1:", dicta1)


# set default method : this method set a default value for the key if the key is not available
# in the target dict
print("_"*50)
dictj = {'a' : 123, 'b' : 345,'c': 567, 'd': 789}

result = dictj.setdefault('g', 700)
print("result:", result)

print("dictj :", dictj)

dictj['c'] = 800
#print("dictj :", dictj)

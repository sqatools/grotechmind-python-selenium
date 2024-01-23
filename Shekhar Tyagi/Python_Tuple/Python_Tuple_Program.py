

# 1). Python tuple program to create a tuple with 2 lists of data.
# Input lists:
# list1 = [4, 6, 8]
# list2 = [7, 1, 4]
print("1). Python tuple program to create a tuple with 2 lists of data.")

list1 = [4, 6, 8]
list2 = [7, 1, 4]

# tup = tuple(zip(list1,list2))
tup = tuple(list1+list2)
print(tup)

# 2). Python tuple program to find the maximum value from a tuple.
# Input = (41, 15, 69, 55)
print("2). Python tuple program to find the maximum value from a tuple.")

tup = (41, 15, 69, 55)
tup1 = max(tup)
print(tup1)

# 3). Python tuple program to find the minimum value from a tuple.
# Input = (36,5,79,25)
print("3). Python tuple program to find the minimum value from a tuple.")

tup = (36,5,79,25)
tup1 = min(tup)
print(tup1)

# 4). Python tuple program to create a list of tuples from a list having a number and its square in each tuple.
print("4). Python tuple program to create a list of tuples from a list having a number and its square in each tuple.")

list1 = [4,6,3,8]
list_of_tuple = [ ]

for tup in list1:
	tup1 = (tup, tup**2)
	list_of_tuple.append(tup1)
print(list_of_tuple)

# 5). Python tuple program to create a tuple with different datatypes.
print("5). Python tuple program to create a tuple with different datatypes.")

mixed_tuple = ('John', 25, 5.5, True, [1, 2, 3])
print("mixed_tuple: ",mixed_tuple )

# 6). Python tuple program to create a tuple and find an element from it by its index no.
print("6). Python tuple program to create a tuple and find an element from it by its index no.")
tup = (4, 8, 9, 1)
Index = 2

tup1 = tup[2]
print(tup1)

# 7). Python tuple program to assign values of tuples to several variables and print them.
print("7). Python tuple program to assign values of tuples to several variables and print them.")

tup1 = (6,7,3)
(a,b,c) = tup1

print("a:",f"{a}" ",", "b:",f"{b}" ",", "c:",f"{c}")

# 8). Python tuple program to add an item to a tuple.
print("8). Python tuple program to add an item to a tuple.")

tup = ( 18, 65, 3, 45)
list1 = list(tup)
list2 = (15,18,26)

list1.extend(list2)
print(tuple(list1))

# 9). Python tuple program to convert a tuple into a string.
print("9). Python tuple program to convert a tuple into a string.")

tup = ('s', 'q', 'a', 't', 'o', 'o', 'l', 's')
string = " "

for char in tup:
	string= string+char
print("string:",string)

# 10). Python tuple program to get the 2nd element from the front and the 3rd element from the back of the tuple.
print("10). Python tuple program to get the 2nd element from the front and the 3rd element from the back of the tuple.")

tup = ('s', 'q', 'a', 't', 'o', 'o', 'l', 's')
print(tup[2],"," , end= " ")
print(tup[-3])

# 11). Python tuple program to check whether an element exists in a tuple or not.
print("11). Python tuple program to check whether an element exists in a tuple or not.")

tup = ('s', 'q', 'a', 't', 'o', 'o', 'l', 's')

if a in tup:
	result = True
else:
	result = False
print(result)

# 12). Python tuple program to add a list in the tuple.
print("12). Python tuple program to add a list in the tuple.")

list1=[12,67]
tup1=(6,8,4)
tup2 = list(tup1)
tup = (tup2+list1)
print(tuple(sorted(tup)))

# 13 13). Python tuple program to find sum of elements in a tuple.
print("13 13). Python tuple program to find sum of elements in a tuple.")

A=(4,6,2)
tup = sum(A)
print(tup)

# 14). Python tuple program to add row-wise elements in Tuple Matrix.
print("14). Python tuple program to add row-wise elements in Tuple Matrix")

A = [[('sqa', 4)], [('tools', 8)]]
B = (3,6)

result_matrix = [[(tup[0], tup[1], B[index]) for index, tup in enumerate(row)] for row in A]

print("Result Matrix:")
for row in result_matrix:
    print(row, end=" ")

print()

# 15). Python tuple program to create a tuple having squares of the elements from the list.
print("15). Python tuple program to create a tuple having squares of the elements from the list.")

tup = (1,5,7,3,6)

list1 =list(tup)
list2 =[]

for i in list1:
	square= i**2
	(list2.append(square))
print(list2)
res = tuple(sorted(list2))
print(res)

# 16). Python tuple program to multiply adjacent elements of a tuple.
print("16). Python tuple program to multiply adjacent elements of a tuple.")

tup = (1,2,3,4)
list1 =[]

for ele1 , ele2 in zip(tup,tup[1:]):
	print(ele1,ele2)
	multip = ele1*ele2
	list1.append(multip)
print(tuple(list1))

# 17). Python tuple program to join tuples if the initial elements of the sub-tuple are the same.
print("17). Python tuple program to join tuples if the initial elements of the sub-tuple are the same.")

list_tup = [(3,6,7),(7,8,4),(7,3),(3,0,5)]

# Not Solve

# 18). Python tuple program to convert a list into a tuple and multiply each element by 2.
print("18). Python tuple program to convert a list into a tuple and multiply each element by 2.")

list1 = [12,65,34,77]
list2 = []
for tup in list1:
	tup2 = tup*2
	list2.append(tup2)
print(tuple(list2))

# 19). Python tuple program to remove an item from a tuple.
print("19). Python tuple program to remove an item from a tuple.")

tup = ('p','y','t','h','o','n')
remove_item = 'h'
result = tuple(element for element in tup if element != remove_item)
print(result, end=" ")
print()

# Or
print("#"*40)

tup = ('p','y','t','h','o','n')
print("Original Result: ", tup)
list1 = list(tup)
list1.remove("h")
remove_result = tuple(list1)
print("Remove_Result:", remove_result)

# 20). Python tuple program to slice a tuple.
print("20). Python tuple program to slice a tuple.")

tup =(5,7,3,4,9,0,2)
print(tup[:3])
print(tup[2:5])
print(tup[5:])

# 21). Python tuple program to find an index of an element in a tuple.
print("21). Python tuple program to find an index of an element in a tuple.")

tup = ('s','q','a','t','o','o','l','s')
# Index of a?

result_of_index = tup.index('a')
print(result_of_index)

# 22). Python tuple program to find the length of a tuple.
print("22). Python tuple program to find the length of a tuple.")

tup =('v','i','r','a','t')
lenght_of_tup = len(tup)
print(lenght_of_tup)

# 23). Python tuple program to convert a tuple into a dictionary.
print("23). Python tuple program to convert a tuple into a dictionary.")

tup =(('Name','Shekhar'),('contact',9760939256))
dict1 = dict(tup)
print(dict1)

# 24). Python tuple program to reverse a tuple.
print("24). Python tuple program to reverse a tuple.")

tup = ( 4, 6, 8, 3, 1)
rev_tup = reversed(tup)
print(tuple(rev_tup))

# 25). Python tuple program to convert a list of tuples in a dictionary.
print("25). Python tuple program to convert a list of tuples in a dictionary.")

list1 = [ ('s', 2), ('q', 1), ('a', 1), ('s', 3), ('q', 2), ('a', 4)]

dict1 = { }
dicts = dict(list1)
for ele1 , ele2 in list1:
	dict1.setdefault(ele1,[]).append(ele2)
print("dicts:",dict1)

# 26). Python tuple program to pair all combinations of 2 tuples.
print("26). Python tuple program to pair all combinations of 2 tuples.")

from itertools import product
A = (2,6)
B = (3,4)

result = list(product(A,B)) + list(product(B,A))
print("Pairs:",result)

# 27). Python tuple program to remove tuples of length i.
print("27). Python tuple program to remove tuples of length i.")

list1 = [(2, 5, 7), (3, 4), ( 8, 9, 0, 5)]
i=2
for tup in list1:
	if len(tup) == 2:
		list1.remove(tup)
print(list1)































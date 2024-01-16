

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





































































list1 = [2, 3.5, 'Hello', [4, 6, 7], (3, 4, 2), {'a': 123, 'b': 555},
         {2, 4, 7}, True]

print(list1[0]) # 2
print(list1[3]) # [4, 6, 7]
print(list1[4][1]) # 4
print(list1[-3]['b']) # 555

# slicing with list

print(list1[2:5])
# ['Hello', [4, 6, 7], (3, 4, 2)]

print(list1[-3:]) # [{'a': 123, 'b': 555}, {2, 4, 7}, True]
print(list1[5:]) # [{'a': 123, 'b': 555}, {2, 4, 7}, True]


# list1 = [2, 3.5, 'Hello', [4, 6, 7], (3, 4, 2), {'a': 123, 'b': 555},
#         {2, 4, 7}, True]

# [initial index: last index: difference]

print(list1[-1: -5: -1])
# [True, {2, 4, 7}, {'a': 123, 'b': 555}, (3, 4, 2)]

print(list1[-1: -5: 1])  # []

print(list1[::-1])
# [True, {2, 4, 7}, {'a': 123, 'b': 555}, (3, 4, 2), [4, 6, 7], 'Hello', 3.5, 2]
print(list1[-1: -len(list1)-1: -1])
# print(list1[-1::-1])
# print(list1[::-1])

print("_"*40)
########## looping with list #####
list2 = [5, 7, 8, 2, 15]

# without indexing
for val in list2:
    print(val)

# with indexing
for i in range(len(list2)):
    print(i, ":", list2[i])

#program : get the all the even number from the list
lista = [4, 6, 7, 2, 3, 12]
print("_"*40)

for val in lista:
    if val%2 == 0:
        print(val)
    else:
        continue

# program : get max value from list
listb = [3, 6, 33, 5, 22, 55, 7, 12]
max_val = 0 #3, 6, 33, 55

for val in listb: # 3, 6
    if val > max_val: # 3 > 0: 6 > 3 : 33 > 6 : 5> 33 : 22> 33 : 55> 33
        max_val = val # 3, 6, 33, 55

print("max value :", max_val)

##################### List Methods #################

print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

##### Add data to the list #####
print("_"*40)
# append method: this method add the data at end of the list
listc = [4, 6, 7, 2, 8]
listc.append(100)
print("listc :", listc)

# insert method: this method add the data at any specified position in the list
listd =  [4, 6, 8, 22, 14]
listd.insert(2, 500)
print("listd :", listd)
# [4, 6, 500, 8, 22, 14]
listd.insert(3, (4, 7, 8))
listd.insert(4, [6, 8, 9])
listd.insert(-1, {'name': 'rahul', 'age': 25})
print("listd :", listd)

# extend method: this method add data from list1 to list2
list1 = [4, 6, 8, [5, 7, 8]]
list2 = ['a', 'b', 'c']

list2.extend(list1)
print("list2:", list2)
# list2: ['a', 'b', 'c', 4, 6, 8, [5, 7, 8]]

# concatenation of list data
list5 = [5, 7, 9]
list6 = [55, 77, 99]
list7 = list5 + list6
print("list7 :",list7)
print("list5 :", list5)
print("list6 :", list6)


################ Remove data from list #############
print("_"*50)
listf = [4, 7, 8, 9, 2, 7]
# remove method : this method will remove specified element from list
# if we have repeated element then the first occurenace will be removed.
var = listf.remove(8)
print("listf :", listf)
print(var)

listf.remove(7)
print("listf :", listf)
listf.remove(7)
print("listf :", listf)


# pop method: this method remove element from specific position and return it.
# the default position is -1
print("_"*50)
listg = [5, 7, 33, 88, 5,  99, 101, 5]

var = listg.pop() # default index will be -1
print("var:", var, listg)
# 5 [5, 7, 33, 88, 5, 99, 101]

var2 = listg.pop(4)
print("var:", var2, listg)
# 5 [5, 7, 33, 88, 99, 101]

# clear method: this method remove all the data from the list
listj = [5, 7, 8, 2, 5]
listj.clear()
print("listj :", listj)

# del : delete entire var from the memory
listk = [5, 7, 8, 2, 5]

# del listk
# print("listk :", listk)
# NameError: name 'listk' is not defined. Did you mean: 'list1'?

#del listk[3:]
#print(listk) # [5, 7, 8]


# listk = [5, 7, 8, 2, 5]
del listk[1:3]
print(listk) # [5, 2, 5]

# replace the list data

listv = [4, 7, 8, 2, 9, 24]
listv[2] = 100
print("listv :", listv)
# listv : [4, 7, 100, 2, 9, 24]

listv[-3:] = [200, 300, 400]
print("listv :", listv)
# listv : [4, 7, 100, 200, 300, 400]



############### filtering and arrangement ##########
listx = [5, 8, 33, 22, 55, 77, 55, 99, 55]
# index method:
print(listx.index(33)) # 2

# count method : this method provide number of occurence of any element
print(listx.count(55)) # 3

# sorting of the list

# sort method: this method sort the list in accending and decending order.
listy = [5, 7, 3, 8, 2, 6, 1]
#listy.sort()
#print("listy :", listy) # [1, 2, 3, 5, 6, 7, 8]

listy.sort(reverse=True)
print("listy :", listy) # [8, 7, 6, 5, 3, 2, 1]


# sorted function
listz= [5, 8, 9, 2, 7, 9, 2, 1]

output = sorted(listz)
print(output) # [1, 2, 2, 5, 7, 8, 9, 9]
output2 = sorted(listz, reverse= True)
print(output2) # [9, 9, 8, 7, 5, 2, 2, 1]
print("listz :", listz)


print("_"*50)
# reverse of the list
# reverse method: this method reverse the list and modify in place
listw = [5, 7, 2, 8, 1, 6, 34]
listw.reverse()
print("listw :", listw)  # [34, 6, 1, 8, 2, 7, 5]


# reversed function
listw1 = [5, 7, 2, 8, 1, 6, 34]
result = reversed(listw1)
print(result)
for val in result:
    print(val, end=' ')

print()
print("listw1 :", listw1)

############################ Copy ###############
print("_"*40)
# Sallow copy

list1 = [4, 7, 8, 2]
list2 = list1
list2.append(50)

print("list1 :", list1, id(list1))
print("list2 :", list2, id(list2))

# Deep Copy
listx = [5, 7, 9, 2, 90]
listy = listx.copy()
listy.append(100)

print("listx :", listx, id(listx))
print("listy :", listy, id(listy))

# program: please provide output of lista

lista = [4, 7, 8, 9]
listb = lista
listc = listb
listc.append(55)
listb.append(66)
print("lista :", lista)


listp = [5, 7, 8, 9]
listq = listp.copy()
listr = listq
listr.append(100)
listq.append(200)

print("listp :", listp)
print("listq :", listq)
print("listr :", listr)

################## Max Min and Sum #######################
print("_"*50)

listg = [5, 7, 8, 3, 66, 23]

print("max value :", max(listg))
print("min value :", min(listg))
print("sum of values :", sum(listg))

# zip function

listh = [5, 7, 8, 9, 10]
listk = ['a', 'b', 'c', 'd', 'e', 'f']

result = zip(listh, listk)
#print(list(result)) # [('a', 5), ('b', 7), ('c', 8), ('d', 9)]
#print(dict(list(result)))  # {'a': 5, 'b': 7, 'c': 8, 'd': 9}
print(dict(result))


############### list comprehension #########

list1 = [4, 7, 9, 2, 8, 11]
list2 = []
for val in list1:
    if val%2 == 0:
        list2.append((val, 'even'))
    else:
        list2.append((val, 'odd'))
print(list2)


result = [x**2 for x in list1 if x%2 == 0]
print(result)

list1 = [4, 7, 9, 2, 8, 11]

reuslt2 = [(x, 'even') if x%2 ==0 else (x, 'odd') for x in list1]
print("result2 :", reuslt2)


































































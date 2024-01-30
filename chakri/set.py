'''#1). Python program to create a set with some elements.
a = {2,3,4,5,6,7,8,6}
print(a)
print(type(a))
#2). Python program to add an element to a set.
a.add(14)
print(a)
#3). Python program to remove an element from a set.
a.remove(7)
print(a)
#4). Python program to find the length of a set.
a = {2,3,4,5,6,7,8,6}
print(len(a))
#5). Python program to check if an element is present in a set.
if 6 in a:
    print('true')
else:
    print('false')
#6). Python program to find the union of two sets.
a = {2,3,4,5,6,7,8,6}
b = {10,20,30}
print(a.union(b))

#7). Python program to find the intersection of two sets.
a = {2,3,4,5,6,10,7,8,6}
b = {10,20,30,2,3,5,6,8}
#print(a.intersection(b))
#8). Python program to find the difference of two sets.
print(a.difference(b))
print(b.difference(a))
#9). Python program to find the symmetric difference of two sets.
print(a.symmetric_difference(b))

#10). Python program to show if one set is a subset of another set.
a = {2,3,4,5,6,10,7,8,6}
b = {3,6,8,10}
print(b.issubset(a))
#11). Python program to check if two sets are disjoint.
print(a.isdisjoint(b))
#12). Python program to convert a list to a set.
c = list(b)
print(type(c))
print(c)
#13). Python program to convert a set to a list.
a = [8, 10, 3, 6]
b = set(a)
print(type(b))
#14). Python program to find the maximum element in a set.
print(max(b))
#17). Python program to find the average of elements in a set.
a = {2,3,4,5,6,10,7,8,6}
b = sum(a)
c = len(a)
print(b/c)'''
#18). Python program to check if all elements in a set are even.
a = {2,4,6,10,8,6,7}
c = 0
for i in a:
    if i%2 == 0:
        c = c+1
if c == len(a):
    print('all are even number')
else:
    print('all are not even')
#19). Python program to check if all elements in a set are odd.
a = {2,4,6,10,8,6,7}
b = {7,9,5,3,13}
c = 0
for i in b:
    if i%2 != 0:
        c = c+1
if c == len(b):
    print('all are odd number')
else:
    print('all are not odd number')

a = [10,40,50,6,8,9,]
b = list(map(lambda x: x%2 == 0,a))
print(list(map(lambda x: x%2 == 0,a)))




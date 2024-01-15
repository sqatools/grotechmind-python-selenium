#1). Python program to calculate the square of each number from the given list.
'''a = [2,3,6,8,10]
for i in a:
    print(i**2,end= ' ')
#2). Python program to combine two lists.
a = [2,3,6,8,10]
b = [10,4,9,12]
a.extend(b)
print(a+b)
print(a)

a = 'happy new year'
a = a.split()
a.reverse()
print(a)
#3). Python program to calculate the sum of all elements from a list.
a = [10,30,40,70]
print(sum(a))

# Python program to find a product of all elements from a given list.
a = [3,6,9,2]
b = 1
for i in a:
    b = b*i
print(b)

#5). Python program to find the minimum and maximum elements from the list.
a = [3,6,9,2,14,67]
print(max(a))
print(min(a))

#6). Python program to differentiate even and odd elements from the given list.
a = [3,6,9,2,14,67,56,48,99]
b = []
c = []
for i in a:
    if i%2 == 0:
        b.append(i)
    else:
        c.append(i)
print(c)
print(b)
#7). Python program to remove all duplicate elements from the list.
a = [3,6,9,2,14,67,56,48,99,48,14,9]
print(set(a))
b = []
for i in a:
    if i not in b:
        b.append(i)
print(sorted(b))
#8). Python program to print a combination of 2 elements from the list whose sum is 10.
a = [3,6,9,2,4,9,7,1]
b = []
c = []
for i in a:
    for k in a:
        if i+k ==  10:
            b = i,k
            c.append(b)
print(set(c))
#9). Python program to print squares of all even numbers in a list.
a = [3,6,9,2,4,9,7,1,8]
for i in a:
    if i%2 == 0:
        print(i**2,end= ' ')

#10). Python program to split the list into two-part, the left side all odd values and the right side all even values.
a = [5, 7, 2, 8, 11, 12, 17, 19, 22]
#Output = [5, 7, 11, 17, 19, 2, 8, 12, 22]
b = []
c = []
for i in a:
    if i%2 == 0:
        c.append(i)
    else:
        b.append(i)
print(b+c)
b.extend(c)
print(b)

#11).  Python program to get common elements from two lists.
list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
#Outputt : [4, 5, 7, 2]
for i in list1:
    if i in list2:
        print(i,end= ' ')

#12). Python program to reverse a list with for loop.
a = [4, 5, 7, 9, 2, 1]
#a.reverse()
#print(a)
#Input list
list1 = [1,2,3,4,55]

#Printing list in the reverse order
#Using for loop
for i in range(len(list1)-1,-1,-1):
    print(list1[i], end=" ")

#14). Python program to reverse a list using index slicing.
a = [4, 5, 7, 9, 2, 1]
print(a[-1::-1])
#15). Python program to reverse a list with reversed and reverse methods.
print(list(reversed(a)))
a.reverse()
print(a)

#16). Python program to copy or clone one list to another list.
a = [4, 5, 7, 9, 2, 1]
b = [2, 5, 8, 3, 4, 7]
c = []
print(a)
print(b)
for i in a:
    c.append(i)
print(c)

#17). Python program to return True if two lists have any common member.
a = [4, 5, 7, 9, 2, 1]
b = [2, 5, 8, 3, 4, 7]
c = []
for i in a:
    if i in b:
        c.append(i)
print(c)
#18). Python program to print a specific list after removing the 1st, 3rd, and 6th elements from the list.
a = [4, 5, 7, 9, 2, 1]
for i in a:
    if a.index(i) == a[0]:
        a.remove(i)
        print(a)
#19). Python program to remove negative values from the list.
a = [4, 5, 7, -9, 2, -1]
b = []
for i in a:
    if i >= 0:
        b.append(i)
print(b)
#20). Python program to get a list of all elements which are divided by 3 and 7.
b = [2, 5, 8, 3, 4, 7, 56, 70, 80, 68, 21 ]
c = []
for i in b:
    if i%3 == 0 and i%7 == 0:
        print(i,'divided 3 and 7',end= ' ')
    else:
        print(i,'is not divided 3 and 7')


#22). Python Program to get a list of words which has vowels in the given string.
a = 'www Student ppp are qqqq learning Python vvv'
#Output : [‘Student’, ‘are’, ‘learning’, ‘Python’]
a = a.split()
b = 'aeiou'
c = []
for word in a:
    for char in word:
        if char.lower() in b:
            if word not in c:
                c.append(word)
print(c)

#23). Python program to add 2 lists with extend method.
a = [4, 5, 7, 9, 2, 1]
print(a)
b = [2, 5, 8, 3, 4, 7]
a.extend(b)
print(a)

#24). Python program to sort list data, with the sort and sorted method.
a = [4, 5, 7, 9, 2, 1, 2, 5, 8, 3, 4, 7]
a.sort()
print(a)
print(set(sorted(a)))

#25). Python program to remove data from the list from a specific index using the pop method.
a = [4, 5, 7, 9, 2, 1, 2, 5, 8, 3, 4, 7]
a.pop(0)
print(a)
#26). Python program to get the max, min, and sum of the list using in-built functions.
a = [4, 5, 7, 9, 2, 1, 2, 5, 8, 3, 4, 7]
print(max(a))
print(min(a))
print(sum(a))
#27). Python program to check whether a list contains a sublist.
a = [4, 5, 9, 2, 1, 2, 8, 3, 7,5, 7]
b = [5,8,4,7]
c = 0
for i in set(a):
    for k in b:
        if i == k :
            c = c+1
if c == len(b):
    print('b is sublist of a')
else:
    print('b is not a sublist a')
print(c)
print(len(b))
#29). Python program to find the second largest number from the list.
a = [4, 5, 9, 2, 1, 2, 8, 3, 7,5, 7]
b = sorted(a)
print(b[-2])
#30). Python program to find the second smallest number from the list.
a = [4, 5, 9, 2, 1, 2, 8, 3, 7,5]
a.sort()
print(a[1])
#31). Python program to merge all elements of the list in a single entity using a special character.
a = ['4', '5']
print("$".join(a))
#32). Python program to get the difference between two lists
a = [22,44,66,99,0,45,76,89]
b = [45,6,7,88,99,0,76]
c = []
for i in a:
    if i not in b:
        c.append(i)

for k in b:
    if k not in a:
        c.append(k)
print(c)
#33). Python program to reverse each element of the list.
a = ['Sqa', 'Tools', 'Online', 'Learning', 'Platform']
b = []
#output = [‘aqS’, ‘slooT’, ‘enilno’, ‘gninraeL’, ‘mroftalP’]
for i in a:
    if i == str(i):
        b.append(i[::-1])
print(b)'''
#34). Python program to combine two list elements as a sublist in a list.
x = [3, 5, 7, 8, 9]
y = [1, 4, 3, 6, 2]
#Output = [[3, 1], [5, 4], [7, 3], [8, 6], [9, 2]]
c = []
d = []
for (a,b) in zip(x,y):
    c.append((list(a,b)))
print(c)



















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
'''
#14). Python program to reverse a list using index slicing.
a = [4, 5, 7, 9, 2, 1]
print(a[-1::-1])
#15). Python program to reverse a list with reversed and reverse methods.
print(list(reversed(a)))
a.reverse()
print(a)








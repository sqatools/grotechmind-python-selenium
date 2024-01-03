# 1). Python program to calculate the square of each number from the given list.
"""
list=[10,20,88,99,5,7]
for val in list:
 print("square of no:",val,val**2)

"""


# 2). Python program to combine two lists.
"""
lst1=[10,88.55,2,7,9,100]

lst2=[88,66,2,33,77,45]

lst3=lst1+lst2
print(lst3) #[10, 88.55, 2, 7, 9, 100, 88, 66, 2, 33, 77, 45]
"""
'''
lst1=[10,88.55,2,7,9,100]

lst2=[88,66,2,33,77,45]

lst1.extend(lst2)

print(lst1) #[10, 88.55, 2, 7, 9, 100, 88, 66, 2, 33, 77, 45]
'''

# 3). Python program to calculate the sum of all elements from a list.
'''
lst1=[1, 8 ,9 ,10,88,900 ]
sum=0
for val in lst1:
    sum=sum+val
print(sum)

'''
"""
lst1=[1, 8 ,9 ,10,88,900 ]

count=0
total=0

while count<len(lst1):

    total=total+lst1[count]
    count=count+1
print(total)
"""
'''
lst1=[1, 8 ,9 ,10,88,900 ]

print(sum(lst1))
'''
"""
lst2=[10,20,80,95,100]
total=0
for val in lst2:
    total=total+val
print(total)

"""
"""
lst2=[10,20,80,95,100]

count=0
total=0

while count<len(lst2):
    total=total+lst2[count]
    count=count+1
print(total)
"""
'''
lst2=[10,20,80,95,100]
print(sum(lst2))
'''




















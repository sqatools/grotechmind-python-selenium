tuple1 = (7, 8, 33, 44, 'a', 4.5, [4, 6], (2, 5, 7), {'a': 123, 'b':146}, True, {5, 7, 9, 5})

print(tuple1[7])
print(tuple1[6][1])
print(tuple1[-1])
print(tuple1[-3]['b'])

print(tuple1[5:8])
print(tuple1[1:10])

print(tuple1[::2])
print(tuple1[::-1])

print("_"*50)
tup2 = (5, 7, 9, 2)
for val in tup2:
    print(val**2)

# with indexing
for i in range(len(tup2)):
    print(i, tup2[i], tup2[i]**2)


# methods
print(dir(tuple))

# 'count', 'index'

tupl3 = (4, 6, 8, 2, 92, 6, 2, 4, 2)
print(tupl3.count(2)) # 3

print(tupl3.index(92)) # 4

# tuple comprehension
tup4 = (4, 7, 12, 8, 1, 5, 9)

result = (val for val in tup4 if val%3 ==0)
print(result)
for val in result:
    print(val, end=' ')

print()
list1 = [4, 7, 8, 2, 6, 8, 34]
result2 = [val for val in list1 if val%2 == 0]
print("result :", result2)


str1 = "Happy New Year 2024"
# print(str1.isalpha())
# for word in str1.split():
#     print(word, ":", word.isalnum())
#
temp = ''
for word in str1:
    #print(word)
    if word.isalnum():
        #print(''.join(word))
        temp= temp + word
print(temp)
print("-".join(temp))

print("-".join(str1.split()))

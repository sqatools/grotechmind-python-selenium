output = lambda x, y: x+y
print(output(50, 60))

def square(n):
    return n**2

list1 = [5, 7, 8, 3, 2]
#output = [25, 49, 64, 9, 4]

output = []

for val in list1:
    result = square(val)
    output.append(result)

print(output)


# map : This will map
list1 = [5, 7, 8, 2, 9]
result = list(map(square, list1))
print(result)


result2 = list(map(lambda x:x**2, list1))
print(result2)


# filter : filter return the expected only
lista = [5, 7, 3, 66, 23, 8, 4]

result3 = list(filter(lambda x: x%2==0, lista))
print("result3:", result3)
# result3: [66, 8, 4]

# reduce : reduce return the one single value
from functools import reduce

listb = [7, 8, 3, 8, 2, 4]

result4 = reduce(lambda x, y: x+y, listb)
print("result4:", result4)

result5 = reduce(lambda x, y: x*y, listb)
print("result4:", result5)

# write a program to find the common values between two list.
# -> avoid duplicate common value
# -> arrange the common value in ascending order.

list1 = [4, 7, 9, 2, 7, 11, 15]
list2 = [8, 7, 1, 9, 2, 4, 5]
common = []

"""
1. Iterate each element of the list1 : for val in list1
2. Check element of list1 is available in list2: if val in list2:
#3. If list1 element is available list2 then add into common list: common.append(val)
3.1 If list1 element is available list2 and not available in common
     then add val into common list: common.append(val)
4. If list1 element is not available in list2 then move to next element.
5. arrange all the common value in ascending order: sorted(common)
"""
"""
for val in list1:
    if val in list2 and val not in common:
        common.append(val)
    else:
        continue

print("common values :", sorted(common))
"""

# input_val = list(input("please enter the numbers"))
# print(input_val)

input_val = input("please enter the numbers")
all_value = input_val.split()
for val in all_value:
    print(int(val)*2)





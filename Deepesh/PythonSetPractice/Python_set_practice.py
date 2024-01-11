set1 = {'a', 'b', 2, 6, 7, 2, 6, 8}
"""
-> set is mutable data type
-> set store only unique data, duplicate data is not allowed.
-> all the immutable data type can be member of set, int, float, string, tuple, boolean
   we can define list and dict as set member.
-> set store data in un-structure order does not follow any indexing.
"""

print(set1, type(set1))

set2 = {2, 2.3, 'Hello', (5, 7, 8), True}
print(set2)

# TypeError: unhashable type: 'list' : list can not member of the set
# TypeError: unhashable type: 'dict' : Dict can not be member of the set

print(dir(set))

# 'add', 'clear', 'copy', 'difference', 'difference_update',
# 'discard', 'intersection', 'intersection_update', 'isdisjoint',
# 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
# 'symmetric_difference_update', 'union', 'update'

# Add data to the set
# add method : this method add one single value at a time in the set
seta = {5, 8, 9}
seta.add(10)

print("seta :", seta)

# update method : update method, update data from set1 to set2.

setb = {5, 7, 9}
setc = {11, 23, 34}

setc.update(setb)
print("setc :", setc)

# union method: This method combine two set data and return new set.
set11 = {22, 33, 44}
set12 = {55, 77, 88}

output = set11.union(set12)
print(output)


# Remove data from set
# remove method : this method remove speicific element from the set if it is available
# if not available then throw as key error.
# KeyError: 89

setj = {5, 7, 18, 2, 8}

setj.remove(18)
print("setj :", setj)

# pop method : this method remove any random data from and return it.

setk = {5, 8, 22, 44, 55}
var = setk.pop()
print("var :", var)


# discard method: This method remove data from set, if it is available in the target.
# if not available , doest do anything.

setl = {6, 7, 88, 22, 55}
setl.discard(23)
print("setl :", setl)

# setl.remove(89)
# remove method throws error, if the element is not available in the target set
# KeyError: 89
print("setl :", setl)


# intersection: intersection method return the common values between two sets.

setx = {5, 7, 8, 3, 9, 89, 5}
sety = {15, 5, 7, 2, 8, 9}

inter_output = setx.intersection(sety)
print("inter section :", inter_output)

# intersection update : this method update the set with common values only, all other data
# will be discarded.
#setx.intersection_update(sety)
print("result :", setx)
print("sety :", sety)
sety.intersection_update(setx)
print("sety :", sety)

# difference method: this method return all the difference values between 2 sets

setp = {6, 8, 23, 45, 22}
setq = {11, 77, 25, 33, 23, 6, 22}

diff_value = setp.difference(setq)
print("diff values :", diff_value) # {8, 45}


diff_value2 = setq.difference(setp)
print(diff_value2) # {33, 11, 77, 25}

# difference update
setr = {6, 8, 23, 45, 22}
sets = {11, 77, 25, 33, 23, 6, 22}


# setr.difference_update(sets)
# print("setr :", setr) # {8, 45}

sets.difference_update(setr)
print("sets :", sets)  # {33, 25, 11, 77}

# subset and superset

setv = {4, 6, 8, 9, 2, 7, 18}
setb = {4, 8, 7}

print(setv.issuperset(setb)) # True
print(setv.issubset(setb))   # False
print(setb.issubset(setv))   # True

# clear method : clear all the data from set
setv1 = {4, 6, 8, 9, 2, 7, 18}

setv1.clear()
print("setv1 :", setv1) # set()

# copy

# shallow copy concept
setb= {'a', 'b', 'c', 'd'}

setc = setb
setd = setc
setd.add(100)
print("setb :", setb)
print("setd :", setd)

# deep copy concept
setc1 = {55, 77, 33, 23}
setc2 = setc1.copy()
setc2.add(500)
print("setc2 :", setc2)
print("setc1 :", setc1)

########################## iterate value using loop ################

setw = {50, 40, 66, 77}

for val in setw:
    print("val :", val)

















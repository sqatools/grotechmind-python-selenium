from itertools import groupby
from operator import itemgetter

a= ["cat","dog","cow","lion","Fox","Shark","Snake","bear"]

for i,wds in groupby(sorted(a),key=itemgetter(0)):
    print(i)
    for w in wds:
        print("",w)
        print("")



print("*"*30)
str = "This is python program"
rev = ' '.join(word[::-1] for word in str .split())
print(rev)

# '' sihTsinohtypmargorp
# ' ' sihT si nohtyp margorp
# spliting the string into words using split()
# Reversing the each word using Slicing([::-1])
# joining the reversed words back together with space using ' '.join

print("*"*30)

print('abcdefcdghcd'.split('cd',2))
# ['ab', 'ef', 'ghcd']

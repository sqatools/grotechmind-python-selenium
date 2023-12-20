# range method with default initial value is zero
# and difference value is 1
"""
for i in range (11):
    print(i)

print("_"*50)
for i in range (1,21):
    print(i)
"""
print("_"*50)
for i in range (0,11,2):
    print(i)

print("_"*50)
# program to print all the even number from 1 to 20
for i in range(1, 20):
    if i%2 == 0:
        print(i)

#print the table of given number:
num=2
for i in range(1,11):
    print(num, "*", i,":" ,i*num)


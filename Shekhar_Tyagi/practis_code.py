
"""

*
**
***
****
*****

"""
for i in range ( 1,6):
    print()
    for j in range (i):
        print(j , end=" ")
print()
print("_"*39)

num = 1
while num <=15:
    if num >5 and num <8:
        num = num+1
        break
    print(num)
    num = num+1


print("_"*50)

num = 6
fact = 1
for i in range (num , 0 ,-1):
    print(i)
    fact = fact*i
    print("fact:",fact)


a = 0
b = 1

for i in range (10):
    print(b, end=" ")
    a,b = b, a+b


print()


print("__"*40)

num = 11
prime = True
for i in range (2, num//2):
    if num%i==0:
        prime = False
if prime:
    print("This is prime value:" ,num)
else:
    print("this is not prime value:",num)


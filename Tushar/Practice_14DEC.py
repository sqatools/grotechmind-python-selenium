#################Nested Loop#################

for i in range (1,11):

    print("address:",i)

    for j in range(1,4):
        #print("address:",i,"pacakge:",j)

        #print("address:",i)
        #print("pacakge:",j)

         print("pacakge:",j)

    print("+"*40)

print("+"*40)

####write programme to get list of prime number between 1 to 100

num=11
prime= True
for i in range (2,num):
    if num%i==0:
        prime=False
if prime:
    print("this is prime no:")
else:
        print("This is not Prime no:")


print("+"*100)


#num=11
for num in range (1,100):
    prime= True
    for i in range (2,num):
        if num%i==0:
            prime=False
    if prime:
        print("this is prime no:",num)
    else:
            print("This is not Prime no:",num)


###Print Following Pattern with Loop Condition###

'''
*
* *
* * *
* * * *
* * * * *

'''
print("+"*100)
"""


for i in range (1,6):
    print(i*"*")
#print(*)

"""

for i in range (1,6):
    for j in range(i):
        print("*",end=" ")
    print()


print("+"*100)

###Print Pattern ###

"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15 """

print("+"*100)

temp=1
for i in range (1,6):
    for j in range (i):
        print(temp,end=" ")
        temp+=1
    print( )


####while loop condition###################

num=1

while num<=10:
    print(num)
    num+=1
    #num=num+1

#####################Continue and Break Statement##############

temp=1
while temp<=10:
    if temp==5:
        temp=temp+1
        continue
    print(temp)
    temp=temp+1


print("+"*100)

temp=1
while temp<=10:
    if temp>5 and temp<8:
        temp=temp+1
        continue
    print(temp)
    temp=temp+1

print("+"*100)

temp=1
while temp<=10:
    if temp==5:
        break
    print(temp)
    temp=temp+1

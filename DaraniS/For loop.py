

# for i in range(1500,2700):
#     if i%7==0 and i%5==0:
#         print(i, end=" ")
#
#
#
# for i in range(4):
#     print(i*"*")
# for i in range(2,-1,-1):
#         print(i * "*")
#
# for i in range(4):
#     print(i*"*", end=" ")
# # for i in range(2,-1,-1):
# #         print(i * "*")

# for i in range(1,101):
#     if i%2==0:
#         print(i,end=" ")
#
# num ='1366'
# count = 0
#
# for i in num:
#     count += 1
# print(count)
#
# num = '12345'
# count = 0
#
# for i in num:
#     count += 1
#
# print(f"Total digits in {num}: ",count)
#
#
# list2=[2,6,7,4,9]
# list3=[6,9,3,2]
# list4 =[]
#
# for val in list2:
#     if val in list3:
#         print(list4.append(val))
#     else:
#         continue
#
#
# print(list4)

# i = 'Sqatools'
# for char in i:
#     print(char,end=' ')
#
# inp=[]
# for i in range(0,11):
#     if i%2 !=0:
#         inp.append(i)
# print(inp)
#
# dic ={'name':'virat','sports':'cricket'}
# for value in dic.keys():
#     print(value)
max1=0
list1 = [12,14,45,88,63,97,88]
for i in list1:
    if i>max1:
        max1 = i
print(max1)

j = 23

for num in range(1,j+1):
    count = 0
    if(num==1 | num == 2):
        print(num)
        continue
    for i in range(2,num+1):
        if(num%i == 0):
            count = count+1
        if(count>=2):
            break
    if(count<2):
        print(num)

even_sum=0
odd_sum=0
for i in range(1,21):
    if i%2==0:
        even_sum= even_sum+i
    else:
        odd_sum=odd_sum+i
print(even_sum)
print(odd_sum)


for num in range(1, 10):
    is_prime = True

    # Check for factors other than 1 and the number itself
    for i in range(2, num):

        if num % i == 0:
            is_prime = False
            break

   # If no factors other than 1 and the number itself are found, it's prime
    if is_prime:
       print(num)


for num in range(1, 10):
    is_prime = True

    # Check for factors other than 1 and the number itself
    for i in range(2, num):
        print(i,num)
        # if num % i == 0:
        #     is_prime = False
        #     break

#    # If no factors other than 1 and the number itself are found, it's prime
#    #if is_prime:
#        print(num)


# for i in range(6,0,-1):
#
#     for j in range(i):
#         print("*",end="")
#
#     print()
# num=1
# while num<=10:
#     print(num)
#     num=num+1
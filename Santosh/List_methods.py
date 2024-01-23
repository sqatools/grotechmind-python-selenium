# list=['hello',3,5,8,2,1,[2,4,6],{'a':121,'b':'abc'},999,1,1,1,5]
#list2=['hello',3,5,8,2,1,[2,4,6],{'a':121,'b':'abc'}]
#print(list)

# print(dir(list))
 #'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

#
# list.append({'c:123'},[1,2,4])
# print(list)

# list2=list.copy()
# print(list2)


# list.count(5)
# print(list)
# list.extend(list2)
# print(list)

# list=['hello',3,5,8,2,1,[2,4,6],1,{'a':121,'b':'abc'},999,1,1,1,5]
#       #  0     1 2 3 4 5
# val=list.index(1)
# print(val)

# A=0
# for i in range (len(list)):0,1,2,...14
#     #print(i)
#     if list[i]==1:
#         print(list[i])
#         A=A+1
#         #print("count:", B)
#         if A==2: ##second occurance
#             print(i)
#         # else:
#         #  continue

# list_value = [45, 55, 69, 55, 78, 55]
# new_list = [] #1 3, 5
# for i in range(len(list_value)): #0, 1, 2,3 4, 5
#     if list_value[i] == 55:
#         new_list.append(i)
# print(new_list)

# list of items
# list1 = [6, 8, 5, 6, 1,6, 2,5]
#
# # Will print index of '6' in sublist
# # having index from 1 to end of the list.
# print(list1.index(5,3))

# list=['hello',3,5,8,2,1,[2,4,6],{'a':121,'b':'abc'},999,1,1,1,5 ]
# # # #list2=['hello',3,5,8,2,1,[2,4,6],{'a':121,'b':'abc'}]
# # # #print(list)
# # #
# # # # print(dir(list))
# # #  #'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
# # #
# list.insert(-1,99999)
# print(list)

# pop method: this method remove element from specific position and return it.
# the default position is -1
# print("_"*50)
# listg = [5, 7, 33, 88, 5,  99, 101, 5]

# var = listg.pop(5) # default index will be -1
# print("var:", var)
# print(listg)

# clear method: this method remove all the data from the list
# listj = [5, 7, 8, 2, 5]
# listj.clear()
# print("listj :", listj)
# # del : delete entire var from the memory
# listk = [5, 7, 8, 2, 5]
#
# del listj
#
# print(listj)


# print("_"*50)
#
# listp=[1,2,3,4,5, [1,2,3,4],(100,200)]
# listp[-3:]=(1000)
# print(listp)


# listx = [5, 8, 33, 22, 55, 77, 55, 99, 55]
# # index method:
# print(listx.index(40)) # 2


# reversed function
# listw1 = [5, 7, 2, 8, 1, 6, 34]
# result = reversed(listw1)
#
# for val in result:
#     print(val, end=' ')
#
#
# # print("listw1 :", listw1)


############################ Copy ###############
print("_"*40)
# Sallow copy

# list1 = [4, 7, 8, 2]
# list2 = list1
# # list2.append(50)
#
# print("list1 :", list1, id(list1))
# print("list2 :", list2, id(list2))

# Deep Copy
# listx = [5, 7, 9, 2, 90]
# listy = listx.copy()
# listy.append(100)
#
# print("listy :",listy, id(listy))
# print("listx :", listx, id(listx))

#
# lista = [4, 7, 8, 9]
# listb = lista
# listc = listb
# listc.append(55)
# listb.append(66)
# print("lista :", lista)


# listp = [5, 7, 8, 9]
# listq = listp.copy()
# listr = listq
# listr.append(100)
# listq.append(200)
#
# print("listp :", listp)
# print("listq :", listq)
# print("listr :", listr)


# list2=[99,2,00,77,4,5,1,88]
# print("Min_Value :", min(list2))
# print("max_val :", max(list2))
# print("Avg_val :", sum(list2)/len(list2))

list1 = [4, 7, 9, 2, 8, 11]

# for i in list1:
#     if i % 2== 0:
#         print("odd",i)
#     if i %2!=0:
#          print("even :",i)
A=[]
for val in list1:
    #print(val)
    if val%2==0:
        A.append((val ,"even"))

    else:
        A.append((val, "odd"))
print(A)

#----------------------------
print("*"*50)

Result=[(x,"even") for x in list1 if x%2==0]
print(Result)


print("*"*50)
Result1=[x for x in list1 if x%2!=0 ]
print(Result1)

#--------------
print("*"*60)

list1 = [4, 7, 9, 2, 8, 11]

reuslt2 = [(x, 'even') if x%2 ==0 else (x, 'odd') for x in list1]
print("result2 :", reuslt2)


















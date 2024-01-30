# pyramid pattern

num=int(input("Enter the number of row :"))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*", end=" ")
    print()



# for i in range(0,4): #0,1,2,3
#     for j in range(4-i):#(4-0=4),(4-1=3),(4-2=2),(4-3=1)
#         print(j,end="")#(0,1,2,3)=4
# #print() #next line  #(0,1,2)=3
# #print() #next line  #(0,1)=2
# #print() #next line  #(0)=1
#     print() # next line


# for i in range(4,0,-1):
#     print(i)
#
#     for j in range(0,4-i):
#         print(end=" ")
#     for j in range(0,i):
#         print("j",end=" ")
#     print()




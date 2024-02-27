######################## print A pattern #################################################

# for row in range(6):
#
#     for col in range(6):
#
#         if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
#             print("A",end="")
#         else:
#             print(end=" ")
#     print()

######################## print F pattern #################################################

# for row in range(7):
#     for col in range(7):
#         if (( row ==0 or row==3 or col==0)):
#             print("*",end="")
#         else:
#             print(end="")
#     print()
######################## print B pattern #################################################
#print("#"*60)
for row in range(7):
    for col in range(7):
        if (row ==0 and col!=6)or row==3 or (row==6 and col!=6)or col==0 or ((row==1 or row==2 or row==4 or row==5) and col==6 ):
            print("*",end="")
        else:
            print(end=" ")
    print()

###############################print "C" alphabet pattern#################

# for row in range(6):
#     for col in range(6):
#         if (col==0 and(row!=0 and row!=5)) or ( row==0 and(col>0 and col<5)) or (row==5 and (col>0 and col<5)):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()

###############################print "E" alphabet pattern#################
# print("#"*60)
# for row in range(7):
#     for col in range(7):
#         if (row==0 and col!=0 ) or (row==6 and col!=0 ) or ( col==0) and (col!=0 or col!=6) or row==3:
#             print("*", end="")
#         else:
#             print(end="")
#     print()
#
# ###############################print "G" alphabet pattern#################
#
# for row in range(6):
#     for col in range(6):
#         if (col==0 and (row!=0 and row!=5)) or (row==0 and(col>0 and col<6)) or (row==1 and col>4) or (row==5 and (col>0 and col<5)) or ((row==5 or row==4 or row==3) and col>4):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()

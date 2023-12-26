######################dictonary#########################################

# dict represent in {} curly braces  and key value
#dict is mutable datatype.we can modify at any point of time
#dict store data in the form of key value pair
#dict maintains unique key.it means duplicate key is not allowed. it considered last updated value only ex:
#dict only immutable data type can be key in dict . int ,float,stirng ,tuple
#all type of data can be value in thr dict
#

dict1={'a':100,'b':400,'a':500}
print(dict1)
#{'a': 500, 'b': 400}

dict1={'a':4,'b':100}
print(dict1,type(dict1))
#{'a': 4, 'b': 100} <class 'dict'>

dict1[4]='tushar'
dict1[(5,3,4)]=[4,6,8,9]
dict1[4.9]=(11,22,99)

print(dict1)

#{'a': 4, 'b': 100, 4: 'tushar', (5, 3, 4): [4, 6, 8, 9], 4.9: (11, 22, 99)}

#we can assign immutable datatype as key and valy can be any type of data.

#dict1[[3,4,4,2]]="tush aher"
print(dict1)
#TypeError: unhashable type: 'list'
#here we can not assign list as key coz its mutable.

#############################set#########################################

#set used to store unique data.duplicate data is not allowed
#{}
#set is mutable datatype .we can modify at any point of time
#set can only contain immutable data type as member int floar string boolean and tuple
#set does not follow indexing
#set does not follow order


set={1,2,3,4}

######programm for add odd and even num 1 to 20##################
odd_sum=0
even_sum=0

for i in range (1,21):
    if i%2==0:
         even_sum=even_sum+i
    else:
         odd_sum=odd_sum+i

print("even_sum:",even_sum)
print("odd_sum:",odd_sum)


################common between two list#####################

list1=[1,2,3,4]
list2=[1,2,3,5]

for val in list1:
    if val in list2:
        print(val)




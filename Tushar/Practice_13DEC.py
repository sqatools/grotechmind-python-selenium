#programme to find out the factorial of any number

num1=4
fact=1
for i in range (num1,0,-1):
    fact=fact*i
    print(fact)
print("+"*50)
###python program to get sum of all the number from 1 to 10

summation=0
for i in range (1,11):
    summation=summation+i
print("sum values:",summation)

print("+"*50)
###Apply loop on list data###############

list1=[10,20,80,90,5]
for val in list1:
    if val%2==0:
        print(val)

print("+"*50)
#add even and odd no from 1 to 20

even_sum=0
odd_sum=0
for val in range (1,21):
    if val%2==0:
        even_sum=even_sum+val
    else:
        odd_sum=odd_sum+val
print("even_sum:",even_sum)
print("odd_sum:",odd_sum)


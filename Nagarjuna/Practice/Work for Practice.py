result = int(input("please enter the value:"))
even_sum = 0
odd_sum = 0

for num in range(1 ,21):
    if(num %2 == 0):
      even_sum = even_sum+ num
    else:
        odd_sum = odd_sum + num
print("sum of even numbers :", even_sum )
print("sum of odd numbers:", odd_sum)


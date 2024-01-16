
"""1.  Numbers
    a).  Integer
    b).  Float
    c). Complex Number

2.  Sequencial data type
    d). String
    e). Tuple
    f). List

3. Dictionary

4.Set
5.Boolean"""

#Interger Type Conversion to Float""
"""Number=40
Num2=float(Number)
print(Num2,type(Num2))"""""

#Integer to String
'''Number= 98765
Str1=str(Number)
print(Str1,type(Str1),Str1[3])'''


#int to  Tuple conversion not possible
#int to Set conversion not possible
#int to Dict conversion not possible

#Int to bollen
'''number =0
var= bool(number)
print(var,type(var))'''

#Float to int
'''Number=10.89
var=int(Number)
print(var,type(var))'''

#Float to String
'''Float1=23.56
String=str(Float1)
print(String,type(String),String[2])'''

# float -> list : conversion is not possible
# float -> tuple : conversion is not possible
# float -> dict : conversion is not possible
# float -> set : conversion is not possible

#Float to boolean True value
'''Num3 = 66.35
Float1=bool(Num3)
print(Float1,type(Float1))'''

#Float to Boolean False value
'''Num3 = 0
Float1=bool(Num3)
print(Float1,type(Float1))'''

#String to Integer ( not possible)
'''stringa = "Home lane"
inte=int(stringa)
print(stringa,type(stringa))'''

#ValueError: invalid literal for int() with base 10: 'Home lane'

#if String contains only numbers then string to integer is possible

'''StringI = "6775444"
Num = int(StringI)
print(Num,type(Num),Num*4)'''

## Pyramid of horizontal tables of numbers
"""rows = 100
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i * j, end=' ')
    print()
"""

#String to Tuple

'''git pull update repository
git status to check the newly added file rec colour
git add . (to add all avaliable file changes done by me 
git commint -m "file added"
git push '''

"""x=100
for i in range(100):
    print(i)
"""

"""for num in range(10, 14):
   for i in range(2, num):
       if num%i == 1:
          print(num)
          break"""

"""Enter_number1=input("Enter Number 1:")
Enter_number2=input("Enter Number 2: ")
result = int(Enter_number1)+int(Enter_number2)
print("Sum =",result)"""

#//////////////////////////////////////////////////////////
number = input("Enter Two digit number for Addition :")
first_digit=number[0]
second_digit=number[1]
result=int(first_digit)+int(second_digit)
print(result)

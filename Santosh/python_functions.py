def function():
    print("hello")
    print("how is going python practice")
function()

print("*"*50)

def function(name):
    print("hello",name)
    print("how is going python practice")
function("Deepesh. you are good teacher")

print("*"*50)
# pass by value
def add_value(val1,val2):
    print(val1+val2)
add_value(2,3)

print("*"*50)

# pass by reference

def add_numbers(n1,n2):
    result=n1+n2
    print(result)
number1=100
Number2=12.5
add_numbers(number1,Number2)

print("*"*50)

def add_numbers(a,b):
    result=8+10
    print(result)
add_numbers(2,5)

print("*"*50)

def add_numbers(a,b):
    result=8+b
    print(result)
add_numbers(2,5)

print("*"*50)

def add_numbers(n1,n2):
    result=n1+n2
    print("Sum is :",result)
number1=100
Number2=12.12
add_numbers(number1,Number2)

print("*"*50)

def add_numbers(n1,n2):
    result=n1+n2
    return result
number1=100
Number2=12.12
result=add_numbers(number1,Number2)
print(result)

print("*"*50)

def function(name):
    print("hello",name)
    return
    print("how is going python practice")
function("santosh")

print("*"*50)

#fuction to find Avg marks
def Avrage_marks(marks):
    sum_marks=sum(marks)
    Total_marks=len(marks)
    Avrage_marks=sum_marks/ Total_marks
    return Avrage_marks
# function to calculate compute grade
def compute_grade(Avrage_marks):
    if Avrage_marks>=80:
        grade="A"
    elif Avrage_marks>=60:
        grade="B"
    elif Avrage_marks>=40:
        grade="C"
    else:
        grade="F"
    return grade

marks=[30,45,50,10,100,80]
Avrage_marks=marks
print("your Avg marks is:",Avrage_marks)
grade=compute_grade(compute_grade)
print("your grade is:",grade)






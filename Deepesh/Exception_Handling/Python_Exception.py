
# show user defined error msg
"""
try:
    num1 = 30
    num2 = "Hello"
    print("add :", num1+num2)
except:
    print("Can not add int with string")

# num1 = 30
# num2 = "Hello"
# print("add :", num1+num2)

print("Multiplication:", 40*4)
"""

"""
# show system generated error msg as well user defined msg
try:
    num1 = 30
    num2 = "Hello"
    print("add :", num1+num2)
except Exception as e:
    print("Can not add int with string")
    print(e)
    # Can not add int with string
    # unsupported operand type(s) for +: 'int' and 'str'
"""

# Raise explicit error msg
def addition():
    try:
        num1 = 30
        num2 = "Hello"
        print("add :", num1+num2)
    except Exception as e:
        #print("Can not add int with string")
        #raise e
        raise "Can not add int with string"

#addition()

# try - except - else  condition

def try_except_else(num1, num2):
    try:
        print("division :", num1/num2)
    except Exception as e:
        print("Mathematical error, division is not successful")
        print(e)
    else:
        # if there is exception code, then this code won't execute
        print("Code execution is successful")


#try_except_else(40, 0)
# try_except_else(40, 2)


# try - except - else and finally section excution.

def try_except_else_finally(num1, num2):
    try:
        print("division :", num1/num2)
    except Exception as e:
        print("Mathematical error, division is not successful")
        print(e)
        #raise
    else:
        # if there is exception code, then this code won't execute
        print("Code execution is successful")

    finally:
        # This code is going to execute if there is exception or no exception.
        print("square of num1 :", num1**2)


#try_except_else_finally(44, 0)
#try_except_else_finally(44, 3)

# handled multiple exception

def multiple_exception(num1, num2):
    try:
        print(" addition :", num1+num2)
        print(" multiplication :", num1*num2)
        print(" division :", num1//num2)
        print(" square :", num1**2)
        assert num1 == num2

    except TypeError:
        print("both values should be number")
    except ZeroDivisionError:
        print("Can not divide number by zero")
    except ArithmeticError:
        print("Can not divide string with number")
    except AssertionError:
        print("Both values are not equal")


#multiple_exception(30, 'Hello')
#multiple_exception(30, 0)
#multiple_exception(30, 2)


def multiple_exception2(num1, num2):
    try:
        print(" addition :", num1+num2)
    except TypeError:
        print("Can not add int with string")

    try:
        print(" multiplication :", num1*num2)
    except ArithmeticError:
        print("Can not multiple special character")

    try:
        print(" division :", num1//num2)
    except ZeroDivisionError:
        print("Can not divide number with zero")
    except TypeError:
        print("Can not divide the string with number")


#multiple_exception2(30, 'Hello')
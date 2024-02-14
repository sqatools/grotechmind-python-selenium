def addition(a, b):
    try:
        print('addition:', a + b)
        print('excuation sucessfull')
    except:
        print('type error')


# addition(10,'hello')

def multi(a, b):
    try:
        print('addition:', a + b)
        print('excuation sucessfull')
    except Exception as e:
        print('type error')
        print(e)


# multi(10,'hi')

def chakri(a, b):
    try:
        print('division:', a / b)
    except Exception as e:
        print(e)
        raise 'can not divide by 0'


# chakri(10,0)

def mutiple(a, b):
    try:
        print(a + b)
        print(a * b)
        print(a / b)
        print(a ** b)
        print(a - b)
        print(a == b)
    except TypeError:
        print('type error')
    except ZeroDivisionError:
        print('cant divide with zero')
    except ArithmeticError:
        print('arithmetic error')
    except AssertionError:
        print('values are not equal')


# mutiple(10,20)


def exception_as(a, b):
    try:
        print(a + b)
        print(a * b)
        print(a / b)
        print(a ** b)
        print(a - b)
        print(a == b)
    except TypeError:
        print('type error')
    except ZeroDivisionError:
        print('cant divide with zero')
    except ArithmeticError:
        print('arithmetic error')
    except AssertionError:
        print('values are not equal')

    else:
        print('code is success fully excuated ')
    finally:
        print(a % 2, b % 2)


def exception_else(a, b):
    try:
        print(a/b)
    except Exception as e:
        print('this is not possible')
        #print(e)
        raise 'division by zero is not possible'
    else:
        print('success fully excuated')
    finally:
        print(a+b)
exception_else(10,'hi')

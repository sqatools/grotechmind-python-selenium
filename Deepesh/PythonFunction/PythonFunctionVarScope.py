"""
Variables scope
global variable : scope of global variable is available in entire module
local variable : local variable scope is limited to the function
nonlocal variable :  non local variable scope is limited to the all the inner functions.
"""

# global variable
varp = 500

def function_a():
    print("_____function_a_____")
    #global varp
    varq = 400 # local variable
    varp = 700
    print("varp :", varp)
    print("varq :", varq)
    return varp

def function_b():
    print("_____function_b_____")
    vars = 300 # local variable
    print("varp :", varp)
    print("vars :", vars)


varp = function_a()
print('var1 :', varp)
function_b()


# Nested function
print("___"*50)
varx = 601 # global variable

def outer_function():
    vary = 500 # Non local variable
    print("----outer function -----")
    print("vary non local variable :", vary)

    def inner_function1():
        print("--inner function1 ---")
        varz = 300 # local variable
        global varx
        nonlocal vary
        print("varz :", varz)
        print("vary:", vary)
        print("varx :", varx)
        vary = 900
        varx = 1000

    def inner_function2():
        print("--inner function2 ---")
        varj = 200 # local variable
        print("varj :", varj)
        print("vary:", vary)
        print("varx :", varx)

    if varx == 600:
        inner_function1()
    else:
        inner_function2()


#outer_function()
#outer_function.inner_function2()
#outer_function().inner_function2()

#outer_function()


def addition(num1, num2):
    return num1+num2

def multiplication(a, b, c):
    add = addition(a, b)
    result = add*c
    print("result :", result)


multiplication(40, 50, 3)


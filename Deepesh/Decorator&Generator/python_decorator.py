
def decorate(func):
    def inner(msg):
        print("Have a nice Day")
        val= func(msg)
        print("Hope you are doing good")
        return val
    return inner

@decorate
def greeting(msg):
     return msg


result = greeting("Very good evening")
print(result)

# def greeting(msg):
#     return msg
#
# val = greeting("Hello Good Morning")
# print(val)
#
print("_"*50)
def welcome(abc):
    def inner(num1, num2):
        print("Welcome to Python Programming")
        if isinstance(num1, int) and isinstance(num2, int):
            abc(num1, num2)
        else:
            print("Invalid input values , it should be int")

    return inner

@welcome
def addition(num1, num2):
    print("addition :", num1+num2)


x = 'Name'
y = 80
addition(x, y)
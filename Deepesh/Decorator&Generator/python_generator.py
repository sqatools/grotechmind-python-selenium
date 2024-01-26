def greeting():
    return "good morning"
    return "Have a nice day"

msg = greeting()
print(msg)

# function with generator

def greeting_msg():

    yield "Good Morning"
    yield "Have a nice"
    yield "Welcome to Python Programming"
    yield "Python is easy to learn"

val = greeting_msg()
print(val)
print(next(val))
print(next(val))
print(next(val))
print(next(val))
print(next(val))

# for msg in val:
#     print(msg)
#
# print(next(val))


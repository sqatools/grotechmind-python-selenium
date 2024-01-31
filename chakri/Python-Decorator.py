def decorate(func):
    def inner(msg):
        #print("Have a nice Day")
        val= func(msg)
        #print("Hope you are doing good")
        return val
    return inner

@decorate
def greeting(a):
     return a
r = greeting('hello chakri')
print(r)

# import pyttsx3
# bot= pyttsx3.init()
# bot.say("my name is santosh")
# bot.runAndWait()

class product:
    pass
prods=[]

for i in range(1,4):
    obj=product()
    #print(obj)
    obj.price = i *6
    #print(obj.price)
    prods.append(obj)
    print(prods)

for prod in prods:
    if prod.price >10:
        print(prod.price)

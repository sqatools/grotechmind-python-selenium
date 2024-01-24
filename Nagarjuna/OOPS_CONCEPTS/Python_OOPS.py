"""
class : class is the blueprint of the object is being created.
object : object is the entity through we can access all the properties and attribute of the class.
method : This is block of code there we can define the code login to and set different properties to the class.
         1. Instance Method/object method
         2. Class Method
         3. Static Method
variable : This is placeholder to assign values
          1. class variable
          2. instance variable
constructor : Constructor which initialize the memory of the object
          1. Default Constructor :
             When we create an object, then automatically in the background default constructor
             initialize the memory of the object.
          2. Parametrize Constructor :

self : self is nothing but the object of the current class which is being used.
module : Each python file module name is __main__ module, once we call the file
         in some other file, then filename will become module name.
inheritance
polymorphism
abstraction
"""

class naga:
    def wishes(self):
        print("hello good morning")
obj = naga()
obj.wishes()
print(type(obj))  # <class '__main__.naga'>

print("OOPS CONCEPTS")
class practice:
    country = "India"   # class variable

    def __int__(self, a, b):  # constructor
        print("initializing the memory")
        self.a_val = a   # instance variable
        self.b_val = b   # instance variable

    #instance method / object method
    def display(self):
        print("value of a: ", self.a_val)
        print("value of b: ", self.b_val)


obj = practice(10,24)
obj.display()


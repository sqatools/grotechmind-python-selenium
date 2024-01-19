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
inheritance
polymorphism
abstraction
"""

class ABC:
    country = "India" # class variable

    def __init__(self, a, b):  # constructor
        print("Initializing the memory")
        self.a_val = a  # instance variable
        self.b_val = b  # instance variable

    # instance method / object method.
    def greeting(self, var1, var2):
        print("Good Morning")
        print("value of a:", self.a_val)
        print("value of b:", self.b_val)
        print("var 1:", var1)
        print("var 2:", var2)
        print("country name :", self.country)

    def show_city_name(self, city_name):
        print("city_name :", city_name)


# obj = ABC(50, 60)
#obj.greeting(100, 200)
#obj.show_city_name("Mumbai")

#ABC.show_city_name("Bangalore", "Mumbai")

"""
print(type(obj))

str1 = "Hello"
str1.split()
print(type(str1))
"""
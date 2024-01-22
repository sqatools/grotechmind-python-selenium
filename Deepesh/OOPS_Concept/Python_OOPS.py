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

class ABC:
    country = "India" # class variable

    def __init__(self, a, b):  # constructor
        print("Initializing the memory")
        self.a_val = a  # instance variable
        self.b_val = b  # instance variable
        self.c_val = 50
        self.show_city_name("Bangalore")

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
        print(" c variable",  self.c_val)


# obj = ABC(50, 60)
#obj.greeting(100, 200)
#obj.show_city_name("Mumbai")

#ABC.show_city_name("Bangalore", "Mumbai")

# obj1 = ABC(100, 300)



"""
print(type(obj))

str1 = "Hello"
str1.split()
print(type(str1))
"""


class car:

    country = "India" # class variable
    def __init__(self, car_name, comp_name, car_price):
        self.car_name = car_name
        self.company_name = comp_name
        self.car_price = car_price

    # instance method
    def show_car_name(self):
        print("Car name is :", self.car_name)

    # instance method
    def show_car_price(self):
        print("Car price :", self.car_price)

    # instance method
    def show_car_company(self):
        print("Company name is :", self.company_name)

    @classmethod
    def show_car_country(cls):
        print("Country name :", cls.country)

    @staticmethod
    def show_car_milege(milege):
        print("Car milege :", milege)


# in python each default module name is main (__main__)

if __name__ == '__main__':
    # obj = car("Swift", "Maruti", "8 Lac")
    # obj.show_car_name()
    # print(obj.__module__)   # __main__
    # obj.show_car_country()
    # obj.show_car_milege(20)

    car.show_car_milege(25)
    car.show_car_name()

# obj = car("Swift", "Maruti", "8 Lac")
# obj.show_car_name()
# print(obj.__module__)




# Assignment
# Create a class structure for IT company
# Create a class structure for School Institute
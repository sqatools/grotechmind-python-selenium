"""
class temp:

    def greetings(self):
        print("Hello World")

obj = temp()
obj.greetings()


print(type(obj))
print("@"*50)
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


obj = ABC(50, 60)
obj.greeting(100, 200)
"""

class IT:

    country = "India" # class variable
    def __init__(self, comp_name, comp_dept, comp_Address):
        self.comp_name = comp_name
        self.comp_dept = comp_dept
        self.comp_Addr = comp_Address

    # instance method
    def show_comp_name(self):
        print("Comp name is :", self.comp_name)

    # instance method
    def show_comp_dept(self):
        print("Company  department :", self.comp_dept)

    # instance method
    def show_comp_addr(self):
        print("Company Address is :", self.comp_addr)

    @classmethod
    def show_ITcomp_country(cls):
        print("Country name :", cls.country)

    @staticmethod
    def show_comp_Grade(A):
        print("Company Grade :", A)

if __name__ == '__main__':
     obj=IT("infosec","HR","Chennai_560012")
     print(obj.__module__)


"""
bj = IT("infosec","HR" "Chennai_560012")
obj.show_comp_name()
print(obj.comp_name)o

"""
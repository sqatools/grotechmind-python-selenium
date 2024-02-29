# 1). Python oops program to create a class with the constructor.
"""
class xyz:

    def __init__(self):
        print("my name is tushar")

    def father_name(self):
        print("my father name is suresh")

obj=xyz()
obj.father_name()
"""
"""

class village :

    def __init__(self,village_name,village_dist):
        self.village_name=village_name
        self.village_district=village_dist

    def display_village_name(self):
        print("village name is:",self.village_name)
        print("village is in:",self.village_district)
        print("village is in:",self.village_district)

    def dispaly_village_dist(self):
        print("village is in:",self.village_district)
if __name__=='__main__':

     obj=village("palkhed","nashik")
     obj.display_village_name()
"""

# 2). Python oops program to create a class with an instance variable.
"""
class instance_var:  #define class
    def __init__(self): #define constructor
        self.inst_var=15 #declare instance variable

obj=instance_var() #declare object of class
print(obj.inst_var) #print instance variable
"""

# 3). Python oops program to create a class with Instance methods.
"""
class house: #declare class

    def __init__(self,house_name,house_address):  #declare constructor
        self.house_name=house_name   #declare variable
        self.house_address=house_address

    def house_details(self):                   #instance method
        print("house_name:",self.house_name)
        print("house_address:",self.house_address)

    def update_house_details(self,new_house_name,new_house_address):
        self.house_name=new_house_name
        self.house_address=new_house_address

obj=house("prem","pune")
obj.house_details()

obj.update_house_details("shram safalya","nashik")
obj.house_details()
"""


# 4). Python oops program to create a class with class variables.
"""

class class_var:
    country="india"
    
    @classmethod
    def dispaly_country (cls):
        print("country_name:",cls.country)

class_var.dispaly_country()

"""


# 5). Python oops program to create a class with a static method.
"""
class class_with_static_method():

    @staticmethod
    def country_revenue(revenue):
        print("country revenue:",revenue)
class_with_static_method.country_revenue(500)

"""

# 7). Write a Python Class to get the class name and modules name.
"""
class house:
    pass
obj=house()

print("module_name:",obj.__module__)   # __main__
print("class_name:",obj.__class__.__name__)

class MyClass:
    pass

obj = MyClass()
print("Class name:", obj.__class__.__name__)
print("Module name:", obj.__module__)
"""


# 8) Write a Python Class object under syntax if __name__ == ‘__main__’.
"""
class movie:

    def __init__(self,movie_name,movie_relese_month):
        self.movie_name=movie_name
        self.movie_release_month=movie_relese_month

    def movie_details(self):
        print("movie_name",self.movie_name)
        print("movie_release_month:",self.movie_release_month)

if __name__=='__main__':
  obj=movie("chak de india","march")
  obj.movie_details()
  print(obj.__module__)
  print(obj.__class__.__name__)

"""



# 9). Python class with Single Inheritance.

class father:

    def __init__(self,fname,fcar):
        self.father_name=fname
        self.father_car=fcar

    def father_details(self,flocation):

        print("father_name is:",self.father_name)
        #print("father_car is :",self.father_car)
        #print("father location:",flocation)

obj=father("suresh","alto")
#obj.father_details("nashik")


class son(father):
    def __init__(self, sname, sage, fname, fcar):
        super().__init__(fname, fcar)
        self.son_name=sname
        self.son_age=sage

    def son_details(self):
        print("son_name:",self.son_name)
        #print("son_age:",self.son_age)
if __name__=='__main__':
    obj=son("tushar",34,"suresh","nexon")
    obj.son_details()
    obj.father_details("nanded")



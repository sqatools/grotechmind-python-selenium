# class hr_schema:
#     def __init__(self,employee_id,ename,esalary,dname,d_id,location_id,location_name):
#         self.employee_id=employee_id
#         self.ename=ename
#         self.esalary=esalary
#         self.dname=dname
#         self.d_id=d_id
#         self.location_id=location_id
#         self.location_name=location_name
#     def employee(self):
#         print("employee id is :",self.employee_id)
#         print("employee name is :",self.ename)
#         print("employee salary is :",self.esalary)
#         print("location name is :",self.location_name)
#
#     def department(self):
#         print("department name is :",self.dname)
#         print("department id is :",self.d_id)
#     def location(self):
#         print("location id is :",self.location_id)
#         print("location name is :",self.location_name)
#
# A=hr_schema("101","santosh","2000","mechanical","30","900","pune")
# A.employee()
# #obj.location()
# #obj.department()


# class hr_schema:
#     def __init__(self):
#         print("hello")
#     def employee(self,employee_id,first_name,salary):
#          print("employee id is :",employee_id)
#          print("employee name is :",first_name)
#          print("employee salary is :",salary)
#     def department(self,dept_id,dname):
#
#         print("department name is :",dname)
#         print("department id is :",dept_id)
#     def location(self,location_id,location_name):
#         print("location id is :",location_id)
#         print("location name is :",location_name)
#
# obj=hr_schema
# obj.employee("100","jhon","980000","99000")
# #obj.location()
# #obj.department()
# #hr_schema.department("A","B","p")


# class ABC:
#     country = "India"  # class variable
#
#     def __init__(self, a, b):  # constructor
#         print("Initializing the memory")
#         self.a_val = a  # instance variable
#
#         self.b_val = b  # instance variable
#
#         self.c_val = 50
#         self.show_city_name("pune")
#
#     # instance method / object method.
#     def greeting(self, var1, var2):
#         print("Good Morning")
#         print("value of a:", self.a_val)
#         print("value of b:", self.b_val)
#         print("var 1:", var1)
#         print("var 2:", var2)
#         print("country name :", self.country)
#
#     def show_city_name(self, city_name):
#         print("city_name :", city_name)
#         #print(" c variable", self.c_val)
#
#
# obj =  ABC(111, 333)
# obj.greeting(100, 200)
# obj.show_city_name("Mumbai")
#
# ABC.show_city_name( "self","nashik")

#obj1 = ABC(111, 333)

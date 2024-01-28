
# 1). Python oops program to create a class with the constructor.
print("1). Python oops program to create a class with the constructor.")



class MyClass:
	def __init__(self, name):
		self.name = name
	def display_name(self):
		print("Name: ", self.name)

obj = MyClass('Shekhar Tyagi')
obj.display_name()

# 2). Python oops program to create a class with an instance variable.
print("2). Python oops program to create a class with an instance variable.")

class MyClass:
	def __init__(self):
		self.instance_var = 1996

obj = MyClass()
print(obj.instance_var)

# 3). Python oops program to create a class with Instance methods.
print("3). Python oops program to create a class with Instance methods.")

class MyClass:
	def __init__(self, name):
		self.name= name
	def display_name(self):
		print("Name:", self.name)

	def New_Name(self, New_Name):
		self.name = New_Name

obj = MyClass("Shekhar")
obj.display_name()

obj.New_Name("SHekhar Tyagi")
obj.display_name()

# 4). Python oops program to create a class with class variables.
print("4). Python oops program to create a class with class variables.")

class MyClass:
	class_var = "Hello, I'm Shekhar Tyagi"
print(MyClass.class_var)























"""
class Employee:
    def __init__(self, employee_id, name, position):
        self.employee_id = employee_id
        self.name = name
        self.position = position

    def display_info(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Position: {self.position}")


class Department(Employee):
    def __init__(self, department_id, name):
        self.department_id = department_id
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_info(self):
        print(f"Department ID: {self.department_id}, Name: {self.name}")
        print("Employees:")
        for employee in self.employees:
            employee.display_info()


class ITCompany(Department):
    def __init__(self, company_name):
        self.company_name = company_name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def display_info(self):
        print(f"Company Name: {self.company_name}")
        print("Departments:")
        for department in self.departments:
            department.display_info()



if __name__ == "__main__":
    employee1 = Employee(1, "John Doe", "Software Engineer")
    employee2 = Employee(2, "Jane Smith", "QA Engineer")


    development_department = Department(101, "Development")
    testing_department = Department(102, "Testing")

    development_department.add_employee(employee1)
    testing_department.add_employee(employee2)

    it_company = ITCompany("GrowTechMind")

    it_company.add_department(development_department)
    it_company.add_department(testing_department)

    it_company.display_info()

"""
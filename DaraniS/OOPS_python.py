class company:
    company_location = "Canada"
    def __init__(self,emp_name,emp_id,emp_department):
        self.employee_name = emp_name
        self.employee_id = emp_id
        self.employee_department = emp_department

    def IT_employee_name(self):
        print("Employee name is ",self.employee_name)

    def IT_employee_Id(self):
        print("Employee id id" ,self.employee_id)

    def IT_employee_department(self):
        print("Employee department is", self.employee_department)

    def Company_location(cls):
        print("Company location",cls.company_location)

    def company_MD(md_name):

        print("Company MD name",md_name)
if __name__ == '__main__':
        obj = company("Darani","20", "In IT Department as associate developer")
        obj.Company_location()
        obj.company_MD("John")
        print(obj.__module__)
# IT Company
"""
class company:

    country = "india"

    def __init__(self,company_name,company_place,company_staff):
        self.company_name= company_name
        self.company_place= company_place
        self.company_staff = company_staff

    def show_company_name(self):
        print("company name is : ", self.company_name)

    def show_company_place(self):
        print("company place is : ", self.company_place)

    def show_company_staff(self):
        print("company has a staff of: ", self.company_staff)

    @classmethod
    def show_country_name(cls):
        print("country name :", cls.country)

    @staticmethod
    def show_company_salary(salary):
        print("salary from the company :", salary)

if __name__ == '__main__':

    obj = company("HPE","bangalore","1000000")
    obj.show_company_name()
    obj.show_company_place()
    obj.show_company_staff()
    company.show_country_name()
    company.show_company_salary(50000)
 """

# SCHOOL

class school:
    student_name= "Naga"

    def __init__(self,schl_name,schl_place,schl_type):
        self.school_name = schl_name
        self.school_place = schl_place
        self.school_type = schl_type

    def show_school_name(self):
        print("school name is : ", self.school_name)

    def show_school_place(self):
        print("school is located at : ", self.school_place)

    def show_school_type(self):
        print("school type is :", self.school_type)

    @classmethod
    def show_student_name(cls):
        print("student name is : ",cls.student_name)

    @staticmethod
    def show_school_strength(total):
        print("school strength is : ",total)

if __name__ == '__main__':
    obj = school("raghava vidya nilayam", "guntur","secondary school")
    obj.show_school_name()
    obj.show_school_place()
    obj.show_school_type()
    school.show_student_name()
    school.show_school_strength(10000)
    print(obj.__module__)

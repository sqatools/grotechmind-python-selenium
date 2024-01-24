# Assignment
# Create a class structure for IT company
# Create a class structure for School Institute
'''
class Company:
    country = "india"
    def __init__(self, c_name, c_location, c_owner):
        self.company_name = c_name
        self.company_location = c_location
        self.company_owner = c_owner

    def c_name(self):
        print('company name:',self.company_name)

    def c_location(self):
        print('company location:',self.company_location)

    def c_owner(self):
        print('company owner:',self.company_owner)

    @classmethod
    def c_country(cls):
        print('company country :',cls.country)
    @staticmethod
    def c_salary(salary):
        print('salary:',salary)


#if __name__ == '__main__':
a = Company("tcs", "Hyderabad", "ratan tata")
a.c_location()
a.c_owner()
#a.c_name()
a.c_salary(50000)
a.c_country()
'''
# Create a class structure for School Institute

class School:
    student = 'chakri'
    def __init__(self,syl,sl_name,principal):
        self.syllabus = syl
        self.sl_name = sl_name
        self.principal = principal

    def sl_syllabus(self):
        print('school syllabus:',self.syllabus)

    def school_name(self):
        print('school name:',self.sl_name)

    def principal_name(self):
        print('principl name:',self.principal)

    @classmethod
    def student_name(cls):
        print('student name:',cls.student)

    @staticmethod
    def marks(scored):
        print(scored)

b = School("CBSE","zpph high school","Soma sekhar")
if __name__ == '__main__':
 b.sl_syllabus()
 b.principal_name()
 b.student_name()
 b.school_name()
 b.marks(80)


















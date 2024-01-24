# Create a class structure for IT company
"""
#Step 1: We have to first defined the class

class company:

       country='India'  #class variable for classic method

#Step2: Then define the constructor--To Intialzied the memory of object

       def __init__(self,company_name,company_address,company_type,company_services):
              self.company_name=company_name
              self.company_address=company_address
              self.company_type=company_type
              self.company_services=company_services

##instance method / object method

       def display_company_name(self):
              print("company name is :",self.company_name)

       def display_company_address(self):
              print("company address is :",self.company_address)

       def display_company_type(self):
              print("company type is :",self.company_type)

       def display_company_services(self):
              print("company services is :",self.company_services)

##class method

       @classmethod
       def display_company_country(cls):
              print("Country name :", cls.country)

##Static method

       @staticmethod
       def display_company_turnover(turnover):
              print("company turnover :", turnover)


if __name__ == '__main__':

## object create

       obj=company("Infosys","Pune","Servic","Testing")

       obj.display_company_name() #Infosys

       obj.display_company_address() #Pune

       obj.display_company_type() #Servic

       obj.display_company_services() #Testing

       print(obj.__module__)  #__main__


       company.display_company_country()

       company.display_company_turnover(500)

"""
##############################################################################################
"""

#Create a class structure for School Institute


class school:

       country="india"

       def __init__(self,school_name,school_address,school_pattern):
              self.school_name=school_name
              self.school_address=school_address
              self.school_pattern=school_pattern

       def display_school_name(self):
              print("school name is :",self.school_name)

       def display_school_address(self):
              print("school address is :",self.school_address)

       def display_school_pattern(self):
              print("school pattern is:",self.school_pattern)

       @classmethod
       def display_school_country(cls):
              print("school in:",cls.country)

       @staticmethod
       def display_school_fees(fees):
              print("school fees is:",fees)

if __name__ == '__main__':

       obj=school("Delhi public school","Nashik","ICSE")

       obj.display_school_name()
       obj.display_school_address()
       obj.display_school_pattern()


       school.display_school_country()

       school.display_school_fees(500000)

"""

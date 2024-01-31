"""
Inheritance : When one class aquare the property of another class then it is known as inheritance.

1. Single Inheritance
2. Multi Level Inheritance
3. Multiple Inheritance
3. Heirachical Inheritance
"""


# Multiple Inheritance
# A ->  B, C -> B

class father:
    def __init__(self, fname, fbusiness, fhouse):
        self.fname = fname
        self.fbusiness = fbusiness
        self.fhouse = fhouse

    def show_father_details(self):
        print("Father name :", self.fname)
        print("Father Business :", self.fbusiness)
        print("Father House :", self.fhouse)


class mother:
    def __init__(self, mname, mbusiness):
        self.mname = mname
        self.mbusiness = mbusiness

    def show_mother_details(self):
        print("Mother name :", self.mname)
        print("MOther business :", self.mbusiness)


# MRO : Method Resolution Order
class son(mother, father):
   #  address = "Borvali Mumbai"  # class variable

    def __init__(self, sname, mname, mbusiness, fname, fbusiness, fhouse):
        super().__init__(mname, mbusiness)
        self.sname = sname
        self.fobj = father(fname, fbusiness, fhouse)

    def show_son_name(self):
        print("Son name is :", self.sname)
        #self.city = "Mumbai"

    def show_city_name(self):
        print("city name :", self.city)

    def show_family_details(self):
        self.show_son_name()
        self.show_mother_details()
        self.fobj.show_father_details()

    @staticmethod
    def country_name(country):
        print("Country Name :", country)

    @classmethod
    def show_address_name(cls):
        print("address :", cls.address)


if __name__ == '__main__':
    obj = son("Shreshth", "Neha", "Fashion", "Mohan", "Construction", "Duplex house")
    obj.show_son_name()
    obj.show_mother_details()
    obj.fobj.show_father_details()
    # obj.show_city_name()
    #obj.show_family_details()

    # son.show_son_name()
    # calling static method with class name
    #son.country_name('India')
    #son.show_address_name()

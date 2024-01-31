"""
Inheritance : When one class aquare the property of another class then it is known as inheritance.

1. Single Inheritance
2. Multi Level Inheritance
3. Multiple Inheritance
3. Heirachical Inheritance
"""
# 1. Single Inheritance

class father:
    def __init__(self,fname,fbike,flocation):
        self.father_name = fname
        self.father_bike = fbike
        self.father_location = flocation

    def show_father_name(self):
        print("Father name is : ", self.father_name)

    def show_father_bike(self):
        print("Father bike is : ", self.father_bike)

    def show_father_location(self):
        print("Father location is : ", self.father_location)

    def show_father_details(self):
        self.show_father_name()
        self.show_father_bike()
        self.show_father_location()

#obj = father("MVN Rao", "activa125 cc", "hyd")    # callin only father with obj
#obj.show_father_details()                         # calling the father details method with obj

# Child class
class son(father):
    def __init__(self, sname, sstudy, fname, fbike, flocation):
        super().__init__(fname, fbike, flocation)
        self.son_name = sname
        self.son_study = sstudy

    def show_son_name(self):
        print("Son name is : ",self.son_name)
    def show_son_study(self):
        print("Son studied :", self.son_study)

    def show_son_details(self):
        self.show_son_name()
        self.show_son_study()

    def show_family_details(self):
        self.show_father_details()
        self.show_son_details()
"""
obj = son("NAGA","BE","MVN RAO","ACTIVA125 CC","HYD")
obj.show_family_details()
print("%"*30)
obj.show_son_details()
obj.show_father_details()
"""

if __name__ == '__main__':
    obj = son("ARJUN","BE","MVN RAO","ACTIVA125 CC","HYD")
    obj.show_family_details()
    print(obj.__module__)

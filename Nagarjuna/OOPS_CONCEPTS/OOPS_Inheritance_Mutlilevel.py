"""
Inheritance : When one class aquare the property of another class then it is known as inheritance.

1. Single Inheritance
2. Multi Level Inheritance
3. Multiple Inheritance
3. Heirachical Inheritance
"""
# 2. Multilevel Inheritance

class grandfather:
    def __init__(self,gf_name,gf_land):
        self.grand_father_name = gf_name
        self.grand_father_land = gf_land

    def show_grand_father_name(self):
        print("Grand Father Name : ", self.grand_father_name)

class father(grandfather):
    def __init__(self, fname, fbike, fhouse, gf_name, gf_land):
        super().__init__(gf_name, gf_land)
        self.father_name = fname
        self.father_bike = fbike
        self.father_house = fhouse

    def show_father_name(self):
        print("Father name is :", self.father_name)

    def show_father_bike(self):
        print("Father bike is :", self.father_bike)

    def show_father_house(self):
        print("Father house : ", self.father_house)

    def show_father_details(self):
        self.show_father_name()
        self.show_father_bike()
        self.show_father_house()

    def show_grandfather_land(self):
        print("Grandfather property name : ",self.grand_father_land)

# CHILD CLASS
class son(father):

    def __init__(self, sname, sstudy, fname, fbike, fhouse, gf_name, gf_land):
        super().__init__(fname, fbike, fhouse, gf_name, gf_land)
              # initialize the parent class constructor
        self.son_name = sname
        self.son_study = sstudy

    def show_son_name(self):
        print("Son name is : ", self.son_name)

    def show_son_study(self):
        print("Son study is :", self.son_study)

    def show_son_details(self):
        self.show_son_name()
        self.show_son_study()

    def show_family_details(self):
        self.show_grand_father_name()
        self.show_grandfather_land()
        self.show_father_details()
        self.show_son_details()

# obj = son("akhil","B.E","nagarjuna","pulsar","mumbai","ANR","40 acres")
# obj.show_family_details()

if __name__ == '__main__':
    obj = son("akhil","B.E","nagarjuna","pulsar","mumbai","ANR","40 acres")
    obj.show_family_details()
    print(obj.__module__)

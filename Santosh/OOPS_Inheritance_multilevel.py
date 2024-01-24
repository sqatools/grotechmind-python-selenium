"""
Inheritance : When one class aquare the property of another class then it is known as inheritance.

1. Single Inheritance
2. Multi Level Inheritance
3. Multiple Inheritance
3. Heirachical Inheritance
"""
# 2. Multilevel Inheritance
class grandfather:
    def __init__(self, gf_name, gf_property):
        self.grand_father_name = gf_name
        self.grand_father_property = gf_property

    def show_grand_father_name(self):
        print("Grand father name :", self.grand_father_name)

# parent class
class father(grandfather):
    def __init__(self, fname, fcar, fhouse, gf_name, gf_property):
        super().__init__(gf_name, gf_property)
        self.father_name = fname
        self.father_car = fcar
        self.father_house = fhouse

    def show_father_name(self):
        print("Father name is :", self.father_name)

    def show_father_car(self):
        print("Father car is :", self.father_car)

    def show_father_house(self):
        print("Father Owns :", self.father_house)

    def show_father_details(self):
        self.show_father_name()
        self.show_father_car()
        self.show_father_house()

    def show_grand_father_property(self):
        print("Grandfather property name :", self.grand_father_property)


# child class
class son(father):

    def __init__(self, sname, education, fname, fcar, fhouse, gf_name, gf_property):
        #super().__init__(fname, fcar, fhouse, gf_name, gf_property)
        # initialize the parent class constructor
        super().__init__(fname, fcar, fhouse, gf_name, gf_property)
        self.son_name = sname
        self.son_education = education

    # def __init__(self):  # default constructor
    #     print("Hello Good Morning")
    #     self.evening_greet()
    #
    # def evening_greet(self):
    #     print("Good Evening, How are you?")

    def show_son_name(self):
        print("Son name is :", self.son_name)

    def show_son_education(self):
        print("Son Education :", self.son_education)

    def show_son_details(self):
        self.show_son_name()
        self.show_son_education()

    def show_family_details(self):
        self.show_father_details()
        self.show_son_details()


if __name__ == '__main__':
    obj = son('Mohit', "BE", "MOhan", "Harrier", "4 BHK", "HariRam", "200 Acr")
    obj.show_father_name()
    obj.show_son_education()
    print("_"*40)
    obj.show_family_details()
    print(obj.__module__)
    obj.show_grand_father_name()
    print("Property owns by grand father :", obj.grand_father_property)


#obj= son()



# obj = son('Mohit', "BE", "MOhan", "Harrier", "4 BHK")
# obj.show_father_name()
# obj.show_son_education()
# print("_"*40)
# obj.show_family_details()
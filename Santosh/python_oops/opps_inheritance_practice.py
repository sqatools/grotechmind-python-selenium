class Father:
    def __init__(self,Fname,fcar,fhouse ):
        self.father_name=Fname
        self.father_car=fcar
        self.father_house=fhouse
    def display_father_name(self):
        print("Father name is :",self.father_name)
    def show_father_car(self):
        print("father car name is :",self.father_car)
    def show_father_house(self):
        print("father house is ", self.father_house)
    def show_father_details(self):
        self.display_father_name()
        self.show_father_car()
        self.show_father_house()
# if __name__ == '__main__':
#      obj = Father("Ganesh", "Nexon", "8lakh")
#      obj.display_father_name()
#      obj.show_father_house()
#      print(obj.__module__)
#
#      obj.show_father_details()
class son(Father):
     def __init__(self,Sname,job, Fname, fcar, fhouse):
         super().__init__(Fname, fcar, fhouse)
         self.son_name = Sname
         self.son_education = job
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
    obj=son('Mohit', "It engineer", "Mohan", "Harrier", "4 BHK")
    print("*"*50)
    obj.show_family_details()





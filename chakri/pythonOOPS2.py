#1 1). Python oops program to create a class with the constructor.

'''class Chakri:
    def __init__(self,name):
        self.name = name
    def display_name(self):
        print("person name is:",self.name)

obj = Chakri('chakradhar')
obj.display_name()

#2). Python oops program to create a class with an instance variable.
class Chakri:
    def __init__(self):
        self.instance_vrl = 25
    def int_variable(self):
        print(self.instance_vrl)

obj = Chakri()
print(obj.instance_vrl)

#3). Python oops program to create a class with Instance methods.
class Village:
    def __init__(self,fvoter,mvoter):
        self.fvoters = fvoter
        self.mvoters = mvoter
    def female_voter(self):
        print('female voters in village:',self.fvoters)
    def male_voter(self):
        print('male voters in village:',self.mvoters)

a = Village(2380,3067)
a.female_voter()
a.male_voter()
#4). Python oops program to create a class with class variables
class My_class:
    c = 'hello'
print(My_class.c)

#5). Python oops program to create a class with a static method.
class Chakri:
    @staticmethod
    def chakri_marks(m):
        print(m)
Chakri.chakri_marks(98)

#6). Python oops program to create a class with the class method.
class Chakri:
    name = 'sainath'
    @classmethod
    def student_name(cls):
        print(cls.name)
Chakri.student_name()

class Chakri:
    pass
a = Chakri()
print(a.__class__.__name__)
print(a.__class__.__module__)
#8) Write a Python Class object under syntax if __name__ == ‘__main__’.
class Village:
    def __init__(self,fvoter,mvoter):
        self.fvoters = fvoter
        self.mvoters = mvoter
    def female_voter(self):
        print('female voters in village:',self.fvoters)
    def male_voter(self):
        print('male voters in village:',self.mvoters)

a = Village(234,560)
if __name__ == '__main__':
    a.female_voter()
    a.male_voter()
'''

#9). Python class with Single Inheritance.
class Father:
    def __init__(self,fname,bike,car,home):
        self.fname = fname
        self.bike = bike
        self.car = car
        self.house = home
    def father_name(self):
        print('fathar name:',self.fname)
    def father_bike(self):
        print('father bike:',self.bike)
    def father_car(self):
        print('father car:',self.car)
    def father_home(self):
        print('father home:',self.house)
    def father_details(self):
        print(self.fname)
        print(self.bike)
        print(self.house)
        print(self.car)

class Dughter(Father):
    def __init__(self, dname, dvillage, deuc, fname, bike, car, home):
        super().__init__(fname, bike, car, home)
        self.dname = dname
        self.dvillage = dvillage
        self.dedu = deuc
    def dughter_name(self):
        print('d name :',self.dname)
    def dughter_village(self):
        print('d village :',self.dvillage)
    def dughter_edu(self):
        print('dughter education:',self.dedu)

class Son(Dughter):
    def __init__(self, sname, fname, bike, car, home, dname, dvillage, deuc):
        super().__init__(dname, dvillage, deuc, fname, bike, car, home)
        self.sname = sname

    def son_name(self):
        print('son name:',self.sname)

    def family_members(self):
        print(self.fname)
        print(self.dname)
        print(self.sname)

a = Son('chakri','krishna','pulsar','swift','2BHK','bhvani','tpalem','10th')
a.father_details()
a.family_members()
a.father_bike()








































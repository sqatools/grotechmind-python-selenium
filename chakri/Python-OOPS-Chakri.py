# 1 1). Python oops program to create a class with the constructor.

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
a.father_name()

# 10). Python Class with Multiple Inheritance.

class Father:
    def __init__(self, fname, fbike, fjob, fhouse):
        self.fname = fname
        self.fbike = fbike
        self.fjob = fjob
        self.fhouse = fhouse

    def father_name(self):
        print('father name:', self.fname)

    def father_bike(self):
        print('father bike:', self.father_bike)

    def father_job(self):
        print('father job:', self.fjob)

    def father_house(self):
        print('fther house:', self.fhouse)

    def father_details(self):
        print('father name:', self.fname)
        print('father bike:', self.fbike)
        print('father job:', self.fjob)
        print('father house:', self.fhouse)


class Mother:
    def __init__(self, mname, mjob):
        self.mname = mname
        self.mjob = mjob

    def mother_name(self):
        print('mother name:', self.mname)

    def mother_job(self):
        print('mother job:', self.mjob)


class Son(Father, Mother):
    def __init__(self, sname, sage, fname, fbike, fjob, fhouse, mname, mjob):
        super().__init__(fname, fbike, fjob, fhouse)
        self.sname = sname
        self.sage = sage
        self.b = Mother(mname, mjob)
    def son_name(self):
        print('son name:',self.sname)
    def son_age(self):
        print('sone age:',self.sage)
a = Son('chakri',25,'krishna','pulsar','farmer','2bhk','parvathi','house wife')
a.son_age()
a.b.mother_name()
a.father_details()

#13). Python Class with Method Overloading

class Number:
    def __init__(self,v1,v2):
        self.v1 =v1
        delf.v2 = v2
    def multiplication(self):
        print('multipilcation :',v1*v2)
    def addition(self):
        print('addition:',v1+v2)

#13). Python Class with Method Overloading

class Greeting:
    def wish (self,a,b=None):
        if b is None:
            print(a)
        else:
            print(a,' ',b)

obj = Greeting()
obj.wish('hello')
obj.wish('hello','chakri')

#14). Python Class with Method Overriding.
class Number:
    def __init__(self,v1,v2):
        self.v1 =v1
        self.v2 = v2
    def multiplication(self):
        print('multipilcation :',self.v1*self.v2)
    def addition(self):
        print('addition:',self.v1+self.v2)
class Num(Number):
    def __init__(self, v3, v4, v1, v2):
        super().__init__(v1, v2)
        self.v3 =v3
        self.v4=v4
    def multiplication(self):
        print('multipilcation :',self.v4*self.v3)
 # this child method override parent methode when we have two methods in
 # two classes with same name.


a = Num(v1=3,v2=5,v3=8,v4=9)
a.addition()
a.multiplication()
'''

#15). Write a Python Class Program with an Abstract method.

'''class Chakri:
    def display_name(self):
        print('my name is chakri')


class Sainath(Chakri):
    def display_name(self):
        print('my name is sainath')

class Ramu(Chakri):
    def display_name(self):
        print('my name is ramu')

a = Sainath()
a.display_name()
b =  Ramu()
b.display_name()
#16). Write a Python Class program to create a class with data hiding.

class Person:
  def __init__(self,pname,pjob,phouse):
      self.pname = pname
      self.pjob = pjob
      self.phouse = phouse

  def display_name(self):
      print('person name:',self.pname)
  def _display_job(self):
      print('person name:',self.pjob)
  def __display_house(self):
      print('person house:',self.phouse)


a = Person('chakri','manual tester','2BHK')
a.display_name()
a._display_job()
a.__display_house()'''
#17). Python Class Structure for School Management System.

class School:
    def __init__(self,name):
        self.school = name
        self.students = []
        self.teachers =[]
        self.courses = []
    def school_name(self):
         print(self.school)
    def add_student(self,student):
        self.students.append(student)
    def remove_student(self,student):
        if student in self.students:
            self.students.remove(student)
    def add_t(self,tname):
        self.teachers.append(tname)
    def remove_t(self,tname):
        if tname in self.teachers:
            self.teachers.remove(tname)
    def addc(self,cname):
        self.courses.append(cname)
    def removec(self,cname):
        if cname in self.courses:
            self.courses.remove(cname)
    def students(self):
        print(self.students)












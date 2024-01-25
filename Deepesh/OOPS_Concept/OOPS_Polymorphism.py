# Polymorphism : When one individual Entity performing task then it is known polymorphism.

# Method Overriding : When two class have same method name, then child class method will
                    #  override the parent class method.
# Method Overloading : when one class have two methods with same name with different parameter
#                     then it is known as method overloading, but python does not support this
#                     functionality, so latest defined method will get priority.

# Operator overloading : when one operator is performing multiple task, then it is known operator overloading

class ABC:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def addition(self):
        print("Addition :", self.var1, self.var2)

    def multiplication(self):
        print("Multiplication :", self.var1*self.var2)

class XYZ(ABC):
    def __init__(self, num1, num2, num3, var1, var2):
        super().__init__(var1, var2)
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def addition(self):
        print("Addition of three variables :", self.num1+self.num2+self.num3)

    def division(self):
        print("division :", self.num1//self.num2)

class PQR(XYZ):

    def __init__(self, p1, num1, num2, num3, var1, var2):
        super().__init__(num1, num2, num3, var1, var2)
        self.p1 = p1

    def addition(self):
        print("single variable :", self.p1)


    def subtraction(self, param1, param2):
        print("subtraction :", param1-param2)

    def subtraction(self, param1, param2, param3):
        print("subtraction with three vari:", (param1-param2)*param3)

# if __name__ == "__main__":
#     # obj = XYZ(num1=10, num2=20, num3=40, var1=50, var2=60)
#     # obj.addition()
#
#     obj = PQR(p1=100, num1=10, num2=20, num3=40, var1=50, var2=60)
#     obj.addition()
#     obj.multiplication()
#     obj.subtraction(500, 600)


# plus operator
var1 = 100
var2 = 500
print("addition :", var1 + var2 + 400)
print(dir(int))
print("addition :", var1.__add__(var2).__add__(400))

str1 = "Hello"
str2 = " Good Morning"
print(dir(str))
print("string msg :", str1+str2)
print("string msg :", str1.__add__(str2))

list1 = [4, 6, 8, 10]
list2 = [40, 50, 60]

print(list1 + list2)
print(list1.__add__(list2))


# multiplication operator
p1 = 60
p2 = 70
print("multiplication :", p1*p2)
print("multiplication :", p1.__mul__(p2))

v1 = "hello"
v2 = 2
print("string multiplication :", v1*v2)
print("string multiplication :", v1.__mul__(v2))

list1 = [5, 6, 7, 2]
num1 = 3

print("list multiplication :", num1*list1)
print("list multiplication :", list1.__mul__(num1))





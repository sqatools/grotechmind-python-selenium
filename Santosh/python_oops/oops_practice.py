# # class xyz:
# #     country="indial"   #class variable
# #     def __init__(self,a,b):  # constructor
# #         print("initialize the memory")
# #         self.val_a=a  # instance variable
# #         #print("val_a :",a)
# #         self.val_b=b  # instance variable
# #         #print("val_b :",b)
# #         self.val_c=50
# #         self.val_E=90
# #     # instance method / object method.
# #     def greeting(self,val1,val2):
# #         print("good morning")
# #         print("var 1:", val1)
# #         print("var 2:", val2)
# #         print("value of a:", self.val_a)
# #         print("value of b:", self.val_b)
# #         print("country name :", self.country)
# #     def show_city_name(self,city_name):
# #         print("city name :", city_name)
# #         print("c variable:",self.val_c)
# # obj=xyz(500,60)
# # obj.greeting(700,900)
# # c_name="Namded"
# # obj.show_city_name(c_name)
# #
#
# # class car:
# #     def __init__(self, car_name, car_company, car_price):
# #         self.car_name=car_name
# #         self.car_company=car_company
# #         #print("car_company :", car_company)
# #         self.car_price=car_price
# # #obj=car("nexon","Tata","98000")
# #     def show_car_name(self,car_name):
# #         print("car_name :",car_name)
# #
# # obj=car("Santro","suzuki","90000")
# # obj.show_car_name("Santro")
#
#
# class car:
#     def __init__(self, car_name, car_company, car_price):
#         self.car_name=car_name
#         self.car_company=car_company
#         #print("car_company :", car_company)
#         self.car_price=car_price
# #obj=car("nexon","Tata","98000")
#     def show_car_name(self):
#         print("car_name is :",self.car_name)
#     def show_car_comapny(self):
#         print("this is car company name :", self.car_company)
#
#     # @classmethod
#     # def show_car_country(cls,country):
#     #     print("Country name :", cls.country)
#
#     @staticmethod
#     def show_car_milege(milege):
#         print("Car milege :", milege)
#
#
# if __name__ == '__main__':
#      obj = car("Swift", "Maruti", "8 Lac")
#      obj.show_car_name()
#     # print(obj.__module__)   # __main__
#     # obj.show_car_country()
#      #car.show_car_country("kk","ll")
#      obj.show_car_milege(20)


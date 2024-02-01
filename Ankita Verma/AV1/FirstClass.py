class MyFirstClass():  #class name
  first_variable=10
  second_variable=1000000

first_object=MyFirstClass()
print(first_object) #printing hex
print(first_object.first_variable) #accessing attribute


second_object=MyFirstClass()
print(second_object)
print(second_object.second_variable)

print("-"*50)

class Atm():
      def sbi(self):
        print("SBI bank")

varobj=Atm()
print(varobj)
print(varobj.sbi())

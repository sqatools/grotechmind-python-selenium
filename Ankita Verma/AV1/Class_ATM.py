class Atm:
    #constructor
   def __init__(self):
    self.pin=""
    self.balance=0

    def menu(self):
     self.menu()

    def menu(self):
         user_input=("""Hello! HOw would you like to Processed
                   1.Enter 1 to create PIN
                   2.Enter 2 to create Deposite
                   3.Enter 3 to crete Withdrawal
                   4. Enter 4 to create Check Balance
                   5.Enter 5 to Exit""")
    if user_input==1:
      print("Create Pin")
    elif user_input==2:
      print("Create Deposite")
    elif user_input==3:
      print("Create Withdrawal")
    elif user_input==4:
      print("Check Balance")
    else:
        user_input==5:
        print("Bye")
 def create_pin(self):
     self.pin=input("Enetr Your Pin")
      Print("Pin Set Successfully")

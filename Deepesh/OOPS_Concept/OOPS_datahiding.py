"""
Data hiding : data hiding can be achieved by defining the method/variable with prefix as single
underscore ( _ ) and double underscore ( __ )
"""

class student:

    def __init__(self, name, address, email):
        self.name = name
        self._address = address
        self.__email = email

    def show_st_name(self):
        print("Student name is :", self.name)

    def _show_st_address(self):
        print("student address :", self._address)

    def __show_st_email(self):
        print("Student email address :", self.__email)


if __name__ == "__main__":
    obj = student("Mohit", "Mumbai", "mohit@gmail.com")
    # access single underscore prefix data
    obj._show_st_address()

    # access double underscore prefix data
    # obj._<classname>.__var/method
    obj._student__show_st_email()

    print(dir(obj))

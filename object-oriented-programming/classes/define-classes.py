class Student:
    def __init__(self, firstname, lastname, email="", grade=0, home_number=[], mobile_number=[]):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.grade = grade
        self.home_number = home_number
        self.mobile_number = mobile_number

    def return_name(self):
        return self.firstname + " " + self.lastname

    def print(self):
        print(self.return_name())

    def __str__(self):
        return "Name: " + self.return_name() + "\n" + "Email address: " + self.email + "\n" + "Home numbers: " + str(self.home_number).strip('[]') + "\n" + "Mobile numbers: " + str(self.mobile_number).strip('[]')
        ### nice format

jan = Student("Jan", "Spörer", "jan.spoerer@whu.edu", grade=1, home_number=["+492713178090"], mobile_number=["+491715395666", "asdfsadf"])
print(jan.firstname, jan.lastname)

jan.lastname = "Spörer-Theron"
print(jan.firstname, jan.lastname)

print(type(jan))

print(jan.return_name())

print(jan)

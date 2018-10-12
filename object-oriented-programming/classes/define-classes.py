class PhoneNumber:
    def __init__(self, number, number_type):
        self.number = number
        self.number_type = number_type

class Student:
    def __init__(self, firstname, lastname, email="", grade=0, numbers=[]):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.grade = grade
        self.numbers = numbers

    def add_number(self, number_instance):
        self.numbers.append(number_instance)

    def return_name(self):
        return self.firstname + " " + self.lastname

    def print(self):
        print(self.return_name())

    def __str__(self):
        result = "Name: " + self.return_name() + "\n" + "Email address: " + self.email + "\n"
        for value in self.numbers:
            result = result + value.number_type + ": " + value.number + "\n"
        result
        return result
        # return "Home numbers: " + str(self.home_number).strip('[]') + "\n" + "Mobile numbers: " + str(self.mobile_number).strip('[]')

jan = Student("Jan", "Spörer", "jan.spoerer@whu.edu", 1, [PhoneNumber("+491715395666", "Mobile")])
print(jan.firstname, jan.lastname)

jan.lastname = "Spörer-Theron"
print(jan.firstname, jan.lastname)

print(type(jan))

print(jan.return_name())

print(jan)

jan.add_number(PhoneNumber("1234", "German"))

print(jan)

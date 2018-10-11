class Student:
    def __init__(self, firstname, lastname, email="", grade=0, numbers={}):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.grade = grade
        self.numbers = numbers

    def return_name(self):
        return self.firstname + " " + self.lastname

    def print(self):
        print(self.return_name())

    def __str__(self):
        result = "Name: " + self.return_name() + "\n" + "Email address: " + self.email + "\n"
        for key, value in self.numbers.items():
            result = result + str(key) + ": " + str(value) + "\n"
        result
        return result
        # return "Home numbers: " + str(self.home_number).strip('[]') + "\n" + "Mobile numbers: " + str(self.mobile_number).strip('[]')

jan = Student("Jan", "Spörer", "jan.spoerer@whu.edu", grade=1, numbers={"Home number": "12345", "Mobile number": "+491715395666", "Fax": "+491839240"})
print(jan.firstname, jan.lastname)

jan.lastname = "Spörer-Theron"
print(jan.firstname, jan.lastname)

print(type(jan))

print(jan.return_name())

print(jan)

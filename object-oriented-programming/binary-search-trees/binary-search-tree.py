class Node:
    def __init__(self, name, age, child_left=None, child_right=None):
        self.name = name
        self.age = age
        self.child_left = child_left
        self.child_right = child_right

    def get_instance(self, name):
        if self.name == name:
            return self
        if self.name > name:
            if self.child_left is None:
                return self
            else:
                return self.child_left.get_instance(name)
        else:
            if self.child_right is None:
                return self
            else:
                return self.child_right.get_instance(name)

    def insert(self, child):
        if self.name == child.name:
            print("name already there, idiot")
        elif (self.name > child.name):
            if (self.child_left is None):
                self.child_left = child
                print("Successfully inserted", child.name, "into", self.name, " to the left.")
            else:
                self.child_left.insert(child)
        elif (self.name < child.name):
            if (self.child_right is None):
                self.child_right = child
                print("Successfully inserted", child.name, "into", self.name, " to the right.")
            else:
                self.child_right.insert(child)


head = Node("Jan", 1)
head.insert(Node("Ana", "Ana age"))
head.insert(Node("Johannes", "Johannes age"))
head.insert(Node("Zakariya", "Zaka age"))
head.insert(Node("Lenka", "Lenka age"))
head.insert(Node("Vahe", "Vahe age"))
head.insert(Node("Ruby", "Ruby age"))
# print(head.name)
# print(head.child_right.name)
# print(head.child_right.child_right.name)


print(head.get_instance("Johannes").age)
print(head.get_instance("Zakariya").age)
print(head.get_instance("Jan").age)
print(head.get_instance("Lenka").age)
print(head.get_instance("Vahe").age)
print(head.get_instance("Ruby").age)

class Node:
    def __init__(self, name, age, child_left=None, child_right=None):
        self.name = name
        self.age = age
        self.child_left = child_left
        self.child_right = child_right

    def get_instance(self, name):
        if self.name == name:
            return self
        if self.name < name:
            if self.child_left is None:

            else:
                return self.child_left.get_instance(name)

        else:
            return self.child_right.get_instance(name)

    def insert(self, child):
        if self.name == child.name:
            print("name already there, idiot")
        elif (self.name > child.name):
            if (self.child_left is None):
                self.child_left = child
                print("Successfully inserted", child.name, "into", self.name)
            else:
                self.child_left.insert(child)
        elif (self.name < child.name):
            if (self.child_right is None):
                self.child_right = child
                print("Successfully inserted", child.name, "into", self.name)
            else:
                self.child_right.insert(child)


head = Node("Jan", 1)
head.insert(Node("Ana", 2))
head.insert(Node("Johannes", 3))
head.insert(Node("Zakariya", 4))
head.insert(Node("Lenka", 5))
head.insert(Node("Vahe", 6))
head.insert(Node("Ruby", 7))
print(head.name)
print(head.child_right.name)
print(head.child_right.child_right.name)


head.get_instance("Johannes").age

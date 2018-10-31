import math

class Node:
    def __init__(self, name, age, child_left=None, child_right=None):
        self.name = name
        self.age = age
        self.child_left = child_left
        self.child_right = child_right

    def __ge__(self, other):
        return self.name >= other.name

    def __le__(self, other):
        return self.name <= other.name

    def __gt__(self, other):
        return self.name > other.name

    def __eq__(self, other):
        return self.name == other.name

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

    def tree_to_list(root, unsorted_list=[]):
        """
        The root node does not necessarily have to be the actual node.
        Subtrees can also be balanced by taking a root that is different from
        the actual root.
        """
        if root.child_left is not None:
            root.child_left.tree_to_list()
            unsorted_list.append(root.child_left)
        if root.child_right is not None:
            root.child_right.tree_to_list()
            unsorted_list.append(root.child_right)
        return unsorted_list

    def put_middle_to_front(sorted_sublist):
        print("Chalo")
        middle_element = sorted_sublist.pop(len(sorted_sublist) % 2)
        left = sorted_sublist[:len(sorted_sublist) % 2]
        right = sorted_sublist[len(sorted_sublist) % 2:]
        if left is None or len(left) < 2:
            left = Node.put_middle_to_front(left)
        else:
            left = []
        if right is None or len(right) < 2:
            right = Node.put_middle_to_front(right)
        else:
            right = []
        result = []
        result.append(middle_element)
        print("MIDDLE ELEMENT!!!!!!!!!!!!!!:", middle_element)
        print("LEFT ELEMENT!!!!!!!!!!!!!!:", left)
        print("RIGHT ELEMENT!!!!!!!!!!!!!!:", right)
        return result.extend(left).extend(right)

    def rebalance_tree(self):
        unsorted_list = self.tree_to_list()
        unsorted_list.sort() # unsorted_list is now sorted
        prepared_list = Node.put_middle_to_front(unsorted_list)
        tree = prepared_list.pop(0)
        for node in prepared_list:
            tree.insert(node)
        return tree

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

head.rebalance_tree()

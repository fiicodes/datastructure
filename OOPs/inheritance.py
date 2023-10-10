class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(self.id)
        print(self.name)

    def details(self):
        print("The id is {}".format(self.id))
        print("The name is {}".format(self.name))


class Employee(Person):
    def __init__(self, name, id, age):
        self.age = age

        Person.__init__(self, name, id)

    def display(self):
        print(self.age)
        return super().display()

    def details(self):
        print("The id is {}".format(self.id))
        print("The name is {}".format(self.name))
        print("The age is {}".format(self.age))


obj = Employee("fitha", 7, 25)
obj.details()
obj.display()

class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def __str__(self):
        return f"Hello {self.firstName} {self.lastName}. You are {self.age}"

    def getPersonInfo(self):
        return f"The person's information: {self.firstName} {self.lastName}, {self.age} years old"

    # Destructor method
    def __del__(self):
        print("This is the destructor")


class Employee(Person):
    def __init__(self, firstName, lastName, age, position):
        # Calling parent constructor
        super().__init__(firstName, lastName, age)
        self.position = position

    # Method override
    def getPersonInfo(self):
        return f"The person's information: {self.firstName} {self.lastName}, {self.age} years old and works as a {self.position}"


person1 = Person('Sergei', 'Sokolov', 40)
person2 = Employee('Sergei', 'Sokolov', 40, 'Senior Python Developer')

print(person2.getPersonInfo())

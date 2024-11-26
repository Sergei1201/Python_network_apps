class Person:
    # Constructor
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # Str Method
    def __str__(self):
        return f'Hello {self.first_name} {self.last_name}. You are {self.age}'

    # Get information about the object
    def get_info(self):
        return f'This is the information on the person: {self.first_name}; {self.last_name}; {self.age}'

    # Inheritance


class Employee(Person):
    # Constructor
    def __init__(self, first_name, last_name, age, position):
        super().__init__(first_name, last_name, age)
        self.position = position

    # Get information about employee
    def get_employee_info(self):
        return f'This is the information on the employee: {self.first_name}, {self.last_name}, {self.age} {self.position}'

# person1 = Person('Sergei', 'Sokolov', 40)
# print(person1.get_info())


employee1 = Employee('Daniil', 'Sokolov', 9, 'Student')
print(employee1.get_info())
print(employee1.get_employee_info())

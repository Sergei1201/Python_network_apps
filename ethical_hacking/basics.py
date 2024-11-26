class Person:
    # Constructor
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def __str__(self):
        return f'Hello {self.first_name} {self.last_name}. You are {self.age} years old'
    

# Inheritance
class Employee(Person):
    #Constructor
    def __init__(self, first_name, last_name, age, position):
        # Calling the parent constructor
        super().__init__(first_name, last_name, age)
        self.position = position
    
    # Definition
    def say_hello(self):
        return f'Hello {self.first_name} {self.last_name}. You are {self. age} and have a position of a {self.position}'


person = Person('Sergei', 'Sokolov', 40)
print(person)

employee1 = Employee('Sergei', 'Sokolov,', 40, 'Senior Developer')
print(employee1.say_hello())

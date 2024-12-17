# Basics of OOP in Python
class Person:
    # Constructor
    def __init__(self, first_name, last_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    # Magic methods

    # String representation of an object
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    # Comparing two objects
    def __eq__(self, other) -> bool:
        return self.age == other.age

    # Public methods
    def greetings(self) -> str:
        return f"Greetings to you {self.first_name} {self.last_name}"



# Main function
if __name__ == "__main__":
    p1 = Person("John", "Doe", 35)
    p2 = Person("Jane", "Doe", 25)
    print(p1 ==  p2)


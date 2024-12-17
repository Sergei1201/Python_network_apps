# Adding dynamic attributes to a class in Python
class Person:
    pass


# Main function
if __name__ == "__main__":
    # Create a dictionary for adding attributes dynamically to a class

    p1 = Person();
    person1 = {
            "first_name" : "John",
            "last_name" : "Doe",
            "age" : 35
            }
    for key, value in person1:
        setattr(p1, key, value)




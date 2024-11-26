# Passing a function as an argument to an object
def multiply(x, y):
    return x * y

class Test:
    # Constructor
    def __init__(self, myltiply_func):
        self.myltiply_func = myltiply_func

    # Str method
    def __str__(self):
        return f'This is the test function'
    
test = Test(multiply(4,6))
print(test)
print(test.myltiply_func)


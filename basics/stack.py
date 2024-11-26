'''
1. Create an empty stack
2. Check if the stack is empty
3. Push an element onto the stack
4. Remove an element from the stack
'''

# Create an empty stack


def createStack():
    stack = []
    return stack

# Check if the stack if empty


def stackIsEmpty(stack):
    return len(stack) == 0

# Push an element onto the stack


def pushElement(stack, element):
    stack.append(element)
    return element

# Remove an element from the stack


def popElement(stack):
    if stackIsEmpty(stack):
        return "Stack is empty"
    return stack.pop()


stack = createStack()
pushElement(stack, 1)
pushElement(stack, 2)
pushElement(stack, 3)
pushElement(stack, 4)
pushElement(stack, 5)
print(stack)

print(popElement(stack))
print(stack)
print(popElement(stack))
print(stack)
print(popElement(stack))
print(stack)
print(popElement(stack))
print(stack)
print(popElement(stack))
print(stack)
print(popElement(stack))

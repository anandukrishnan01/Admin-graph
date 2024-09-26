class Example:
    def _init_(self, value):
        self.__value = value  # Private attribute

    def get_value(self):
        return self.__value  # Public method to access the private attribute

    def set_value(self, value):
        self.__value = value  # Public method to modify the private attribute

# Create an Example object
obj = Example(42)

# Accessing private attribute directly (will raise an AttributeError)
# print(obj.__value)

# Using public methods to access and modify the private attribute
print(obj.get_value())  # Output: 42

obj.set_value(99)
print(obj.get_value()) 




class Example:
    def __init__(self, value):
        self.__value = value  # Private attribute

    def get_value(self):
        return self.__value  # Public method to access the private attribute

    def set_value(self, value):
        self.__value = value  # Public method to modify the private attribute

# Create an Example object
obj = Example(42)

# Accessing private attribute directly (will raise an AttributeError)
# print(obj.__value)

# Using public methods to access and modify the private attribute
print(obj.get_value())  # Output: 42

obj.set_value(99)
print(obj.get_value())  # Output: 99

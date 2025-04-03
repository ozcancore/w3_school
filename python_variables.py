x = 5
y = 2
print(x + y)  # Addition: 7
print(x - y)  # Subtraction: 3
print(x * y)  # Multiplication: 10
print(x / y)  # Division: 2.5

x = 3.14  # A float
print(type(x))  # Output: <class 'float'>


x = "Hello Piotr"  # A string
print(type(x))  # Output: <class 'str'>

x = "Hello"
y = "World"

# Concatenation (combining strings)
print(x + " " + y)  # Output: Hello World

# Repeating a string
print(x * 3)  # Output: HelloHelloHello


x = True
y = False

# Logical operations
print(x and y)  # Output: False
print(x or y)   # Output: True
print(not x)    # Output: False

x = [1, 2, 3, "apple", 3.14]  # A list
print(type(x))  # Output: <class 'list'>


x = (1, 2, 3, "apple", 3.14)

# Accessing elements
print(x[2])  # Output: 3

# Tuples are immutable, so you cannot change their elements
# x[0] = 10  # This would result in an error

x = {"name": "John", "age": 30, "city": "New York"}

# Accessing a value by key
print(x["name"])  # Output: John

# Adding a new key-value pair
x["job"] = "Engineer"
print(x)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'job': 'Engineer'}

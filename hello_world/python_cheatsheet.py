# Feel Free to add your on print statemenets
a, b = 10, 2
# == Equals
a == b

# != Not Equal
a != b

# < Less than
a < b

# > Greater than
a > b

# <= Less than or Equal to
a <= b

# >= Greater than or Equal to
a >= b

# print(), This function looks for the default output device, your terminal, and displays the value passed to it.
print("Hello")

# input(), This function looks for the default input device, your keyboard,
#  and captures the value. This value can then be assigned or used.
print("Where do you live?")
location = input()
print("So you live in " + location)

# len(), This function returns the length or the count of the elements contained within
# the structure it is applied on. This may be a string, array, list, tuple, dictionary or any sequence.
len("Hello")

# str(), This function can be used to convert the provided value into a String
str(55)

# int(), This function can be used to convert the provided value into an int
int('75')

# float(), This function can be used to convert the provided value into a float
some_int = 10
float(some_int)

# Creating Functions Functions in Python require a keyword to define them
#  : def   followed by an identifier (a name) this forms the function signature.
# The body of the function contains the code to run when the function is called.


def say_hello():
    return "Hello there!"

# With parameters


def say_hello(you):
    return "Hello " + you

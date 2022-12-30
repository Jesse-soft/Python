# functions are set of instructions that take an input and returns an outputs.

# def <function name> (<params>):
#     <task to complete>

def sum(x, y):
    return x+y


currentYear = input("current year ")
age = input("age ")
currentYear = int(currentYear)
age = int(age)


def calDateOfBirth(Year, yage):
    return (Year-yage)


print(calDateOfBirth(currentYear, age))

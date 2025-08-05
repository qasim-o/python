# Typecasting = The process of converting a variable from one data type to another
#              str(), int(), float(), bool()

name = "Alpha"
age = 25
GPA = 3.3
is_student = True

# Using the type function to find the type of variable
print(type(is_student))
print(type(name))
print(type(age))
print(type(GPA))

# Now we are going to convert one data type to another

# Convert GPA to integer currently it is a float
GPA = int(GPA)
print(GPA)

# Let's convert age to a floating point number
age = float(age)
print(age)

# convert age to a string
age = str(age)
print(type(age))        # To check the type of variable use the type function

# Now we will convert name to boolean
name = bool(name)
print(name)     # The output is true because there is no empty value
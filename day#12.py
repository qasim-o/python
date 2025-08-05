# Conditional expression = A one-line shortcut for the if-else statement  (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else y

num = 5
print("Positive" if num > 0 else "Negative")

# To Check Old or Even Numbers

value = int(input("Enter the Value to Check Even or Odd: "))

result = "EVEN" if value % 2 == 0 else "ODD"
print(result)

# Another Example of Comparing to numbers

a = 7
b = 9
max_num = a if a > b else b
min_num = a if a < b else b

# One more Example of Age

age = 25

status = "Adult" if age > 18 else "Child"

# For Temperature

temperature = 30

weather = "HOT" if temperature >= 20 else "COLD"
print(weather)

# One more Example

user_role = "admin"
access_level = "Full access" if user_role == "admin" else "Limited Access"
print(access_level)
# Variable = A container for a value (string, integer, float, boolean)
# A variable behaves as if it was the value it contains

# These are string
fist_name = "Alpha"
food = "banana"
email = "alpha@fake.com"

print(f"Hello {fist_name}")
print(f"I like {food}")
print(f"Your email is:  {email}")

# These are Integers
age = 25
quantity = 6
num_of_students = 31

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

# Float
price = 49.99
GPA = 3.3
distance = 5.6

print(f"The price is ${price}")
print(f"Your GPA is: {GPA}")
print(f"You ran {distance}km")

 # Boolean

is_student = False

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")

for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT available")

is_online = True

if is_online:
    print("You are online")
else:
    print("You are offline")
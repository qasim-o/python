# if = Do some code only IF some condition is True
#   Else do something else

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Let's do some other Examples

age_1 = int(input("Enter your age: "))

if age_1 > 100:
    print("You are too old to sign up")
elif age_1 >= 18:

    print("You are now signed up!")
elif age_1 <= 0:    # We can check more conditions before reaching to else statement for this we can use elif statement

    print("You haven't been born yet!")

else:
    print("you must be 18+ to sign up.")

# Let's do some another example
# Ask from the user would like some food

response = input("Would you like some food? (Yes/No): ")

if response == "Yes":
    print("Have some food!")
else:
    print("No food for you!")

# Here is other example user type their name
name = input("Enter your name: ")

if name == "":
    print("You didn't type in your name! ")
else:
    print(f"Hello {name}!")

# One important thing that you should know is the boolean with if statement
# Now another example using boolean expression

for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")

# Another example using boolean

online = False

if online:
    print("The user is online")
else:
    print("The user is offline")


scours = float(input("Enter your scour here: "))
if scours >= 90:
    print("Your grade is A")
elif scours >= 75:
    print("Your grade is B")
elif scours >= 50:
    print("Your grade is C")
else:
    print("You are fail")
# while loop = execute some WHILE some condition remains true

name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")

print(f"hello {name}")

# Here is another example of while loop
age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter Your age: "))

print(f"You are {age} years old")

# Going for one more example.
food = input("Enter a food you like (q to quite): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print("byee")

# Last example about while loop
num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num >10:
    print(f"{num} is not valid")
    num = int(input("Enter a number 1 - 10: "))

print(f"Your number is {num}")
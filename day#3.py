# input() = A function that prompts the user to enter data
#      Returns the entered data as a string

name = input("What is your name?")
age = int(input("How old are you?"))

age = age + 1

print(f"Hello {name}")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old")

# Exercise 1: Find the Area of a Rectangle

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width

print(f"The area of length {length} and width {width} is: {area}cm")

# Exercise 2: Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} X {item}/s")
print(f"Your total is: ${total}")

# Addtion, subractoion, multiplication, and Division of Two numbers

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

sum = num1 + num2
difference = num1 - num2
Product = num1 * num2
Quotient = num1 / num2

print("The Sum of ",num1, "and", num2,"is",sum)
print("The Difference between ",num1, "and", num2,"is",difference)
print("The Product of ",num1, "and", num2,"is",Product)
print("The Quotient of ",num1, "and", num2,"is",Quotient) 
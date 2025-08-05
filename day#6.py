# How to calculate the cercumference of the circle
import math    # import the math module

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")   # we can use the round function

# How to find the area of a circle
import math

radius1 = float(input("Enter the radius of a Circle: "))

area = math.pi * pow(radius1, 2)
print(f"The area of a Circle is {round(area, 2)}cm^2")

# How to the long side of the right angle triangle
import math

a = float(input("Enter the side A: "))
b = float(input("Enter the side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The Side C = {c}")

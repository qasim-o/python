# python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "kgs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not valid")


# Let's try it with different a way

print("1. Kg to Pounds: ")
print("2. Pounds to Kg: ")

choice = (input("Choose an option: "))

if choice == "1":
    kg = float(input("Enter weight in Kg: "))
    pounds = kg * 2.20462
    print(f"{kg} kg = {pounds} pounds")
elif choice == "2":
    pounds = float(input("Enter weight in pounds: "))
    kg = pounds / 2.20462
    print(f"{pounds} pounds = {kg} kg")



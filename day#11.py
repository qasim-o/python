# Logical Operators = evaluate multiple conditions (or, and, not)
#           or = at least one condition must be True
#           and = both conditions must be True
#           not = inverts the condition (not False, not True)

# The example of (or)
temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled.")

# Now let's cover the (and) condition by an example

tempt = 30
is_suny = True

if tempt >= 29 and is_suny:
    print("It is HOT outside ")
    print("It is SUNNY ")
elif tempt <=0 and is_suny:
    print("It is COLD outside ")
    print("It is SUNNY")
elif 28 > tempt > 0 and is_suny:
    print("It is WARM outside ")
    print("It is SUNNY ")

elif tempt >= 29 and not is_suny:
    print("It is HOT outside ")
    print("It is CLOUDY ")
elif tempt <=0 and not is_suny:
    print("It is COLD outside ")
    print("It is CLOUDY")
elif 28 > tempt > 0 and not is_suny:
    print("It is WARM outside ")
    print("It is CLOUDY ")


# for loops = Execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

# Suppose we need to count to 10
for x in range(1, 11):
    print(x)

# We want to wish HAPPY NEW YEAR!
for counter in reversed(range(1, 11)):      # To Count back word we use the reversed function
    print(counter)
print("HAPPY NEW YEAR!")

# Go for another example for explanation
for i in range(1, 21, 2):   # In the braces 1st number is for starting 2nd for ending which is exclusive and 3rd is to separate it.
    print(i)

# Now it can use it over string
credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)

# Now count to 20, but we want to skip some numbers

for count in range(1, 21):
    if count == 13:
        continue        # continue key word is used for to skip some number
                        # if you use break keyword than you out of this loop entirely.
    else:
        print(count)

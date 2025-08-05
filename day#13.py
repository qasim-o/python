# Today we will cover the other types of string
from ctypes import HRESULT

name = input("Enter your full name: ")
#result = len(name)
#result = name.find("h")     # Finds the first position of the entered letter
#result = name.rfind("h")     # rfinds is used for the last occurrences of the letter or word
                            # If there is no word found the result will be (-1)
#name = name.capitalize()    # Capitalize the first letter of the name
#name = name.upper()         # Convert the name to upper case
#name = name.lower()         # Convert the name to lower case
#result = name.isdigit()     # Used for to check digits and the result will boolean
#name = name.isalpha()     # Used for to check alphabets and the result will be boolean (if the name contain spaces the result will still false)

print(name)

# To find the dashes in the phone number using count.
phone_number = input("Enter your phone number #:")
#result = phone_number.count("-")    # count is used for to count something
rephone_number = phone_number.replace("-", " ")

print(rephone_number)

# if you a comprehensive list about strings methods available to you, You can use the "print(help(str))"

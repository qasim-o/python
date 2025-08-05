# indexing = accessing elements of a sequence using [] (indexing operator)
#               [start : end : step]
credit_number = "1234-5678-9012-3456"

#print(credit_number[3])
#print(credit_number[:4])
#print(credit_number[5:9])
#print(credit_number[5:])
#print(credit_number[-1])       # You can use negative indexing as will and will from the end side


# Now lets cover the steps in indexing
#print(credit_number[::3])       # the first : is used for starting and second : is used for ending and 3 is used for steps

# OK! Here is a practical example to Get the last four digits of Credit Card Number
last_digits = credit_number[-4:]
print(f"Last Digits of your Credit Card Number is XXXX-XXXX-XXXX-{last_digits}")

# if you want to reverse your credit number type this last_digits = credit_number[::-1]
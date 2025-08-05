# format specifiers = {value:flags} format a value based on what
#                           flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

# .(number)f = round to that many decimal places (fixed point)
#price1 = 3.14356
#price2 = -945.34
#price3 = 45.32

#print(f"Price 1 is ${price1:.2f}")
#print(f"Price 2 is ${price2:.2f}")
#print(f"Price 3 is ${price3:.2f}")

# :(number) = allocate that many spaces
#price1 = 3.14356
#price2 = -945.34
#price3 = 45.32

#print(f"Price 1 is ${price1:10}")     #if you want 0 zero instead of space write 0 after 10
#print(f"Price 2 is ${price2:10}")
#print(f"Price 3 is ${price3:10}")

# :< = left justify
#price1 = 3.14356
#price2 = -945.34
#price3 = 45.32

#print(f"Price 1 is ${price1:<10}")
#print(f"Price 2 is ${price2:<10}")
#print(f"Price 3 is ${price3:<10}")

# :> = right justify
#price1 = 3.14356
#price2 = -945.34
#price3 = 45.32

#print(f"Price 1 is ${price1:>10}")
#print(f"Price 2 is ${price2:>10}")
#print(f"Price 3 is ${price3:>10}")

# :^ = center align
#price1 = 3.14356
#price2 = -945.34
#price3 = 45.32

#print(f"Price 1 is ${price1:^10}")
#print(f"Price 2 is ${price2:^10}")
#print(f"Price 3 is ${price3:^10}")

# :+ = use a plus sign to indicate positive value (If you have some positive numbers and you like to display the + sign.)
#price1 = 3.14356
#price2 = -945.34
#price3 = 45.32

#print(f"Price 1 is ${price1:+}")
#print(f"Price 2 is ${price2:+}")
#print(f"Price 3 is ${price3:+}")

# :, = comma separator   (Used for large values to separate it by ,)
#price1 = 31325.14356
#price2 = -945246.34
#price3 = 452579.32

#print(f"Price 1 is ${price1:+,.2f}")
#print(f"Price 2 is ${price2:+,.2f}")
#print(f"Price 3 is ${price3:+,.2f}")
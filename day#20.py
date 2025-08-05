# Count down timer program in python
# You can use a sleep function of a time module
import time    # To import time module

my_time = int(input("Enter the time in seconds: "))    # Input from the user

for x in (range (my_time, 0, -1)):   #Another technique for reversed function is reversed(range(my_time, 0)):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")


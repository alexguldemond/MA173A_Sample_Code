#!/usr/bin/python3

# Floating point numbers are decimals stored with a finite number of digits
a = 1.0
b = 2.3

# We can do all the normal stuff witht ehm
print(a + b)
print(a - b)
print(a * b)
print(b - a)
print(a**b)

# You may have noticed that some of these gave weird answers. THis is due to roundoff error, and has to do with the fact that 
# decimals are stored in base 2.
#!/usr/bin/python3

# OFten times we do not know how many times to loop a block of code.
# In this case we use a while loop

data = 0
while(data < 10):
    print(f"Data = {data}")
    data = data + 1

# Just like in for loops, we can use break or continue to leave early or skip an iteration

# Be carefult, while loops can loop infinitely if a mistake is made
# The following would loop forever
# while(data > -1):
#    print(f"Data = {data})
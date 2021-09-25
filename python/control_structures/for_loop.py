#!/usr/bin/python3

# Often times we need to repeat a section of code. One way to do this is with for loops

# Say we want to repeat something 5 times
for _ in range(0, 5):
    print("Hello")

# We may also wish to use the loop index
for i in range(0,5):
    print(f"Hello: {i}")

# The the first argument for range is the starting value
# The second is the final value, and is not included
# An optional thir argument specifies an increment
for i in range(0, 10, 2):
    print(f"Hello: {i}")

# We can interate over lists as well
list = ["a", "b", "c", "d"]
for letter in list:
    print(letter)

# Sometimes we may want to exit a loop early when some unknown condition is met
for i in range(0, 10):
    print(f"Hello: {i}")
    if (i >= 5):
        print("Leaving loop early...")
        break

# We may also sometime wish to skip over some iterations. For this we use the continue statement
for i in range(0, 10):
    if ( i == 2 or i == 8):
        print("Skipping this number")
        continue
    print(f"Hello: {i}")

# In this class, one thing you may need to do is iterate over a matrix
# In this case anested loop can be useful
for i in range(0, 4):
    for j in range(0, 3):
        print(f"Index: ({i},{j})")
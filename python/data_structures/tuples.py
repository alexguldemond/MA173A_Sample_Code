#!/usr/bin/python3

# Tuples are like lists, but they are immutable, i.e. cannot be changed

tup = (1, 2, "Hello")

# We can index them like lists
print(tup[1])

# But we cannot change them
# tup[0] = 3
# The above will error out

# Tuples can also be easily unpacked. This can be useful for getting several values out at once
(one, two, hello) = tup
print(one)
print(two)
print(hello)

#Tuples arecommonly used for returning multiple values from a function
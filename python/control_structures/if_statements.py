#!/usr/bin/python3

# Often times we need to execute code given a certain condition. This is how we do this:

data1 = 10

if (data1 > 5):
    print("This will be printed")

# Sometimes we need to execute some code if the condition is false

if (data1 < 5):
    print("This will not be printed")
else:
    print("This will be printed")

# Sometimes we need to check for many conditions
if (data1 < 3):
    print("This will not be printed")
elif ( data1 > 5):
    print("This will be printed")
else:
    print("This will not be printed")

# Note that only the fist true block gets printed, even if subsequent blocks evaluate to true

if (data1 > 11):
    print("This won't be printed")
elif (data1 > 9):
    print("This will be printed")
elif(data1 > 3):
    print("Even though this is true, it won't get printed")

# We can also test multiple things at once
data2 = -10

if (data1 >= 10 and data2 <= -10):
    print("Both are true")

if (data1 > 9 or data2 > 9):
    print("Inclusive or becomes true if one or both are true")

# To check for equality, we use == instead of =
if (data1 == -data2):
    print("This will be printed")

# To check for inequality, we use !=
if (data1 != data2):
    print("This will be printed")

# For greater than or equal, we use >=, and less than or equal, we use <=    
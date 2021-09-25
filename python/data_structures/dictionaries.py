#!/usr/bin/python3

# Dictionaries are data structures consisting of key value pairs. They are useful for organizing
# data when putting them in a list doesn't make sense

dictionary = {'a' : 1.0, 'b' : 2.0, 'c' : 3.0}

# Dictionary keys and values can be any types
d2 = {'a' : "Hello", 1 : [1, 2], -3.0 : ("a", "b")}

# To get a value out of a dictionary, we simply do
print(dictionary['a'])

# If a certain value doesn't exist, we get an error
# print(dictionary['d'])

# We can add akey value pair like
dictionary['d'] = 4.0
print(dictionary['d'])

# There are a few ways to iterate over dictionaries

# By key
for key in dictionary.keys():
    print(f"{key} : {dictionary[key]}")

# Or if we don't care about the keys,we can simply
for val in dictionary.values():
    print(val)

# Or we can also iterate by key value pairs
for (key, val) in dictionary.items():
    print(f"{key} : {val}")

# Similar to lists, we can use dictionary comprehensions to create new dictionaries
d3 = { key + key : val**2 for (key, value) in dictionary.items()}
print(d3)
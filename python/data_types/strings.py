#!/usr/bin/python3

# One of the most useful data types are strings. They are simply sequences of characters.

string1 = "Hello World"

# We can index strings
char0 = string1[0]
print(f"THe first character is {char0}")

# We can concatenate
string2 = ", Goodbye World"
print(string1 + string2)

# We can repeat
print(string1*3)

# We can split strings up to make parsing easier
list = string1.split(" ")
print(list)

# We can join strings usinga specific delimiter
print(", ".join(list))

# We can do mass replacements
print(string1.replace("Hello", "Goodbye"))

# Note that in python, there is no difference between single and double quotes

# If we need special characters, we use escape sequences. For instance, for a new line, we do
print("Hello\nWorld")

# Or a tab
print("Hello\tWorld")

# If we need \, we escape it
print("Hello \\ World")

# If we wish to print plain text, we use the r prefic
print(r"\t\n\t")

# We can also do multiline strings with tripple quotes
string = """This is
a multiline
string"""
print(string)
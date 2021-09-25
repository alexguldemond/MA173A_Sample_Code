#!/usr/bin/python3

# Sometimes you want to print data without worrying about building strings.
# Formatted printing makes this convenient

datum1 = 1.1
datum2 = 1.2
datum3 = 1.3

# Note the prefix f, and the use of curly braces inside the string
print(f"Here is some data: {datum1}, {datum2}, {datum3}")
# Should print the following:
# Here is some data: 1.1, 1.2, 1.3
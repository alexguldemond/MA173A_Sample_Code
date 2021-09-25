#!/usr/bin/python3

# Sometimes we need to read files. Here I will show two different ways to read a file

file1 = "file1.txt"
file2 = "file2.txt"

# First, we need to open the file. We use the open function for this.
# The second argument r means the we are just reading
f = open(file1, 'r')

# This will read the entire file, and store the data in text1
text1 = f.read()

print(text1)

# Always remember to close the file
f.close()

# Having to remember to call close can be tedious and error prone, especially when your code has multiple exit points.
# instead, we can use the with keyword. This is the preferred method.

with open(file2, 'r') as f:
    text2 = f.read()
    print(text2)

# Outside the scope of the with block, variable f shoud be closed
if (f.closed):
    print("f is closed")
else:
    print("f is still open")
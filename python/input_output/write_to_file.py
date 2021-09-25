#!/usr/bin/python3

# Sometimes the output of some computation is too large to print to screen.
# Instead, we can write it to disk for later

# The 'w' argument opens a file for writing. If the file already exists, this will overwrite it.
with open("file3.txt", "w") as f:
    f.write("This is how we write to a file\n")
    f.write("Let's write some more\n")

print("File written")

# If we wish to append, we use the "a" argument
with open("file3.txt", "a") as f:
    f.write("One more line.\n")

# When writing, you MUST either use a with block, or call the close method.
# If you do not, there is no guarantee that you will actually write to the file.
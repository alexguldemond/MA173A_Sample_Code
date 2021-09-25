#!/usr/bin/python3

# It is cumbersome to put too much into one file. I have put a simple function in testModule.py
# and now I wish to use it here. I need to import it

from testModule import double

# Python hasmany built in modules 

# To distinguish a module from an executable file, we use this if statement
# for executable code. This block only runs if this file was executed
if (__name__ == "__main__"):
    print(double(4))
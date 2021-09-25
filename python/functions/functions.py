#!/usr/bin/python3

# We commonly need to put code into functions for ease of reuse.
# Here are some exmples

# No input or output
def printHello():
    print("Hello World")

# We can call it with
printHello()

# To specify input arguments, we do
def greet(name):
    print(f"Hello {name}")

# And call it with
greet("Bob")

# For output, we use the return keyword.
# Anything after the word return is not executed
def square(n):
    return n*n

fourSquared = square(4)
print(fourSquared)

# We can specify the return in mutiple places
def bigOrSmall(n):
    if (n > 1000):
        return "This number is big!"
    else:
        return "This number is small!"

message = bigOrSmall(20)
print(message)

# We can call functions from other functions
def greetBob(name):
    if (name == "Bob"):
        greet(name)
    else:
        print("Do I know you?")

greetBob("Bob")
greetBob("Tom")


# We can also call functions from itself.
# This is called recursion
def naiveFibonacci(n):
    if (n == 0):
        return 0
    elif(n == 1):
        return 1
    return naiveFibonacci(n-1) + naiveFibonacci(n-2)

print(naiveFibonacci(7))

# Be careful with recusion. If a function calls itself too many times, you can get
# whats called a stack overflow.
# naiveFibonacci(1000) will crash the program

# Notice that any funtion can be called with any type
# I could do 
# naiveFibonacci("Hello")
# but it would fail
# We can use type annotations to help with this
def typesafeNaiveFibonacci(n : int):
    if (n == 0):
        return 0
    elif(n == 1):
        return 1
    return typesafeNaiveFibonacci(n-1) + typesafeNaiveFibonacci(n-2)

#!/usr/bin/python3

# Integers are exactly what they sound like

a = 2
b = 3

# We can add, subtract, and multiply them to get more integers
print(a+b)
print(a-b)
print(a*b)

# We can confirm that these are in fact integers
print(type(a))

# We can also divide them
print(a/b)

# Unlike most programming languages, when you divide two integers in python you are doing regular division, not integer division.
# The closest equivalent is the floor division operator, which is the same as integer division for positive integers.
# Floor division simply rounds down.
print(f" a // b = {a // b}")
print(f" b // a = {b // a}")

print(f"-3 // 2 = {-3 // 2}")

# We can also use the modulus operator. This will give us the remainder of integer division
print(f"b modulo a = {b % a}")

# We can also exponentiate with **. Note that the ^ operator is not exponentiation.
print(f"a**b = {a**b}")
print(f"a^b = {a^b}")

# Unlike languages like C, C++, Fortran, and Java, python3 does not have a maximum integer size
# If your integer exceeds a certain size, it is seemlessly converted to a BigInteger.
# Be warned, BigIntegers are much much slower to work with
print(type(10**10))
print(type(10**1000000))
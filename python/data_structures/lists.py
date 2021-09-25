#!/usr/bin/python3

# Lists are variably sized collections of data
list1 = [1, 4, 2, 6, 8]
print(list1)

# We can pull individual values out of lists by indexing them.
# Note that list indices start at 0
print(list1[0])

# Lists are mutable, so we can do
list1[2] = 3

# We can also get the size of lists
print(len(list1))

# And we can append
list2 = list1.append(7)
print(list1)

# Note that lists do not need to all be the same type
list3 = ["a", 1.0, "b", 4]
print([type(item) for item in list3])

# The above syntax is called a list comprehension, and is a very clean we to build lists from other lists
# Say we wanted to double every item in list 1. With loops it would be
newList = []
for i in list1:
    newList.append(i*2)
print(newList)

# The same can be achieved with a list comprehension
newList = [i*2 for i in list1]
print(newList)

# We can also do list comprehensions conditionally
evens = [i for i in list1 if i % 2 == 0]
print(evens)

#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


class MyString(str):
    def __str__(self):
        return self[::-1]  # so we just created a class called my string.
    # recall that when we slice the string above, we are stepping by -1. This means that we are essentially
    # going to print the string backwards.


print('Hello World.'.upper())  # it is important that a string is immutable. Each time we format a string
# creates a new object
print('Hello World.'.lower())
print('Hello World.'.casefold())
print('Hello, World.'.swapcase())
print('Hello, World. {}'.format(42 * 7))  # Recall that the curly brackets are placeholders
s = MyString('Hello World.')
print(s)
# recall that we can use format to enter variables in a string.

x = 3200
y = 75
print(f'My variables are {x} and {y}')
# the same can also be achieved by having the format outside the string.
print('My variables are {} and {}'.format(x, y))

# say you have a large number in the thousands and would like to add a comma to help identify.
print('Large value {:,}'.format(x * y))
print(f'the number is {x:,}')  # this is the shortcut way


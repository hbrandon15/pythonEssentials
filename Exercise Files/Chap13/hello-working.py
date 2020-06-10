#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = 'Hello, World.'
print(repr(s))  # repr will print the best string representation of an object.


class Bunny:
    def __init__(self, n):
        self._n = n

    def __repr__(self):
        return f'repr: the number of bunnies is {self._n}'

    def __str__(self):
        return f'str: the number of bunnies is {self._n}'


x = Bunny(47)
print(x)  # this uses the str
print(ascii(x))  # this uses the repr

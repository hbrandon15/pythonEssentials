#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = [1, 2, 3, 4, 5]  # This is a list. A list is mutable meaning the values can be changed.
y = (1, 2, 3, 4, 5)  # This is a tuple which is immutable meaning the values can not be changed.
# It can be said that a tuple should be favored.

for i in x:
    print('i is {}'.format(i))

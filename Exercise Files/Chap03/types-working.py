#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#  x = 'seven'  # single quotes and double quotes can be used.
# it is best practice to use single for the newer versions of Python
x = 'seven {} {}'. format(8, 9)  # you can use curly brackets as placeholders for other values.
# say you want to format the output to read seven, 9, 8 without moving the numbers?
y = 'seven {1} {0}'.format(8, 9)
print('x is {}'.format(x))
print('y is {}'.format(y))
print(type(x))

# you can also displace the output by editing values inside the curly brackets
z = 'seven {1:<9} {0:>9}'.format(8, 9)  # We left aligned the first placeholder and right aligned the second
print('z is {}'.format(z))

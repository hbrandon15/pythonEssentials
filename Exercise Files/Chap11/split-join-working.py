#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = 'This is a long string with a bunch of words in it.'
print(s.split())  # split will separate all words into a list.
# we can split and join strings as well.
l = s.split()
s2 = ' -- '.join(l)  # this statement will join the split words together with any character you choose.
print(s2)

#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def main():
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    print(game[1])  # This will just print paper. That is because we count starting from 0.
    # We can use the slice method to pull a selection of elements.
    # The first slice is that starting point and the second number followed by the :
    # is the end but NOT INCLUSIVE
    print(game[1:3])  # This wil print paper since it is at element one, we will print scissors as well
    # since it is element 2. We will stop and NOT include Lizard which is at element 3.
    # Slicing can also have steps added to the arguments. This is similar to range formatting.
    print(game[1:5:2])  # This will start at element 1 and end at element 5; however, we are moving by 2 elements.
    print_list(game)


def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()


if __name__ == '__main__': main()

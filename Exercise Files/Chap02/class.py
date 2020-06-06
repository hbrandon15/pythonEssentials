#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    # You can also use variables within a class.

    sound = 'Quackkkk!'
    walking = 'Walks like a duck.'

    def quack(self):  # Note that the first argument for a method inside a class
        # is always self
        # print('Quaaack!')
        print(self.sound)  # This does the same thing compared to
        # actually printing the sound from the print statement.

    def walk(self):
        print('Walks like a duck.')


def main():
    donald = Duck()
    donald.quack()
    donald.walk()


if __name__ == '__main__': main()

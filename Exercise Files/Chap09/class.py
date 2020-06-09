#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


class Duck:
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

    def quack(self):  # Self is the traditional argument for all modules created in a class
        print(self.sound)

    def move(self):
        print(self.movement)


def main():
    donald = Duck()
    donald.quack()
    donald.move()


if __name__ == '__main__':
    main()

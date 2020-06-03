#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
# This is functional the same as hello-version.py
import platform


def main():
    message()


def message():
    print('This is python version {}'.format(platform.python_version()))
    fox = 'hi'
    x = ['string', 5, fox, True]


if __name__ == '__main__':
    main()  # this causes the interpreter to read the entire script before executing
    print('I am from main')


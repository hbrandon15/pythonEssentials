#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def main():
    f = open('lines.txt')  # this returns a file object
    # The open function opens the file in read only mode.
    # you can add multiple parameters to open in read, write, etc. modes
    for line in f:
        print(line.rstrip())  # rstrip removes any whitespace


if __name__ == '__main__':
    main()

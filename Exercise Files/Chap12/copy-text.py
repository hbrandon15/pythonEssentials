#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('lines.txt', 'rt')  # we are opening the file in read mode and text mode
    outfile = open('lines-copy.txt', 'wt')
    for line in infile:
        print(line.rstrip(), file=outfile)
        print('.', end='', flush=True)  # the end parameter makes the interpreter refrain from entering a new line
        # instead it will end with a space
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()

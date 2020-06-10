#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def main():
    infile = open('berlin.jpg', 'rb')  # the rb identifies as a read only and a binary type of file
    outfile = open('berlin-copy.jpg', 'wb')  # the outfile is opened as write
    while True:
        buf = infile.read(10240)  # this is a buffer size and can vary for many operating systems.
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break
    outfile.close()
    print('\ndone.')


if __name__ == '__main__':
    main()

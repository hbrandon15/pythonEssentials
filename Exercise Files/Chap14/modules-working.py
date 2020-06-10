#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import os
import sys


def main():
    v = sys.version_info
    z = sys.platform
    b = os.name
    print('Python version {}.{}.{}'.format(*v))
    print(z)
    print(b)


if __name__ == '__main__':
    main()

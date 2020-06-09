#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import time


def elapsed_time(f):
    def wrapper():  # this is our function that is wrapped in elapsed_time function.
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1) * 1000} ms')
    return wrapper


@elapsed_time  # this is a decorator
def big_sum():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print(f'Big sum: {sum(num_list)}')

    # this is useful because when you call big_sum, you are calling the function above first,
    # and then calling big_sum


def main():
    big_sum()


if __name__ == '__main__': main()

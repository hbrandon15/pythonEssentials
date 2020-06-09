#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def main():
    try:  # the try method is trying the code below to see if it will execute
        x = int('foo')
    except ValueError:  # if you have a guess that a user will enter a wrong value, you can catch
        # that error and do something else with the code itself.
        print('I caught a ValueError')
    except ZeroDivisionError:
        print('Dont divide by zero')
    except:  # This is a default exception that will catch any error
        print('unknown error')
    else:
        print('Good job! no errors!')


# when looking at the traceback for the error created. you read bottom to top
# The bottom line will tell you where the error is and the line above that is where the error was
# called from.


if __name__ == '__main__':
    main()

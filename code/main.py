#!/usr/bin/env python3

import os


def factorial(n):
    print('factorial({})'.format(n))
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def dec2bin(n):
    print('dec2bin({})'.format(n))
    if n == 0:
        return ''
    else:
        return dec2bin(n//2) + str(n % 2)


if __name__ == '__main__':
    print('Hello World!')
    os.exit(0)

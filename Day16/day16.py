#!/usr/bin/python
"""Advent of Code 2016, Day 16, Part 1 and Part 2

https://adventofcode.com/2016/day/16

Apply a "dragon algorithm" to a string of binary digits, then apply a reducing algorithm.
Part 2 increases the size.

Author: Tim Behrendsen
"""

init_state = '10010000000110000'

def calc(fill_len):
    a = list(map(int, init_state))

    # Apply the algorithm to increase the length, and truncate
    while len(a) < fill_len:
        a += [ 0 ] + list(1-x for x in reversed(a))
    a = a[:fill_len]

    # Reduce to the checksum
    while (len(a) & 1) == 0:
        a = [1 if a[i] == a[i+1] else 0 for i in range(0, len(a), 2)]

    return ''.join(map(str, a))

print(f"Part 1: {calc(272)}")
print(f"Part 2: {calc(35651584)}")

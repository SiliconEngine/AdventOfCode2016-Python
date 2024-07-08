#!/usr/bin/python
"""Advent of Code 2016, Day 9, Part 1 and Part 2

https://adventofcode.com/2016/day/9

Input data is a sequence of characters with repeat counts in parenethesis. Part 1
calculates the total length of the final sequence, accounting for the repeating, but not
repeating the repeat counts. Part 2 allows repeat count sequences to themselves be
repeated, which is solved with recursion.

Part 1 example: A(2x2)BCD(2x2)EFG = 11
Part 2 example: (25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN = 445

See file.dat for full data.

Author: Tim Behrendsen
"""

fn = 'file.dat'

def calc(data, part):
    output_len, i = 0, 0
    while i < len(data):
        if data[i] == '(':
            rp = data.index(')', i)
            p1, p2 = map(int, data[i+1:rp].split('x'))
            # Part 1: Just the length times the count.
            # Part 2: Take the sub-string as-is and recurse, multiply by the count.
            output_len += p1 * p2 if part == 1 else p2 * calc(data[rp+1:rp+p1+1], 2)
            i = rp+p1+1
        else:
            output_len += 1
            i += 1

    return output_len

with open(fn, 'r') as file:
    data = file.readline().strip()

print(f"Part 1 is {calc(data, part=1)}")
print(f"Part 2 is {calc(data, part=2)}")

#!/usr/bin/python
"""Advent of Code 2016, Day 18, Part 1 and Part 2

https://adventofcode.com/2016/day/18

Implements a 1D cellular automata and counts the number of spaces. Part 2 just
increases the number of cycles.

See map.dat for full data.

Author: Tim Behrendsen
"""

fn = 'map.dat'
traps = ('^^.', '.^^', '^..', '..^')

def run(first_row, cycles):
    row, row_len = list(first_row), len(first_row)
    get = lambda i: '.' if i < 0 or i >= row_len else row[i]

    total = sum(c == '.' for c in row)
    for cycle in range(cycles-1):
        row = ['^' if get(i-1) + get(i) + get(i+1) in traps else '.' for i in range(row_len)]
        total += sum(c == '.' for c in row)

    return total

with open(fn, 'r') as file:
    first_row = file.readline().strip()

print(f"Part 1 is {run(first_row, 40)}")
print(f"Part 2 is {run(first_row, 400000)}")

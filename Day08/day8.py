#!/usr/bin/python
"""Advent of Code 2016, Day 8, Part 1 and Part 2

https://adventofcode.com/2016/day/8

We're given instructions to draw pixels on a display, then rotate rows or columns
by various amounts. Part 1 counts the number of final pixels, and Part 2 displays
the drawn letters.

See ops.dat for full data.

Author: Tim Behrendsen
"""

import re

fn = 'ops.dat'

screen = [ [ '.' ] * 50 for _ in range(6) ]

with open(fn, 'r') as file:
    for op in file:
        p1, p2 = map(int, re.findall(r'\d+', op))
        if op[0:4] == 'rect':   # Draw rectangle
            for y in range(p2):
                screen[y][:p1] = ['#'] * p1

        elif op[7] == 'r':      # Rotate row
            screen[p1] = screen[p1][-p2:] + screen[p1][:-p2]

        else:                   # Rotate Column
            col = [screen[r][p1] for r in range(6)]
            for r in range(0, 6):
                screen[r][p1] = col[(r - p2) % 6]

print(f"Part 1: {sum(screen[r][c] == '#' for r in range(6) for c in range(50))}")
print(f"Part 2:\n{chr(10).join(''.join(r) for r in screen)}")

#!/usr/bin/python
"""Advent of Code 2016, Day 3, Part 1 and Part 2

https://adventofcode.com/2016/day/3

Given a list of triangles, calculate how many are valid by ensuring that the sum
of the shortest sides exceeds the long side. Part 1 takes the list as-is, while Part 2
has each set of three rows in a single column is a triangle.

See triangles.dat for full data.

Author: Tim Behrendsen
"""

import re

fn = 'triangles.dat'

def part1(triangles):
    # Note to check a triangle, we don't have to check all combinations of sides,
    # only that the sum of the two smallest exceeds the largest.
    return sum(tri[0]+tri[1] > tri[2] for tri in (sorted(tri) for tri in triangles))

def part2(triangles):
    # Could do this in one line, but makes it pointlessly hard to read
    count = 0
    for r in range(0, len(triangles), 3):
        for c in range(3):
            tri = sorted(triangles[r+i][c] for i in range(3))
            count += tri[0]+tri[1] > tri[2]

    return count

with open(fn, 'r') as file:
    triangles = [ list(map(int, re.findall('\d+', line))) for line in file ]

print(f"Part 1: {part1(triangles)}")
print(f"Part 2: {part2(triangles)}")
